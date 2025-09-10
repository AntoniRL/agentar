#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import re
import ast
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

DARK_GRAY = "#333333"
WHITE = "#FFFFFF"
YELLOW = "#FFD54A"
GRID_LINE = "#DDDDDD"

CELL_SIZE = 28          # piksele na kratkę
PADDING = 10            # margines wewnętrzny wokół planszy
FONT_FAMILY = "Arial"
FONT_SIZE = 12

WORLD_RE = re.compile(r"WORLD::\s*(\[\[.*?\]\])", re.DOTALL)

def extract_worlds(text: str):
    """Zwraca listę macierzy (list[list[int]]) z logów."""
    worlds = []
    for m in WORLD_RE.finditer(text):
        try:
            mat = ast.literal_eval(m.group(1))
            # Weryfikacja, że to lista list liczb
            if isinstance(mat, list) and all(isinstance(r, list) for r in mat):
                worlds.append(mat)
        except Exception:
            # Ignoruj błędne wpisy
            pass
    # Deduplikacja sąsiadujących klatek, by suwak był przyjemniejszy
    deduped = []
    prev = None
    for w in worlds:
        if w != prev:
            deduped.append(w)
            prev = w
    return deduped

class WorldViewer(tk.Tk):
    def __init__(self, worlds):
        super().__init__()
        self.title("Agentar WORLD Viewer")
        self.worlds = worlds if worlds else []
        self.current_idx = 0

        self._build_ui()
        self._load_world(0 if self.worlds else None)

    def _build_ui(self):
        top = ttk.Frame(self)
        top.pack(side=tk.TOP, fill=tk.X, padx=8, pady=6)

        self.info_lbl = ttk.Label(top, text="Brak danych WORLD", font=(FONT_FAMILY, 10))
        self.info_lbl.pack(side=tk.LEFT)

        ttk.Button(top, text="Otwórz log...", command=self._open_file).pack(side=tk.RIGHT, padx=4)

        # Canvas + scrollbar (tylko pionowy przyda się przy dużych siatkach)
        canvas_frame = ttk.Frame(self)
        canvas_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=8, pady=4)

        self.canvas = tk.Canvas(canvas_frame, bg="white", highlightthickness=1, highlightbackground="#CCCCCC")
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        yscroll = ttk.Scrollbar(canvas_frame, orient="vertical", command=self.canvas.yview)
        yscroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.canvas.configure(yscrollcommand=yscroll.set)

        # Suwak do wyboru klatki
        bottom = ttk.Frame(self)
        bottom.pack(side=tk.BOTTOM, fill=tk.X, padx=8, pady=8)

        self.slider = ttk.Scale(bottom, from_=0, to=max(0, len(self.worlds)-1),
                                orient="horizontal", command=self._on_slide)
        self.slider.pack(side=tk.LEFT, fill=tk.X, expand=True)

        self.frame_lbl = ttk.Label(bottom, text="0/0")
        self.frame_lbl.pack(side=tk.LEFT, padx=8)

        # Kliknięcia w canvas pozwalają przełączać się między klatkami klawiszami ← →
        self.bind("<Left>", lambda e: self._step(-1))
        self.bind("<Right>", lambda e: self._step(+1))
        self.canvas.bind("<Configure>", lambda e: self._redraw())

    def _open_file(self):
        path = filedialog.askopenfilename(title="Wybierz plik logów",
                                          filetypes=[("Pliki logów", "*.agar *.log *.txt"), ("Wszystkie pliki", "*.*")])
        if not path:
            return
        try:
            with open(path, "r", encoding="utf-8", errors="ignore") as f:
                text = f.read()
            worlds = extract_worlds(text)
            if not worlds:
                messagebox.showwarning("Brak WORLD", "Nie znaleziono wpisów WORLD w wybranym pliku.")
                return
            self.worlds = worlds
            self.slider.configure(to=len(self.worlds)-1)
            self._load_world(0)
        except Exception as e:
            messagebox.showerror("Błąd", f"Nie udało się wczytać pliku:\n{e}")

    def _on_slide(self, _val):
        idx = int(float(self.slider.get()))
        if idx != self.current_idx:
            self._load_world(idx)

    def _step(self, delta):
        if not self.worlds:
            return
        idx = max(0, min(len(self.worlds)-1, self.current_idx + delta))
        self.slider.set(idx)
        self._load_world(idx)

    def _load_world(self, idx):
        if idx is None or not self.worlds:
            self.info_lbl.config(text="Brak danych WORLD")
            self.frame_lbl.config(text="0/0")
            self.canvas.delete("all")
            return
        self.current_idx = idx
        self.world = self.worlds[idx]
        rows = len(self.world)
        cols = len(self.world[0]) if rows else 0
        self.info_lbl.config(text=f"Klatka: {idx+1}/{len(self.worlds)} | Rozmiar: {rows}×{cols}")
        self.frame_lbl.config(text=f"{idx+1}/{len(self.worlds)}")
        # Dopasuj wirtualny rozmiar canvasu (scrollregion); render w _redraw
        width = cols * CELL_SIZE + 2 * PADDING
        height = rows * CELL_SIZE + 2 * PADDING
        self.canvas.configure(scrollregion=(0, 0, width, height))
        self._redraw()

    def _redraw(self):
        if not hasattr(self, "world"):
            return
        self.canvas.delete("all")
        rows = len(self.world)
        cols = len(self.world[0]) if rows else 0

        # Tło robocze
        self.canvas.create_rectangle(0, 0,
                                     cols * CELL_SIZE + 2 * PADDING,
                                     rows * CELL_SIZE + 2 * PADDING,
                                     fill=WHITE, width=0)

        # Rysuj komórki
        for r, row in enumerate(self.world):
            for c, val in enumerate(row):
                x0 = PADDING + c * CELL_SIZE
                y0 = PADDING + r * CELL_SIZE
                x1 = x0 + CELL_SIZE
                y1 = y0 + CELL_SIZE

                if val == -1:
                    fill = DARK_GRAY
                else:
                    fill = WHITE

                # pole
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=fill, outline=GRID_LINE)

                # liczba
                if isinstance(val, int) and val > 0:
                    self.canvas.create_text(
                        (x0 + x1) // 2,
                        (y0 + y1) // 2,
                        text=str(val),
                        fill=YELLOW,
                        font=(FONT_FAMILY, FONT_SIZE, "bold")
                    )

def main():
    # Plik można podać jako argument, w przeciwnym razie używamy domyślnej ścieżki.
    path = sys.argv[1] if len(sys.argv) > 1 else "logs/agentar.agar"
    try:
        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            text = f.read()
    except FileNotFoundError:
        text = ""  # pozwoli włączyć appkę i wczytać plik z menu
    worlds = extract_worlds(text)

    app = WorldViewer(worlds)
    app.minsize(500, 400)
    app.mainloop()

if __name__ == "__main__":
    main()