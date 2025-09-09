# agentar_replay.py
# Replayer logu Agentar:
# - parsuje pierwszy "(LOGGING) [[...]]" jako WORLD ([stench,wampus,breeze,pit,gold])
# - odtwarza "AGENT POS:: x y", "killing the wampus at (x, y)" i zdarzenia GOLD
# - rysuje strzałki trasy, start, oraz mini-grafikę agenta

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
COL_STENCH = "#c7f5d9"   # pasek u góry
COL_BREEZE = "#d9ebff"   # pasek u dołu
COL_PIT_TXT = "#444444"
COL_WUMPUS_TXT = "#aa2222"
COL_GOLD_TXT = "#b58900"
COL_AGENT_BODY = "#222222"
COL_AGENT_NOSE = "#4444aa"
COL_ARROW = "#888888"
COL_START = "#16a34a"
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
        m = RE_POS.search(line)
        if m:
            x = int(m.group(1)); y = int(m.group(2))
            events.append(("pos", (x, y), line.rstrip()))
            continue
        m = RE_KILL.search(line)
        if m:
            kx = int(m.group(1)); ky = int(m.group(2))
            events.append(("kill", (kx, ky), line.rstrip()))
            continue
        if RE_GOLD.search(line):
            events.append(("gold", None, line.rstrip()))
            continue

    return world, events

class ReplayApp:
    def __init__(self, world, events):
        self.world = world
        self.events = events
        self.idx = 0
        self.paused = False
        self.step_ms = STEP_MS_DEFAULT

        self.H = len(world)
        self.W = len(world[0])

        # Pozycja Wumpusa z planszy (jeśli podana)
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
        self.speed_lbl = tk.StringVar(value=f"{self.step_ms} ms/step (spacja=pauza, [=wolniej, ]=szybciej, r=restart)")
        tk.Label(top, textvariable=self.speed_lbl, anchor="e").pack(side="right")

        cw = self.W * CELL + 2 * MARGIN
        ch = self.H * CELL + 2 * MARGIN
        self.canvas = tk.Canvas(self.root, width=cw, height=ch, bg=COL_BG, highlightthickness=0)
        self.canvas.pack()

        # Rysunki
        self.agent_items = []     # elementy graficzne agenta (do łatwego usuwania/przerysowania)
        self.prev_pos = None      # poprzednia pozycja (do strzałek i orientacji)
        self.arrows = []          # id linii-strzałek
        self.kill_items = []      # X na wumpusie
        self.start_item = None    # marker startu

        # Sterowanie
        self.root.bind("<space>", self.toggle_pause)
        self.root.bind("[", self.slower)
        self.root.bind("]", self.faster)
        self.root.bind("r", self.restart)
        self.root.bind("<Escape>", lambda e: self.root.destroy())
        self.root.bind("q", lambda e: self.root.destroy())

        # Start
        self.draw_world()
        self.find_and_mark_start()  # na podstawie pierwszej sensownej pozycji
        self.root.after(self.step_ms, self.tick)

    # ---------- Sterowanie ----------
    def toggle_pause(self, _=None):
        self.paused = not self.paused
        self.status.set(("Pauza" if self.paused else "Odtwarzanie") + f" — krok {self.idx}/{len(self.events)}")

    def slower(self, _=None):
        self.step_ms = min(2000, self.step_ms + 100)
        self.speed_lbl.set(f"{self.step_ms} ms/step (spacja=pauza, [=wolniej, ]=szybciej, r=restart)")

    def faster(self, _=None):
        self.step_ms = max(20, self.step_ms - 100)
        self.speed_lbl.set(f"{self.step_ms} ms/step (spacja=pauza, [=wolniej, ]=szybciej, r=restart)")

    def restart(self, _=None):
        self.idx = 0
        self.paused = False
        self.prev_pos = None
        # usuń agenta, strzałki, X
        for it in self.agent_items:
            self.canvas.delete(it)
        self.agent_items.clear()
        for it in self.arrows:
            self.canvas.delete(it)
        self.arrows.clear()
        for it in self.kill_items:
            self.canvas.delete(it)
        self.kill_items.clear()
        # start rysujemy ponownie
        if self.start_item is not None:
            self.canvas.delete(self.start_item)
            self.start_item = None
        self.find_and_mark_start()
        self.status.set("Restart — odtwarzanie od początku")

    # ---------- Rysowanie planszy ----------
    def draw_world(self):
        self.canvas.delete("all")
        for y in range(self.H):
            for x in range(self.W):
                x0 = MARGIN + x * CELL
                y0 = MARGIN + y * CELL
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

        self.canvas.create_rectangle(MARGIN, MARGIN,
                                     MARGIN + self.W * CELL,
                                     MARGIN + self.H * CELL,
                                     outline=COL_GRID, width=2)

    # ---------- Start & strzałki ----------
    def find_and_mark_start(self):
        # znajdź pierwszą pozycję w granicach planszy
        start = None
        for etype, payload, _ in self.events:
            if etype == "pos":
                x, y = payload
                if 0 <= x < self.W and 0 <= y < self.H:
                    start = (x, y)
                    break
        if start is None:
            return
        # zapamiętaj jako poprzednią pozycję (żeby pierwsza strzałka była od startu do kolejnego ruchu)
        self.prev_pos = start

        # marker startu: zielony pierścień + S
        cx, cy = self.cell_center(start)
        r = CELL * 0.32
        ring = self.canvas.create_oval(cx - r, cy - r, cx + r, cy + r,
                                       outline=COL_START, width=3)
        label = self.canvas.create_text(cx, cy, text="S", fill=COL_START,
                                        font=("TkDefaultFont", int(CELL*0.35), "bold"))
        # grupa jako jeden „item” (zapamiętujemy pierwszy id)
        self.start_item = ring

        # narysuj agenta w pozycji startowej (domyślna orientacja: w prawo)
        self.draw_agent(start, direction="E")

    def draw_arrow(self, a, b):
        """Rysuje strzałkę od komórki a do b (jeśli obie są w granicach)."""
        if not (self.in_bounds(a) and self.in_bounds(b)):
            return
        x0, y0 = self.cell_center(a)
        x1, y1 = self.cell_center(b)
        # skróć linię, żeby nie nachodziła na obrys kółka agenta
        shrink = CELL * 0.2
        dx, dy = x1 - x0, y1 - y0
        dist = max(1, (abs(dx) + abs(dy)))
        if dx != 0:
            x0 += shrink * (1 if dx > 0 else -1)
            x1 -= shrink * (1 if dx > 0 else -1)
        if dy != 0:
            y0 += shrink * (1 if dy > 0 else -1)
            y1 -= shrink * (1 if dy > 0 else -1)
        line = self.canvas.create_line(x0, y0, x1, y1, fill=COL_ARROW, width=2,
                                       arrow="last", arrowshape=(12, 12, 4))
        self.arrows.append(line)

    # ---------- Grafika agenta ----------
    def draw_agent(self, pos, direction="E"):
        """Tworzy/przesuwa mini-grafikę agenta (kółko + „nosek”)."""
        # usuń poprzednią grafikę
        for it in self.agent_items:
            self.canvas.delete(it)
        self.agent_items.clear()

        cx, cy = self.cell_center(pos)
        r = CELL * 0.28

        body = self.canvas.create_oval(cx - r, cy - r, cx + r, cy + r,
                                       fill=COL_AGENT_BODY, outline="")
        # nos (trójkąt wskazujący kierunek ruchu)
        if direction == "N":
            pts = (cx, cy - r*0.9,  cx - r*0.35, cy - r*0.2,  cx + r*0.35, cy - r*0.2)
        elif direction == "S":
            pts = (cx, cy + r*0.9,  cx - r*0.35, cy + r*0.2,  cx + r*0.35, cy + r*0.2)
        elif direction == "W":
            pts = (cx - r*0.9, cy,  cx - r*0.2, cy - r*0.35,  cx - r*0.2, cy + r*0.35)
        else:  # "E"
            pts = (cx + r*0.9, cy,  cx + r*0.2, cy - r*0.35,  cx + r*0.2, cy + r*0.35)
        nose = self.canvas.create_polygon(*pts, fill=COL_AGENT_NOSE, outline="")

        self.agent_items.extend([body, nose])

    # ---------- Helpers ----------
    def in_bounds(self, pos):
        x, y = pos
        return 0 <= x < self.W and 0 <= y < self.H

    def cell_center(self, pos):
        x, y = pos
        return (MARGIN + x * CELL + CELL/2,
                MARGIN + y * CELL + CELL/2)

    def step_direction(self, a, b):
        """Zwraca 'N','E','S','W' na podstawie ruchu z a do b."""
        ax, ay = a; bx, by = b
        if bx > ax: return "E"
        if bx < ax: return "W"
        if by > ay: return "S"
        return "N"

    def mark_kill(self, wpos_from_log):
        if wpos_from_log is not None:
            wx, wy = wpos_from_log
        elif self.wumpus_pos is not None:
            wx, wy = self.wumpus_pos
        else:
            return
        if not self.in_bounds((wx, wy)):
            return
        x0 = MARGIN + wx * CELL
        y0 = MARGIN + wy * CELL
        x1 = x0 + CELL
        y1 = y0 + CELL
        l1 = self.canvas.create_line(x0+8, y0+8, x1-8, y1-8, fill=COL_KILL_X, width=3)
        l2 = self.canvas.create_line(x1-8, y0+8, x0+8, y1-8, fill=COL_KILL_X, width=3)
        self.kill_items.extend([l1, l2])

    # ---------- Pętla odtwarzania ----------
    def tick(self):
        if not self.paused and self.idx < len(self.events):
            etype, payload, raw = self.events[self.idx]
            if etype == "pos":
                pos = payload
                if self.in_bounds(pos):
                    # strzałka od poprzedniej pozycji
                    if self.prev_pos is not None and self.in_bounds(self.prev_pos) and self.prev_pos != pos:
                        self.draw_arrow(self.prev_pos, pos)
                        dirc = self.step_direction(self.prev_pos, pos)
                    else:
                        dirc = "E"
                    # przerysuj agenta
                    self.draw_agent(pos, direction=dirc)
                    self.prev_pos = pos
                    self.status.set(f"POS {pos}  — krok {self.idx+1}/{len(self.events)}")
                else:
                    self.status.set(f"Poza planszą: {pos} — pomijam  (krok {self.idx+1}/{len(self.events)})")

            elif etype == "kill":
                self.mark_kill(payload)
                self.status.set(f"KILL at {payload}  — krok {self.idx+1}/{len(self.events)}")

            elif etype == "gold":
                self.status.set(f"GOLD event  — krok {self.idx+1}/{len(self.events)}")

            self.idx += 1

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
