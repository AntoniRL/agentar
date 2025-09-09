# agentar_replay.py
# Replayer logu Agentar:
# - czyta cały plik logów
# - parsuje pierwsze "(LOGGING) [[...]]" jako WORLD ([stench,wampus,breeze,pit,gold])
# - odtwarza sekwencję AGENT POS + "Killing the wampus at (...)" + event ze złotem

import ast
import re
import sys
import tkinter as tk

LOG_PATH_DEFAULT = "logs/agentar.log"

CELL = 64
MARGIN = 8
STEP_MS_DEFAULT = 300  # domyślna prędkość odtwarzania (ms/zdarzenie)

# Kolory
COL_BG = "#ffffff"
COL_GRID = "#cccccc"
COL_STENCH = "#c7f5d9"
COL_BREEZE = "#d9ebff"
COL_PIT_TXT = "#444444"
COL_WUMPUS_TXT = "#aa2222"
COL_GOLD_TXT = "#b58900"
COL_AGENT_TXT = "#000000"
COL_KILL_X = "#ff0000"

# Regexy
RE_POS = re.compile(r"AGENT POS::\s*(-?\d+)\s+(-?\d+)")
RE_KILL = re.compile(r"killing the wampus at\s*\(\s*(-?\d+)\s*,\s*(-?\d+)\s*\)", re.IGNORECASE)
RE_GOLD = re.compile(r"(My goal of finding the gold:\s*True|Having gold:\s*True)", re.IGNORECASE)

def extract_world_from_line(line: str):
    if "(LOGGING)" not in line:
        return None
    idx = line.find("(LOGGING)")
    if idx == -1:
        return None
    start = line.find("[", idx)
    if start == -1:
        return None
    payload = line[start:].strip()
    try:
        world = ast.literal_eval(payload)
        if isinstance(world, list) and world and all(isinstance(r, list) for r in world):
            # Minimalna walidacja wymiarów
            H = len(world)
            W = len(world[0]) if H > 0 else 0
            if H >= 1 and W >= 1:
                return world
    except Exception:
        return None
    return None

def parse_log(path: str):
    """Zwraca (world, events). events = lista (typ, payload, surowa_linia)."""
    with open(path, "r", encoding="utf-8", errors="ignore") as fh:
        lines = fh.readlines()

    world = None
    events = []

    for line in lines:
        if world is None:
            w = extract_world_from_line(line)
            if w is not None:
                world = w
                # nie przerywamy – dalej zbieramy eventy
        # AGENT POS
        m = RE_POS.search(line)
        if m:
            x = int(m.group(1)); y = int(m.group(2))
            events.append(("pos", (x, y), line.rstrip()))
            continue
        # KILL WUMPUS
        m = RE_KILL.search(line)
        if m:
            kx = int(m.group(1)); ky = int(m.group(2))
            events.append(("kill", (kx, ky), line.rstrip()))
            continue
        # GOLD
        if RE_GOLD.search(line):
            events.append(("gold", None, line.rstrip()))
            continue

    return world, events

class ReplayApp:
    def __init__(self, world, events):
        self.world = world
        self.events = events
        self.idx = 0               # indeks aktualnego zdarzenia
        self.paused = False
        self.step_ms = STEP_MS_DEFAULT

        # Wymiary
        self.H = len(self.world)
        self.W = len(self.world[0])

        # Szukamy pola Wumpusa z planszy (jeśli zaznaczono)
        self.wumpus_pos = None
        for y in range(self.H):
            for x in range(self.W):
                cell = self.world[y][x]
                if isinstance(cell, (list, tuple)) and len(cell) >= 2 and cell[1] == 1:
                    self.wumpus_pos = (x, y)

        # GUI
        self.root = tk.Tk()
        self.root.title("Agentar Replay")
        top = tk.Frame(self.root); top.pack(fill="x")
        self.status = tk.StringVar(value="Gotowy")
        tk.Label(top, textvariable=self.status, anchor="w").pack(side="left", fill="x", expand=True)
        self.speed_lbl = tk.StringVar(value=f"{self.step_ms} ms/step  (spacja=pauza, [=wolniej, ]=szybciej, r=restart)")
        tk.Label(top, textvariable=self.speed_lbl, anchor="e").pack(side="right")

        cw = self.W * CELL + 2*MARGIN
        ch = self.H * CELL + 2*MARGIN
        self.canvas = tk.Canvas(self.root, width=cw, height=ch, bg=COL_BG, highlightthickness=0)
        self.canvas.pack()

        # Rysunki na canvasie
        self.agent_item = None
        self.kill_item = None  # X nad Wumpusem
        self.visited_marks = []  # opcjonalne kropki ścieżki

        # Klawisze
        self.root.bind("<space>", self.toggle_pause)
        self.root.bind("[", self.slower)
        self.root.bind("]", self.faster)
        self.root.bind("r", self.restart)
        self.root.bind("<Escape>", lambda e: self.root.destroy())
        self.root.bind("q", lambda e: self.root.destroy())

        # Start
        self.draw_world()
        self.root.after(self.step_ms, self.tick)

    # ---- sterowanie ----
    def toggle_pause(self, _=None):
        self.paused = not self.paused
        self.status.set(("Pauza" if self.paused else "Odtwarzanie") + f" — krok {self.idx}/{len(self.events)}")

    def slower(self, _=None):
        self.step_ms = min(2000, self.step_ms + 100)
        self.speed_lbl.set(f"{self.step_ms} ms/step  (spacja=pauza, [=wolniej, ]=szybciej, r=restart)")

    def faster(self, _=None):
        self.step_ms = max(20, self.step_ms - 100)
        self.speed_lbl.set(f"{self.step_ms} ms/step  (spacja=pauza, [=wolniej, ]=szybciej, r=restart)")

    def restart(self, _=None):
        self.idx = 0
        self.paused = False
        # wyczyść agenta, X, ślady
        if self.agent_item is not None:
            self.canvas.delete(self.agent_item)
            self.agent_item = None
        if self.kill_item is not None:
            self.canvas.delete(self.kill_item)
            self.kill_item = None
        for it in self.visited_marks:
            self.canvas.delete(it)
        self.visited_marks.clear()
        self.status.set("Restart — odtwarzanie od początku")

    # ---- rysowanie ----
    def draw_world(self):
        self.canvas.delete("all")
        # siatka i cechy
        for y in range(self.H):
            for x in range(self.W):
                x0 = MARGIN + x*CELL
                y0 = MARGIN + y*CELL
                x1 = x0 + CELL
                y1 = y0 + CELL
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=COL_BG, outline=COL_GRID)

                try:
                    stench, wampus, breeze, pit, gold = self.world[y][x]
                except Exception:
                    continue

                if stench:
                    self.canvas.create_rectangle(x0+2, y0+2, x1-2, y0 + CELL*0.25, fill=COL_STENCH, outline="")
                if breeze:
                    self.canvas.create_rectangle(x0+2, y1 - CELL*0.25, x1-2, y1-2, fill=COL_BREEZE, outline="")

                cx = x0 + CELL/2
                cy = y0 + CELL/2
                if pit:
                    self.canvas.create_text(cx, cy, text="P", fill=COL_PIT_TXT,
                                            font=("TkDefaultFont", int(CELL*0.35), "bold"))
                if wampus:
                    self.canvas.create_text(cx, cy, text="W", fill=COL_WUMPUS_TXT,
                                            font=("TkDefaultFont", int(CELL*0.35), "bold"))
                if gold:
                    self.canvas.create_text(cx, y0 + CELL*0.7, text="G", fill=COL_GOLD_TXT,
                                            font=("TkDefaultFont", int(CELL*0.28), "bold"))

        # obramowanie
        self.canvas.create_rectangle(MARGIN, MARGIN,
                                     MARGIN + self.W*CELL, MARGIN + self.H*CELL,
                                     outline=COL_GRID, width=2)

    def set_agent(self, pos):
        x, y = pos
        if not (0 <= x < self.W and 0 <= y < self.H):
            self.status.set(f"Poza planszą: {pos} — pomijam (krok {self.idx}/{len(self.events)})")
            return
        cx = MARGIN + x * CELL + CELL/2
        cy = MARGIN + y * CELL + CELL/2
        # ślad
        dot = self.canvas.create_oval(cx-3, cy-3, cx+3, cy+3, fill="#888888", outline="")
        self.visited_marks.append(dot)
        # agent
        if self.agent_item is None:
            self.agent_item = self.canvas.create_text(cx, cy, text="A", fill=COL_AGENT_TXT,
                                                      font=("TkDefaultFont", int(CELL*0.5), "bold"))
        else:
            self.canvas.coords(self.agent_item, cx, cy)

    def mark_kill(self, wpos_from_log):
        # Zaznacz czerwone 'X' w miejscu wampusa (z logu lub z mapy, jeśli brak payloadu)
        if wpos_from_log is not None:
            wx, wy = wpos_from_log
        elif self.wumpus_pos is not None:
            wx, wy = self.wumpus_pos
        else:
            return
        if not (0 <= wx < self.W and 0 <= wy < self.H):
            return
        x0 = MARGIN + wx * CELL
        y0 = MARGIN + wy * CELL
        x1 = x0 + CELL
        y1 = y0 + CELL
        # usuń poprzednie X (jeśli było)
        if self.kill_item is not None:
            self.canvas.delete(self.kill_item)
            self.kill_item = None
        # rysuj X
        l1 = self.canvas.create_line(x0+8, y0+8, x1-8, y1-8, fill=COL_KILL_X, width=3)
        l2 = self.canvas.create_line(x1-8, y0+8, x0+8, y1-8, fill=COL_KILL_X, width=3)
        # grupowanie (trik: zapamiętujemy jeden z elementów — drugi zostawiamy)
        self.kill_item = l1

    # ---- pętla odtwarzania ----
    def tick(self):
        if not self.paused and self.idx < len(self.events):
            etype, payload, raw = self.events[self.idx]
            if etype == "pos":
                self.set_agent(payload)
                self.status.set(f"POS {payload}  — krok {self.idx+1}/{len(self.events)}")
            elif etype == "kill":
                self.mark_kill(payload)
                self.status.set(f"KILL at {payload}  — krok {self.idx+1}/{len(self.events)}")
            elif etype == "gold":
                self.status.set(f"GOLD event  — krok {self.idx+1}/{len(self.events)}")
            else:
                self.status.set(f"{etype} — krok {self.idx+1}/{len(self.events)}")
            self.idx += 1

        # zaplanuj kolejny krok
        self.root.after(self.step_ms, self.tick)

    def run(self):
        self.root.mainloop()

def main():
    path = LOG_PATH_DEFAULT if len(sys.argv) < 2 else sys.argv[1]
    world, events = parse_log(path)
    if world is None:
        print("Nie znaleziono planszy (wpisu '(LOGGING) [...]') w logu:", path)
        sys.exit(1)
    if not events:
        print("Brak zdarzeń do odtworzenia w logu:", path)
        sys.exit(1)
    app = ReplayApp(world, events)
    app.run()

if __name__ == "__main__":
    main()
