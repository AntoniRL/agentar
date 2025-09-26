#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Agentar Log GUI Viewer
Wizualizacja planszy WORLD i ruchów agentów na podstawie pliku agentar.log
"""

import sys
import os
import re
import time
import threading
from dataclasses import dataclass, field
from typing import Dict, List, Tuple, Optional

try:
    import tkinter as tk
    from tkinter import ttk, messagebox, filedialog
except Exception:
    print("Tkinter jest wymagany do uruchomienia aplikacji")
    raise

# -----------------------------
# Regex i kolory
# -----------------------------

WORLD_RE = re.compile(r'WORLD::\s*\[\[.*?\]\]', re.DOTALL)

AGENT_POS_RE = re.compile(
    r'INFO:\s*([.\d]+)\S*::\s*\(PRINTING\)\s*([A-Z]+)\s*POS+S?ITION::\s*\((\d+),\s*(\d+)\)',
    re.IGNORECASE
)
AGENT_TEAM_RE = re.compile(
    r'INFO:\s*([.\d]+)\S*::\s*\(PRINTING\)\s*MY TEAM:::\s*([A-Z]+)',
    re.IGNORECASE
)
START_POS_RE = re.compile(
    r'INFO:\s*([.\d]+)\S*::\s*\(PRINTING\)\s*([A-Z]+)\s*start position::\s*\((\d+),\s*(\d+)\)',
    re.IGNORECASE
)

COLOR_MAP = {
    'GREEN': '#28a745',
    'BLUE': '#007bff',
    'RED': '#dc3545',
    'YELLOW': '#ffc107',
    'PURPLE': '#6f42c1',
    'ORANGE': '#fd7e14',
    'CYAN': '#17a2b8',
    'PINK': '#e83e8c',
    'GRAY': '#6c757d'
}

def parse_world(text: str) -> Optional[List[List[int]]]:
    m = WORLD_RE.search(text)
    if not m:
        return None
    blob = m.group(0)
    arr_txt = blob.split('WORLD::', 1)[-1].strip()
    try:
        import ast
        grid = ast.literal_eval(arr_txt)
        return grid
    except Exception:
        return None

@dataclass
class AgentEvent:
    t: float
    agent_id: str
    team: str
    x: int
    y: int

@dataclass
class LogModel:
    world: Optional[List[List[int]]] = None
    events: List[AgentEvent] = field(default_factory=list)
    agent_teams: Dict[str, str] = field(default_factory=dict)
    master_team: Optional[str] = None
    # (x,y) -> team name (dla podświetlenia pól startowych)
    start_cells: Dict[Tuple[int,int], str] = field(default_factory=dict)

def parse_log(path: str) -> LogModel:
    model = LogModel()
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()

    model.world = parse_world(text)

    # Teamy
    for m in AGENT_TEAM_RE.finditer(text):
        agent_id, team = m.group(1), m.group(2).upper()
        model.agent_teams[agent_id] = team
        if agent_id.startswith('.1.1'):
            model.master_team = team

    # Pozycje startowe
    for m in START_POS_RE.finditer(text):
        _agent_id = m.group(1)
        team = m.group(2).upper()
        x = int(m.group(3)); y = int(m.group(4))
        model.start_cells[(x, y)] = team

    # Ruchy
    for m in AGENT_POS_RE.finditer(text):
        agent_id = m.group(1)
        team = m.group(2).upper()
        x = int(m.group(3))
        y = int(m.group(4))
        model.events.append(
            AgentEvent(t=len(model.events), agent_id=agent_id, team=team, x=x, y=y)
        )

    return model

# -----------------------------
# GUI
# -----------------------------

def darken(hex_color: str, factor: float = 0.6) -> str:
    hex_color = hex_color.lstrip('#')
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    r = int(r * factor)
    g = int(g * factor)
    b = int(b * factor)
    return f'#{r:02x}{g:02x}{b:02x}'

def _last_number(s: str):
    m = re.search(r'(\d+)(?!.*\d)', s)
    return int(m.group(1)) if m else None

class WorldCanvas(tk.Canvas):
    def __init__(self, master, cell_size: int = 32, **kwargs):
        super().__init__(master, **kwargs)
        self.cell_size = cell_size
        self.grid_data: Optional[List[List[int]]] = None
        self.visited_by_team: Dict[Tuple[int,int], str] = {}
        self.agent_positions: Dict[str, Tuple[int,int,str]] = {}
        self.agent_indices: Dict[str, int] = {}
        self.next_index: int = 1
        self.team_color_name = None
        self.start_cells: Dict[Tuple[int,int], str] = {}

    def set_world(self, grid: List[List[int]]):
        self.grid_data = grid
        h = len(grid)
        w = len(grid[0]) if h else 0
        self.config(width=w*self.cell_size, height=h*self.cell_size)
        self.redraw()

    def set_team_name(self, team_name: str):
        self.team_color_name = team_name

    def set_start_cells(self, start_cells: Dict[Tuple[int,int], str]):
        self.start_cells = dict(start_cells)
        self.redraw()

    def mark_visited_by_team(self, x: int, y: int, team: str):
        # Kolorujemy odwiedziny tylko dla master teamu .1.1 (zgodnie z wymaganiem)
        if self.team_color_name and team.upper() == self.team_color_name.upper():
            self.visited_by_team[(x,y)] = team
        self.redraw_cell(x,y)

    def update_agent(self, agent_id: str, x: int, y: int, team: str):
        self.agent_positions[agent_id] = (x,y,team)
        # nadaj/utrwal numer agenta
        num = _last_number(agent_id)
        if num is not None and 1 <= num <= 9:
            self.agent_indices.setdefault(agent_id, num)
        else:
            if agent_id not in self.agent_indices and self.next_index <= 4:
                self.agent_indices[agent_id] = self.next_index
                self.next_index += 1
        # zaznacz odwiedzone pole przez team .1.1
        self.mark_visited_by_team(x,y,team)
        self.redraw()

    def redraw(self):
        self.delete('all')
        if not self.grid_data:
            return
        rows = len(self.grid_data)
        cols = len(self.grid_data[0])
        for y in range(rows):
            for x in range(cols):
                self.redraw_cell(x,y)
        for agent_id, (ax, ay, team) in self.agent_positions.items():
            self.draw_agent(ax, ay, team, agent_id)

    def redraw_cell(self, x:int, y:int):
        if not self.grid_data: return
        val = self.grid_data[y][x]
        cs = self.cell_size
        x0, y0 = x*cs, y*cs
        x1, y1 = x0+cs, y0+cs

        # 1) tło podstawowe wg WORLD (-1 czarne, 0/pos białe)
        if val == -1:
            base_fill = '#000000'
        else:
            base_fill = '#ffffff'

        # 2) jeżeli to pole startowe któregoś teamu – nadpisz tło ciemnym odcieniem koloru teamu
        if (x, y) in self.start_cells:
            team = self.start_cells[(x, y)].upper()
            base_fill = darken(COLOR_MAP.get(team, '#28a745'), 0.55)

        self.create_rectangle(x0, y0, x1, y1, fill=base_fill, outline='#cccccc')

        # 3) jeśli >0 – żółta cyfra na środku
        if val > 0:
            self.create_text((x0+x1)//2, (y0+y1)//2, text=str(val),
                             fill='#d4aa00', font=('Helvetica','12','bold'))

        # 4) jeżeli odwiedzone przez .1.1 – malujemy górny-lewy trójkąt kolorem teamu
        if (x,y) in self.visited_by_team:
            team = self.visited_by_team[(x,y)]
            color = COLOR_MAP.get(team.upper(), '#28a745')
            self.create_polygon(x0, y0, x1, y0, x0, y1, fill=color, outline='')

    def draw_agent(self, x:int, y:int, team:str, agent_id:str=None):
        cs = self.cell_size
        x0, y0 = x*cs, y*cs
        x1, y1 = x0+cs, y0+cs
        color = COLOR_MAP.get(team.upper(), '#28a745')
        shade = darken(color, 0.55)
        # cyfra agenta (z id albo przydzielona 1..4)
        label = str(self.agent_indices.get(agent_id, 'S'))
        self.create_text((x0+x1)//2, (y0+y1)//2, text=label,
                         fill=shade, font=('Helvetica','16','bold'))

# -----------------------------
# Kontroler
# -----------------------------

class Controller:
    def __init__(self, root: tk.Tk, log_path: str):
        self.root = root
        self.root.title("Agentar GUI Viewer")
        self.log_path = log_path
        self.model = LogModel()
        self.play_index = 0
        self.play_speed = 1.0
        self.playing = False
        self.follow_live = tk.BooleanVar(value=False)
        self.tail_thread: Optional[threading.Thread] = None
        self.tail_stop = threading.Event()

        self.canvas = WorldCanvas(root, cell_size=30, bg='#f0f0f0', highlightthickness=0)
        self.canvas.grid(row=0, column=0, columnspan=6, padx=10, pady=10)

        ttk.Button(root, text='Otwórz log…', command=self.open_file).grid(row=1, column=0, sticky='ew', padx=5, pady=5)
        self.play_btn = ttk.Button(root, text='Start', command=self.toggle_play)
        self.play_btn.grid(row=1, column=1, sticky='ew', padx=5, pady=5)
        ttk.Button(root, text='⏮︎ Początek', command=self.restart).grid(row=1, column=2, sticky='ew', padx=5, pady=5)

        ttk.Label(root, text='Szybkość').grid(row=1, column=3, sticky='e', padx=5)
        self.speed = tk.DoubleVar(value=1.0)
        self.speed_scale = ttk.Scale(root, from_=0.1, to=10.0, variable=self.speed, command=self.on_speed, orient='horizontal')
        self.speed_scale.grid(row=1, column=4, sticky='ew', padx=5, pady=5)

        self.follow_chk = ttk.Checkbutton(root, text='Śledź na żywo (tail)', variable=self.follow_live, command=self.on_follow_toggle)
        self.follow_chk.grid(row=1, column=5, sticky='w', padx=5, pady=5)

        root.grid_columnconfigure(4, weight=1)
        root.grid_rowconfigure(0, weight=1)

        self.load_log(self.log_path)

    def on_speed(self, _evt=None):
        self.play_speed = self.speed.get()

    def open_file(self):
        path = filedialog.askopenfilename(filetypes=[('Log files','*.log *.txt'), ('All files','*.*')])
        if path:
            self.stop_tail()
            self.load_log(path)

    def load_log(self, path: str):
        try:
            self.model = parse_log(path)
            self.log_path = path
        except FileNotFoundError:
            messagebox.showerror("Błąd", f"Nie znaleziono pliku: {path}")
            return

        if not self.model.world:
            messagebox.showwarning("Uwaga", "Nie znaleziono WORLD w logu.")
        else:
            self.canvas.set_world(self.model.world)

        if self.model.master_team:
            self.canvas.set_team_name(self.model.master_team)

        # przekaż pola startowe do canvasa
        self.canvas.set_start_cells(self.model.start_cells)

        self.play_index = 0
        self.canvas.agent_positions.clear()
        self.canvas.visited_by_team.clear()
        self.canvas.redraw()

    def toggle_play(self):
        self.playing = not self.playing
        self.play_btn.config(text='Pauza' if self.playing else 'Start')
        if self.playing:
            self.root.after(0, self.play_step)

    def restart(self):
        self.playing = False
        self.play_btn.config(text='Start')
        self.play_index = 0
        self.canvas.agent_positions.clear()
        self.canvas.visited_by_team.clear()
        self.canvas.redraw()

    def play_step(self):
        if not self.playing:
            return
        if self.play_index < len(self.model.events):
            ev = self.model.events[self.play_index]
            self.canvas.update_agent(ev.agent_id, ev.x, ev.y, ev.team)
            self.play_index += 1
            delay = int(1000 / max(0.1, self.play_speed))
            self.root.after(delay, self.play_step)
        else:
            if self.follow_live.get():
                self.root.after(500, self.play_step)
            else:
                self.playing = False
                self.play_btn.config(text='Start')

    def on_follow_toggle(self):
        if self.follow_live.get():
            self.start_tail()
        else:
            self.stop_tail()

    def start_tail(self):
        self.stop_tail()
        self.tail_stop.clear()
        self.tail_thread = threading.Thread(target=self.tail_loop, daemon=True)
        self.tail_thread.start()

    def stop_tail(self):
        if self.tail_thread and self.tail_thread.is_alive():
            self.tail_stop.set()
            self.tail_thread.join(timeout=1.0)
        self.tail_thread = None
        self.tail_stop.clear()

    def tail_loop(self):
        try:
            with open(self.log_path, 'r', encoding='utf-8', errors='ignore') as f:
                f.seek(0, os.SEEK_END)
                while not self.tail_stop.is_set():
                    where = f.tell()
                    line = f.readline()
                    if not line:
                        time.sleep(0.2)
                        f.seek(where)
                        continue

                    # przechwyć deklaracje teamów (dla .1.1)
                    mteam = AGENT_TEAM_RE.search(line)
                    if mteam:
                        agent_id, team = mteam.group(1), mteam.group(2).upper()
                        self.model.agent_teams[agent_id] = team
                        if agent_id.startswith('.1.1'):
                            self.model.master_team = team
                            self.canvas.set_team_name(team)

                    # przechwyć pozycję startową
                    mstart = START_POS_RE.search(line)
                    if mstart:
                        _agent_id = mstart.group(1)
                        team = mstart.group(2).upper()
                        x = int(mstart.group(3)); y = int(mstart.group(4))
                        self.model.start_cells[(x, y)] = team
                        def upd_start():
                            self.canvas.set_start_cells(self.model.start_cells)
                        self.root.after(0, upd_start)

                    # przechwyć kolejne pozycje
                    m = AGENT_POS_RE.search(line)
                    if m:
                        agent_id = m.group(1)
                        team = m.group(2).upper()
                        x = int(m.group(3)); y = int(m.group(4))
                        ev = AgentEvent(t=time.time(), agent_id=agent_id, team=team, x=x, y=y)
                        self.model.events.append(ev)
                        def do_update():
                            self.canvas.update_agent(agent_id, x, y, team)
                        self.root.after(0, do_update)

        except Exception as e:
            def show_err():
                messagebox.showerror("Tail błąd", str(e))
            self.root.after(0, show_err)

# -----------------------------
# main
# -----------------------------

def main():
    if len(sys.argv) > 1:
        log_path = sys.argv[1]
    else:
        log_path = os.path.join(os.getcwd(), 'agentar.log')
    root = tk.Tk()
    style = ttk.Style(root)
    try:
        style.theme_use('clam')
    except Exception:
        pass
    Controller(root, log_path)
    root.mainloop()

if __name__ == '__main__':
    main()
