#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Agentar Log Viewer v2 – poprawiona wersja:
- jasne tło
- aktualny licznik złota obu drużyn
- brak wyświetlania kroków
- szybszy suwak prędkości (10–600 ms)
"""

import ast
import os
import re
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Set, Tuple

Point = Tuple[int, int]

# --- Regexy ---
WORLD_RE = re.compile(r"\(LOGGING\)\s*WORLD::\s*(\[\[.*\]\])")
BASE_RE = re.compile(r"\(PRINTING\)\s*Color\s+(RED|BLUE);\s*start\s+possition:\s*\((\d+),\s*(\d+)\)", re.IGNORECASE)
ID_PREFIX_RE = re.compile(r"INFO:\s*([.\d]+)::")
MOVE_RE = re.compile(
    r"\(PRINTING\)\s*GLOBAL\s+POSSITION::\s*(-?\d+)\s+(-?\d+)\s+RELATIV\s+POSSITION::\s*(-?\d+)\s+(-?\d+)\s+visited::\s*(\d+)\s+GOLD::\s*(\d+)",
    re.IGNORECASE,
)
GOLD_COLLECT_RE = re.compile(r"\(LOGGING\)\s*GOLD\s+colected\s+at\s*\((\d+),\s*(\d+)\)", re.IGNORECASE)
FINISH_RE = re.compile(r"Team\s+(RED|BLUE)\s+finished\s+with:\s*(\d+)\s+GOLD", re.IGNORECASE)


def team_from_agent_id(agent_id: str) -> Optional[str]:
    parts = [p for p in agent_id.split(".") if p.strip()]
    if len(parts) >= 2:
        if parts[1] == "1":
            return "RED"
        if parts[1] == "2":
            return "BLUE"
    return None


def last_digit_from_id(agent_id: str) -> str:
    digits = re.findall(r"\d", agent_id)
    return digits[-1] if digits else "?"


@dataclass
class Event:
    kind: str
    payload: dict


@dataclass
class WorldState:
    grid: List[List[int]] = field(default_factory=list)
    width: int = 0
    height: int = 0
    gold: Set[Point] = field(default_factory=set)
    bases: Dict[str, Point] = field(default_factory=dict)
    visited_red: Set[Point] = field(default_factory=set)
    visited_blue: Set[Point] = field(default_factory=set)
    agents: Dict[str, Point] = field(default_factory=dict)
    team_gold: Dict[str, int] = field(default_factory=lambda: {"RED": 0, "BLUE": 0})
    team_finished: Dict[str, Optional[int]] = field(default_factory=lambda: {"RED": None, "BLUE": None})

    def reset(self):
        self.visited_red.clear()
        self.visited_blue.clear()
        self.agents.clear()
        self.team_gold = {"RED": 0, "BLUE": 0}
        self.team_finished = {"RED": None, "BLUE": None}


class LogParser:
    def __init__(self, path: str):
        self.path = path

    def parse(self) -> List[Event]:
        events = []
        with open(self.path, "r", encoding="utf-8", errors="ignore") as f:
            for line in f:
                m = WORLD_RE.search(line)
                if m:
                    matrix = ast.literal_eval(m.group(1))
                    events.append(Event("world", {"matrix": matrix}))
                    continue
                m = BASE_RE.search(line)
                if m:
                    team, xs, ys = m.groups()
                    events.append(Event("base", {"team": team.upper(), "pos": (int(xs), int(ys))}))
                    continue
                idm = ID_PREFIX_RE.search(line)
                mm = MOVE_RE.search(line)
                if idm and mm:
                    agent_id = idm.group(1)
                    gx, gy, *_ = mm.groups()
                    events.append(Event("move", {"agent_id": agent_id, "pos": (int(gx), int(gy))}))
                    continue
                m = GOLD_COLLECT_RE.search(line)
                if m:
                    xs, ys = m.groups()
                    events.append(Event("collect", {"pos": (int(xs), int(ys))}))
                    continue
                m = FINISH_RE.search(line)
                if m:
                    team, amount = m.groups()
                    events.append(Event("finish", {"team": team.upper(), "amount": int(amount)}))
        return events


# --- Kolory i rozmiary ---
CELL = 44
GRID_MARGIN = 2
COLOR_WHITE = "#ffffff"
COLOR_BLACK = "#000000"
COLOR_GOLD = "#f2c94c"
COLOR_RED = "#ef4444"
COLOR_BLUE = "#3b82f6"
COLOR_BASE = "#22c55e"


class ScrollableCanvas(ttk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent)
        self.canvas = tk.Canvas(self, bg=COLOR_WHITE, highlightthickness=0, **kwargs)
        self.hbar = ttk.Scrollbar(self, orient="horizontal", command=self.canvas.xview)
        self.vbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(xscrollcommand=self.hbar.set, yscrollcommand=self.vbar.set)
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.vbar.grid(row=0, column=1, sticky="ns")
        self.hbar.grid(row=1, column=0, sticky="ew")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

    def set_scrollregion(self, w, h):
        self.canvas.config(scrollregion=(0, 0, w, h))

    def clear(self):
        self.canvas.delete("all")


class ViewerApp:
    def __init__(self, root, initial_log=None):
        self.root = root
        self.root.title("Agentar Log Viewer v2")
        self.state = WorldState()
        self.events: List[Event] = []
        self.step_index = 0
        self.playing = False
        self.delay_ms = 200

        self._build_ui()
        if initial_log and os.path.exists(initial_log):
            self.load_log(initial_log)

    def _build_ui(self):
        self.root.configure(bg=COLOR_WHITE)
        topbar = ttk.Frame(self.root)
        topbar.pack(side="top", fill="x", padx=8, pady=6)

        ttk.Button(topbar, text="Wybierz plik logów…", command=self.on_open).pack(side="left", padx=5)
        self.btn_play = ttk.Button(topbar, text="▶︎ Start", command=self.toggle_play)
        self.btn_play.pack(side="left", padx=5)
        ttk.Button(topbar, text="Krok ▶︎", command=self.step_once).pack(side="left", padx=5)
        ttk.Button(topbar, text="⟲ Reset", command=self.reset_state).pack(side="left", padx=5)

        ttk.Label(topbar, text="Prędkość:").pack(side="left", padx=(30, 5))
        self.s_speed = ttk.Scale(topbar, from_=600, to=10, command=lambda e: self.update_speed())
        self.s_speed.set(self.delay_ms)
        self.s_speed.pack(side="left", fill="x", expand=True, padx=5)

        right = ttk.Frame(self.root)
        right.pack(side="right", fill="y", padx=8, pady=6)
        self.lbl_file = ttk.Label(right, text="Brak pliku", wraplength=200)
        self.lbl_file.pack(anchor="w", pady=4)

        self.red_var = tk.StringVar(value="RED: 0")
        self.blue_var = tk.StringVar(value="BLUE: 0")
        ttk.Label(right, textvariable=self.red_var, foreground=COLOR_RED).pack(anchor="w", pady=2)
        ttk.Label(right, textvariable=self.blue_var, foreground=COLOR_BLUE).pack(anchor="w", pady=2)

        self.sc = ScrollableCanvas(self.root, width=900, height=700)
        self.sc.pack(fill="both", expand=True, padx=8, pady=8)

    # --- Kontrolki ---
    def on_open(self):
        path = filedialog.askopenfilename(filetypes=[("Log files", "*.log *.txt"), ("All", "*.*")])
        if path:
            self.load_log(path)

    def toggle_play(self):
        if not self.events:
            messagebox.showinfo("Brak danych", "Wczytaj plik logów.")
            return
        self.playing = not self.playing
        self.btn_play.config(text="⏸ Pauza" if self.playing else "▶︎ Start")
        if self.playing:
            self._tick()

    def step_once(self):
        if self.step_index < len(self.events):
            self.apply_event(self.events[self.step_index])
            self.step_index += 1
            self.draw()

    def reset_state(self):
        self.playing = False
        self.btn_play.config(text="▶︎ Start")
        self.step_index = 0
        self.state.reset()
        self.draw()

    def update_speed(self):
        self.delay_ms = int(float(self.s_speed.get()))

    # --- Symulacja ---
    def _tick(self):
        if not self.playing:
            return
        if self.step_index < len(self.events):
            self.apply_event(self.events[self.step_index])
            self.step_index += 1
            self.draw()
            self.root.after(self.delay_ms, self._tick)
        else:
            self.playing = False
            self.btn_play.config(text="▶︎ Start")

    # --- Logika zdarzeń ---
    def load_log(self, path):
        self.lbl_file.config(text=os.path.basename(path))
        parser = LogParser(path)
        self.events = parser.parse()
        self.reset_state()
        for e in self.events:
            if e.kind == "world":
                self.state.grid = e.payload["matrix"]
                self.state.height = len(self.state.grid)
                self.state.width = len(self.state.grid[0])
                self.state.gold = {(x, y) for y, row in enumerate(self.state.grid) for x, v in enumerate(row) if v == 1}
                break
        self.draw()

    def apply_event(self, ev: Event):
        s = self.state
        if ev.kind == "base":
            s.bases[ev.payload["team"]] = ev.payload["pos"]
        elif ev.kind == "move":
            a = ev.payload["agent_id"]
            s.agents[a] = ev.payload["pos"]
            team = team_from_agent_id(a)
            if team == "RED":
                s.visited_red.add(ev.payload["pos"])
            elif team == "BLUE":
                s.visited_blue.add(ev.payload["pos"])
        elif ev.kind == "collect":
            x, y = ev.payload["pos"]
            if (x, y) in s.gold:
                s.gold.remove((x, y))
            # przypisz złoto drużynie której agent jest najbliżej
            min_team, min_dist = None, 999
            for a, pos in s.agents.items():
                dist = abs(pos[0]-x)+abs(pos[1]-y)
                if dist < min_dist:
                    min_dist = dist
                    min_team = team_from_agent_id(a)
            if min_team:
                s.team_gold[min_team] += 1
        elif ev.kind == "finish":
            s.team_finished[ev.payload["team"]] = ev.payload["amount"]

    # --- Rysowanie ---
    def draw(self):
        cv = self.sc.canvas
        cv.delete("all")
        s = self.state
        if not s.grid:
            return

        W, H = s.width * CELL, s.height * CELL
        self.sc.set_scrollregion(W, H)

        for y in range(s.height):
            for x in range(s.width):
                x0, y0 = x * CELL, y * CELL
                fill = COLOR_WHITE if s.grid[y][x] >= 0 else COLOR_BLACK
                cv.create_rectangle(x0, y0, x0 + CELL, y0 + CELL, fill=fill, outline="#ccc")
        # złoto
        for (x, y) in s.gold:
            cv.create_text(x * CELL + CELL / 2, y * CELL + CELL / 2, text="G", fill=COLOR_GOLD, font=("Arial", 14, "bold"))
        # bazy
        for team, (x, y) in s.bases.items():
            color = COLOR_RED if team == "RED" else COLOR_BLUE
            cv.create_rectangle(x * CELL + 3, y * CELL + 3, x * CELL + CELL - 3, y * CELL + CELL - 3,
                                outline=COLOR_BASE, width=3)
            cv.create_text(x * CELL + CELL/2, y * CELL + CELL/2, text=team[0], fill=color, font=("Arial", 10, "bold"))
        # odwiedziny
        for (x, y) in s.visited_red:
            cv.create_polygon(x * CELL + CELL - 4, y * CELL + CELL - 4,
                              x * CELL + CELL - 4, y * CELL + CELL - 14,
                              x * CELL + CELL - 14, y * CELL + CELL - 4,
                              fill=COLOR_RED, outline="")
        for (x, y) in s.visited_blue:
            cv.create_polygon(x * CELL + 4, y * CELL + 4,
                              x * CELL + 14, y * CELL + 4,
                              x * CELL + 4, y * CELL + 14,
                              fill=COLOR_BLUE, outline="")
        # agenci
        for aid, (x, y) in s.agents.items():
            color = COLOR_RED if team_from_agent_id(aid) == "RED" else COLOR_BLUE
            cv.create_text(x * CELL + CELL / 2, y * CELL + CELL / 2,
                           text=last_digit_from_id(aid), fill=color, font=("Arial", 16, "bold"))

        # aktualny stan złota
        self.red_var.set(f"RED: {s.team_gold['RED']}")
        self.blue_var.set(f"BLUE: {s.team_gold['BLUE']}")


def main():
    root = tk.Tk()
    root.geometry("1200x800+100+50")
    init = "/mnt/data/agentar.log" if os.path.exists("/mnt/data/agentar.log") else None
    ViewerApp(root, init)
    root.mainloop()


if __name__ == "__main__":
    main()
