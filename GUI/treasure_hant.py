#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import io
import re
import ast
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

# === Kolory i stałe UI ===
DARK_GRAY = "#333333"
WHITE = "#FFFFFF"
YELLOW = "#FFD54A"
GRID_LINE = "#DDDDDD"

AGENT_COLORS = {
    "GREEN": "#00C853",
    "RED": "#FF5252",
    "BLUE": "#40C4FF",
    "YELLOW": "#FFD740",
    "PURPLE": "#B388FF",
    "ORANGE": "#FFAB40",
}

CELL_SIZE = 28
PADDING = 10
FONT_FAMILY = "Arial"
FONT_SIZE = 12

# === RegEx do parsowania logów ===
# WORLD bywa w jednej linii – taki regex jest szybki i stabilny
WORLD_RE = re.compile(r"WORLD::\s*(\[\[.*\]\])")

# „GREEN start position:: (x,y)”
START_POS_RE = re.compile(
    r"\(PRINTING\)\s*([A-Z]+)\s+start position::\s*\(\s*(\d+)\s*,\s*(\d+)\s*\)"
)

# „GREEN POSSITION:: (x,y)” / „GREEN POSITION:: (x,y)” – dopuszczam literówki
CUR_POS_RE = re.compile(
    r"\(PRINTING\)\s*([A-Z]+)\s+PO?S+I?T+I?O?N::\s*\(\s*(\d+)\s*,\s*(\d+)\s*\)",
    re.IGNORECASE,
)

# Wyciąga identyfikator aktora z nagłówka linii (np. ".1.1.1.2::")
ACTOR_ID_RE = re.compile(r"INFO:\s+([.0-9]+)::")

def safe_literal_eval(text):
    try:
        return ast.literal_eval(text)
    except Exception:
        return None

def extract_world_from_line(line: str):
    m = WORLD_RE.search(line)
    if not m:
        return None
    mat = safe_literal_eval(m.group(1))
    if isinstance(mat, list) and mat and all(isinstance(r, list) for r in mat):
        return mat
    return None

def extract_start_pos_from_line(line: str):
    m = START_POS_RE.search(line)
    if not m:
        return None
    color, xs, ys = m.groups()
    return color.upper(), int(xs), int(ys)

def extract_cur_pos_from_line(line: str):
    m = CUR_POS_RE.search(line)
    if not m:
        return None
    color, xs, ys = m.groups()
    return color.upper(), int(xs), int(ys)

def extract_actor_id(line: str):
    m = ACTOR_ID_RE.search(line)
    return m.group(1) if m else "?"

def hex_to_rgb(hx: str):
    hx = hx.lstrip("#")
    return tuple(int(hx[i:i+2], 16) for i in (0, 2, 4))

def rgb_to_hex(rgb):
    return "#{:02X}{:02X}{:02X}".format(*rgb)

def darken(hex_color: str, factor: float = 0.7):
    r, g, b = hex_to_rgb(hex_color)
    r = int(max(0, min(255, r * factor)))
    g = int(max(0, min(255, g * factor)))
    b = int(max(0, min(255, b * factor)))
    return rgb_to_hex((r, g, b))

def color_for(name: str):
    base = AGENT_COLORS.get(name.upper())
    if base:
        return base
    # deterministyczny fallback z nazwy koloru
    h = abs(hash(name)) % 0xFFFFFF
    return "#{:06X}".format(h)

# --------- Tailer (działa jak `tail -F`) ---------
class LogTailer:
    def __init__(self, path):
        self.path = path
        self.file = None
        self.inode = None
        self.buf = ""

    def open(self, start_at_end=True):
        if not self.path:
            return False
        try:
            self.file = open(self.path, "r", encoding="utf-8", errors="ignore")
            self.inode = os.fstat(self.file.fileno()).st_ino
            self.buf = ""
            self.file.seek(0, io.SEEK_END if start_at_end else io.SEEK_SET)
            return True
        except Exception:
            return False

    def close(self):
        try:
            if self.file:
                self.file.close()
        finally:
            self.file = None
            self.inode = None

    def _reopen_if_rotated(self):
        try:
            st = os.stat(self.path)
        except Exception:
            return
        if self.file is None:
            self.open()
            return
        if st.st_ino != self.inode or st.st_size < self.file.tell():
            self.close()
            self.open(start_at_end=False)

    def read_all_existing_lines(self):
        if not self.file:
            if not self.open(start_at_end=False):
                return []
        self.file.seek(0, io.SEEK_SET)
        data = self.file.read()
        lines = data.splitlines()
        self.file.seek(0, io.SEEK_END)
        self.buf = ""
        return lines

    def read_new_lines(self):
        self._reopen_if_rotated()
        if not self.file:
            return []
        chunk = self.file.read()
        if not chunk:
            return []
        self.buf += chunk
        if "\n" not in self.buf:
            return []
        parts = self.buf.splitlines(keepends=True)
        if not parts[-1].endswith("\n"):
            self.buf = parts[-1]
            complete = [p.rstrip("\r\n") for p in parts[:-1]]
        else:
            self.buf = ""
            complete = [p.rstrip("\r\n") for p in parts]
        return complete

# --------- Główne okno ---------
class WorldViewer(tk.Tk):
    def __init__(self, initial_worlds=None, path=None):
        super().__init__()
        self.title("Agentar WORLD Viewer (live, multi-agent)")
        self.geometry("1100x760")

        # Dane
        self.worlds = initial_worlds[:] if initial_worlds else []
        self.current_world = self.worlds[-1] if self.worlds else None

        # Agenci: klucz = (color, actor_id)
        self.agent_pos = {}    # { (color, actor): (x,y) }
        self.agent_start = {}  # { (color, actor): (x,y) }

        # Odwiedziny GREEN (zgodnie z wymaganiem)
        self.visited_by_green = set()

        # Tail
        self.tail = None
        self.tail_interval_ms = 300

        # UI
        self._build_ui()

        if path:
            self._start_tail(path)
        else:
            self._update_info()
        self.after(self.tail_interval_ms, self._poll_tail)

    # ---------- UI ----------
    def _build_ui(self):
        # Górny pasek
        top = ttk.Frame(self)
        top.pack(side=tk.TOP, fill=tk.X, padx=8, pady=6)

        self.path_var = tk.StringVar(value="")
        ttk.Label(top, text="Plik:").pack(side=tk.LEFT)
        ttk.Entry(top, textvariable=self.path_var, width=65).pack(side=tk.LEFT, padx=6)
        ttk.Button(top, text="Wybierz...", command=self._open_file_dialog).pack(side=tk.LEFT)
        ttk.Button(top, text="Przeładuj", command=self._reload_file).pack(side=tk.LEFT, padx=6)

        self.info_lbl = ttk.Label(top, text="Brak danych WORLD", font=(FONT_FAMILY, 10))
        self.info_lbl.pack(side=tk.RIGHT)

        # Główna część: płótno + panel boczny (legenda)
        mid = ttk.Frame(self)
        mid.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=8, pady=4)

        # Canvas z pionowym scrollem
        canvas_wrap = ttk.Frame(mid)
        canvas_wrap.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(canvas_wrap, bg="white",
                                highlightthickness=1, highlightbackground="#CCCCCC")
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        yscroll = ttk.Scrollbar(canvas_wrap, orient="vertical", command=self.canvas.yview)
        yscroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.configure(yscrollcommand=yscroll.set)

        self.canvas.bind("<Configure>", lambda e: self._redraw())

        # Prawa kolumna – legenda
        right = ttk.Frame(mid)
        right.pack(side=tk.RIGHT, fill=tk.Y, padx=8)

        ttk.Label(right, text="Agenci", font=(FONT_FAMILY, 12, "bold")).pack(anchor="w", pady=(0, 4))
        self.agent_list = tk.Listbox(right, height=22)
        self.agent_list.pack(fill=tk.Y)
        self.agent_list_tip = ttk.Label(right, text="Kolor = kolor agenta\nID = z nagłówka logu",
                                        font=(FONT_FAMILY, 9))
        self.agent_list_tip.pack(anchor="w", pady=6)

        # Dolny pasek statusu
        bottom = ttk.Frame(self)
        bottom.pack(side=tk.BOTTOM, fill=tk.X, padx=8, pady=8)
        self.status_lbl = ttk.Label(bottom, text="—", anchor="w")
        self.status_lbl.pack(side=tk.LEFT)

    def _open_file_dialog(self):
        path = filedialog.askopenfilename(
            title="Wybierz plik logów",
            filetypes=[("Pliki logów", "*.agar *.log *.txt"), ("Wszystkie pliki", "*.*")]
        )
        if path:
            self._start_tail(path)

    def _reload_file(self):
        path = self.path_var.get().strip()
        if path:
            self._start_tail(path)

    # ---------- Tail / parsing ----------
    def _start_tail(self, path):
        if self.tail:
            self.tail.close()
            self.tail = None

        self.path_var.set(path)
        self.tail = LogTailer(path)
        if not self.tail.open(start_at_end=False):
            messagebox.showerror("Błąd", f"Nie można otworzyć pliku:\n{path}")
            return

        # Reset stanu
        self.worlds.clear()
        self.current_world = None
        self.agent_pos.clear()
        self.agent_start.clear()
        self.visited_by_green.clear()

        # Wczytaj historię
        history_lines = self.tail.read_all_existing_lines()
        if history_lines:
            changed = self._process_lines(history_lines)
            if changed:
                self._redraw()

        self._update_info()

    def _poll_tail(self):
        try:
            if self.tail:
                lines = self.tail.read_new_lines()
                if lines:
                    changed = self._process_lines(lines)
                    if changed:
                        self._redraw()
        finally:
            self.after(self.tail_interval_ms, self._poll_tail)

    def _process_lines(self, lines):
        changed = False
        for line in lines:
            # WORLD
            mat = extract_world_from_line(line)
            if mat is not None:
                if not self.worlds or self.worlds[-1] != mat:
                    self.worlds.append(mat)
                    self.current_world = mat
                    changed = True
                continue

            actor = extract_actor_id(line)

            # Start
            sp = extract_start_pos_from_line(line)
            if sp:
                color, x, y = sp
                key = (color, actor)
                self.agent_start[key] = (x, y)
                self.agent_pos.setdefault(key, (x, y))
                if color == "GREEN":
                    self.visited_by_green.add((x, y))
                changed = True
                continue

            # Bieżąca pozycja
            cp = extract_cur_pos_from_line(line)
            if cp:
                color, x, y = cp
                key = (color, actor)
                self.agent_pos[key] = (x, y)
                if color == "GREEN":
                    self.visited_by_green.add((x, y))
                changed = True
                continue

        if changed:
            self._update_info()
        return changed

    # ---------- Rysowanie ----------
    def _update_info(self):
        rows, cols = (0, 0)
        if self.current_world:
            rows = len(self.current_world)
            cols = len(self.current_world[0]) if rows else 0
        worlds_count = len(self.worlds)
        agents_count = len(self.agent_pos)
        info = f"Klatki WORLD: {worlds_count} | Rozmiar: {rows}×{cols} | Agenci: {agents_count}"
        self.info_lbl.config(text=info)

        width = cols * CELL_SIZE + 2 * PADDING
        height = rows * CELL_SIZE + 2 * PADDING
        self.canvas.configure(scrollregion=(0, 0, width, height))

        # odśwież listę agentów
        self.agent_list.delete(0, tk.END)
        for (color, actor), (x, y) in sorted(self.agent_pos.items(), key=lambda kv: (kv[0][0], kv[0][1])):
            base = color_for(color)
            self.agent_list.insert(tk.END, f"{color:<6} | ID {actor:<8} | pos=({x},{y})")
            # podkoloruj wiersz tłem (tk.Listbox nie wspiera per-row bg bez rozszerzeń — zostawiamy tekstowo)

    def _redraw(self):
        self.canvas.delete("all")
        if not self.current_world:
            self.status_lbl.config(text="Brak WORLD — czekam na dane…")
            return

        rows = len(self.current_world)
        cols = len(self.current_world[0]) if rows else 0

        # Tło
        self.canvas.create_rectangle(
            0, 0,
            cols * CELL_SIZE + 2 * PADDING,
            rows * CELL_SIZE + 2 * PADDING,
            fill=WHITE, width=0
        )

        # Kratki + liczby
        for r, row in enumerate(self.current_world):
            for c, val in enumerate(row):
                x0 = PADDING + c * CELL_SIZE
                y0 = PADDING + r * CELL_SIZE
                x1 = x0 + CELL_SIZE
                y1 = y0 + CELL_SIZE

                fill = DARK_GRAY if val == -1 else WHITE
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=fill, outline=GRID_LINE)

                if isinstance(val, int) and val > 0:
                    self.canvas.create_text(
                        (x0 + x1) // 2,
                        (y0 + y1) // 2,
                        text=str(val),
                        fill=YELLOW,
                        font=(FONT_FAMILY, FONT_SIZE, "bold")
                    )

        # Odwiedziny GREEN – lewy górny trójkąt
        green_fill = color_for("GREEN")
        for (vx, vy) in self.visited_by_green:
            if 0 <= vy < rows and 0 <= vx < cols:
                x0 = PADDING + vx * CELL_SIZE
                y0 = PADDING + vy * CELL_SIZE
                x1 = x0 + CELL_SIZE
                y1 = y0 + CELL_SIZE
                self.canvas.create_polygon(
                    x0, y0,  # lewy górny
                    x1, y0,  # prawy górny
                    x0, y1,  # lewy dolny
                    fill=green_fill,
                    outline="",
                )

        # Starty agentów – ramka przyciemnionym kolorem
        for (color, _actor), (sx, sy) in self.agent_start.items():
            if 0 <= sy < rows and 0 <= sx < cols:
                base = color_for(color)
                dark = darken(base, 0.65)
                x0 = PADDING + sx * CELL_SIZE
                y0 = PADDING + sy * CELL_SIZE
                x1 = x0 + CELL_SIZE
                y1 = y0 + CELL_SIZE
                self.canvas.create_rectangle(x0+1, y0+1, x1-1, y1-1, outline=dark, width=3)

        # Pozycje agentów – literka 's' przyciemnionym kolorem
        for (color, actor), (ax, ay) in self.agent_pos.items():
            if 0 <= ay < rows and 0 <= ax < cols:
                base = color_for(color)
                dark = darken(base, 0.55)
                x0 = PADDING + ax * CELL_SIZE
                y0 = PADDING + ay * CELL_SIZE
                x1 = x0 + CELL_SIZE
                y1 = y0 + CELL_SIZE
                self.canvas.create_text(
                    (x0 + x1) // 2,
                    (y0 + y1) // 2,
                    text="s",
                    fill=dark,
                    font=(FONT_FAMILY, FONT_SIZE - 1, "bold")  # ciut mniejsze „s”
                )
                # mała kropka w rogu komórki, by odróżnić agentów o tym samym kolorze (różne ID)
                self.canvas.create_oval(x1-7, y0+3, x1-3, y0+7, fill=dark, outline=dark)

        self.status_lbl.config(text="OK")

# ---------- main ----------
def main():
    path = sys.argv[1] if len(sys.argv) > 1 else ""
    app = WorldViewer(initial_worlds=None, path=path if path else None)
    app.minsize(720, 520)
    app.mainloop()

if __name__ == "__main__":
    main()
