#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Agentar Dashboard GUI — tylko agenci .1.1.1 .. .1.1.4 + zsynchronizowane mini-mapki
Zmiany:
- Filtr agentów: renderujemy i śledzimy WYŁĄCZNIE .1.1.1, .1.1.2, .1.1.3, .1.1.4
- Jednolita orientacja mini-map: oś Y w dół (zgodnie z główną planszą)
"""

import sys
import os
import re
import time
import threading
from dataclasses import dataclass, field
from typing import Dict, List, Tuple, Optional, Set, Literal

try:
    import tkinter as tk
    from tkinter import ttk, messagebox, filedialog
except Exception:
    print("Tkinter jest wymagany do uruchomienia aplikacji")
    raise

# --------- KONFIG ---------
ALLOWED_AGENTS = {".1.1.1", ".1.1.2", ".1.1.3", ".1.1.4"}
# Jeżeli chcesz, żeby oś Y mini-map była w górę (geometryczna), ustaw na False:
RELATIVE_Y_DOWN = True

# --------- REGEX ---------
WORLD_RE = re.compile(r'WORLD::\s*\[\[.*?\]\]', re.DOTALL)

POS_RE = re.compile(
    r'INFO:\s*([.\d]+)\S*::\s*\(PRINTING\)\s*POS+S?ITION::\s*(?:\((\d+)\s*,\s*(\d+)\)|(\d+)\s+(\d+))',
    re.IGNORECASE
)

TEAM_RE = re.compile(
    r'INFO:\s*([.\d]+)\S*::\s*\(PRINTING\)\s*MY TEAM:::\s*([A-Z]+)',
    re.IGNORECASE
)

START_RE = re.compile(
    r'INFO:\s*([.\d]+)\S*::\s*\(PRINTING\)\s*([A-Z]+)\s*start position::\s*\((\d+),\s*(\d+)\)',
    re.IGNORECASE
)

DICT_RE = re.compile(r'\(LOGGING\)\s*(FRONTIERS|VISITED)::\s*\{([^}]*)\}', re.IGNORECASE)
PAIR_RE = re.compile(r'\(\s*(-?\d+)\s*,\s*(-?\d+)\s*\)')

# --------- KOLORY ---------
COLOR_MAP = {
    'GREEN': '#28a745',
    'BLUE':  '#007bff',
    'RED':   '#dc3545',
    'YELLOW':'#ffc107',
    'PURPLE':'#6f42c1',
    'ORANGE':'#fd7e14',
    'CYAN':  '#17a2b8',
    'PINK':  '#e83e8c',
    'GRAY':  '#6c757d'
}

def lighten(hex_color: str, factor: float = 1.35) -> str:
    c = hex_color.lstrip('#')
    r = min(int(int(c[0:2], 16)*factor), 255)
    g = min(int(int(c[2:4], 16)*factor), 255)
    b = min(int(int(c[4:6], 16)*factor), 255)
    return f'#{r:02x}{g:02x}{b:02x}'

def darken(hex_color: str, factor: float = 0.6) -> str:
    c = hex_color.lstrip('#')
    r = int(int(c[0:2], 16)*factor)
    g = int(int(c[2:4], 16)*factor)
    b = int(int(c[4:6], 16)*factor)
    return f'#{r:02x}{g:02x}{b:02x}'

def last_number(s: str) -> Optional[int]:
    m = re.search(r'(\d+)(?!.*\d)', s)
    return int(m.group(1)) if m else None

# --------- MODELE ---------
EventType = Literal['team', 'start', 'pos', 'visited', 'frontiers']

@dataclass
class Event:
    t: float
    type: EventType
    agent_id: Optional[str] = None
    team: Optional[str] = None
    x: Optional[int] = None
    y: Optional[int] = None
    coords: Optional[Set[Tuple[int,int]]] = None  # dla visited/frontiers

@dataclass
class AgentState:
    team: str = 'GREEN'
    pos: Tuple[int,int] = (0,0)
    visited_rel: Set[Tuple[int,int]] = field(default_factory=set)
    frontiers_rel: Set[Tuple[int,int]] = field(default_factory=set)

@dataclass
class LogModel:
    world: Optional[List[List[int]]] = None
    events: List[Event] = field(default_factory=list)
    master_team: Optional[str] = None
    start_cells: Dict[Tuple[int,int], str] = field(default_factory=dict)
    agents: Dict[str, AgentState] = field(default_factory=dict)

# --------- PARSERY ---------
def parse_world(text: str) -> Optional[List[List[int]]]:
    m = WORLD_RE.search(text)
    if not m: return None
    arr_txt = m.group(0).split('WORLD::', 1)[-1].strip()
    try:
        import ast
        grid = ast.literal_eval(arr_txt)
        return grid
    except Exception:
        return None

def parse_frontiers_visited(line: str) -> Tuple[Optional[str], Set[Tuple[int,int]]]:
    m = DICT_RE.search(line)
    if not m:
        return None, set()
    kind = m.group(1).lower()  # 'frontiers' lub 'visited'
    body = m.group(2)
    coords: Set[Tuple[int,int]] = set()
    for a,b in PAIR_RE.findall(body):
        x, y = int(a), int(b)
        if not RELATIVE_Y_DOWN:
            y = -y  # jeśli oś Y ma być w górę
        coords.add((x, y))
    return kind, coords

def parse_log(path: str) -> LogModel:
    model = LogModel()
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()
    text = ''.join(lines)

    model.world = parse_world(text)

    # zdarzenia w kolejności linii
    for line in lines:
        # TEAM
        m = TEAM_RE.search(line)
        if m:
            aid, team = m.group(1), m.group(2).upper()
            # Team może dotyczyć .1.1 – zachowujemy, bo definiuje master_team dla odwiedzin
            model.events.append(Event(t=len(model.events), type='team', agent_id=aid, team=team))
            if aid.startswith('.1.1'):
                model.master_team = team
            continue

        # START
        m = START_RE.search(line)
        if m:
            aid, team = m.group(1), m.group(2).upper()
            sx, sy = int(m.group(3)), int(m.group(4))
            model.events.append(Event(t=len(model.events), type='start', agent_id=aid, team=team, x=sx, y=sy))
            continue

        # VISITED / FRONTIERS
        if '(LOGGING)' in line and ('VISITED' in line or 'FRONTIERS' in line):
            m_aid = re.search(r'INFO:\s*([.\d]+)\S*::', line)
            if m_aid:
                aid = m_aid.group(1)
                if aid in ALLOWED_AGENTS:  # tylko agenci .1.1.1..4
                    kind, coords = parse_frontiers_visited(line)
                    if kind == 'visited':
                        model.events.append(Event(t=len(model.events), type='visited', agent_id=aid, coords=set(coords)))
                    elif kind == 'frontiers':
                        model.events.append(Event(t=len(model.events), type='frontiers', agent_id=aid, coords=set(coords)))
            continue

        # POS
        m = POS_RE.search(line)
        if m:
            aid = m.group(1)
            if aid not in ALLOWED_AGENTS:
                continue  # ignoruj niechcianych agentów
            if m.group(2) and m.group(3):
                x, y = int(m.group(2)), int(m.group(3))
            else:
                x, y = int(m.group(4)), int(m.group(5))
            model.events.append(Event(t=len(model.events), type='pos', agent_id=aid, x=x, y=y))
            continue

    return model

# --------- KOMPONENTY RYSUJĄCE ---------
class WorldCanvas(tk.Canvas):
    def __init__(self, master, cell_size: int = 30, **kwargs):
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
        if self.team_color_name and team and team.upper() == self.team_color_name.upper():
            self.visited_by_team[(x,y)] = team
        self.redraw_cell(x,y)

    def update_agent(self, agent_id: str, x: int, y: int, team: str):
        self.agent_positions[agent_id] = (x,y,team)
        num = last_number(agent_id)
        if num is not None and 1 <= num <= 9:
            self.agent_indices.setdefault(agent_id, num)
        else:
            if agent_id not in self.agent_indices and self.next_index <= 4:
                self.agent_indices[agent_id] = self.next_index
                self.next_index += 1
        self.mark_visited_by_team(x,y,team)
        self.redraw()

    def redraw(self):
        self.delete('all')
        if not self.grid_data: return
        rows = len(self.grid_data); cols = len(self.grid_data[0])
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

        base_fill = '#000000' if val == -1 else '#ffffff'
        if (x,y) in self.start_cells:
            team = self.start_cells[(x,y)].upper()
            base_fill = COLOR_MAP.get(team, '#28a745')

        self.create_rectangle(x0,y0,x1,y1, fill=base_fill, outline='#cccccc')

        if val > 0:
            self.create_text((x0+x1)//2,(y0+y1)//2, text=str(val),
                             fill='#d4aa00', font=('Helvetica','12','bold'))

        if (x,y) in self.visited_by_team:
            team = self.visited_by_team[(x,y)].upper()
            base = COLOR_MAP.get(team, '#28a745')
            light = lighten(base, 1.35)
            self.create_polygon(x0,y0, x1,y0, x0,y1, fill=light, outline='')

    def draw_agent(self, x:int, y:int, team:str, agent_id:str):
        cs = self.cell_size
        x0,y0 = x*cs, y*cs
        x1,y1 = x0+cs, y0+cs
        base = COLOR_MAP.get(team.upper(), '#28a745')
        label = str(self.agent_indices.get(agent_id, last_number(agent_id) or 1))
        self.create_text((x0+x1)//2,(y0+y1)//2, text=label,
                         fill=base, font=('Helvetica','16','bold'))

class AgentMiniMap(tk.Canvas):
    """
    Mini-mapa relatywna jednego agenta:
    - wspólna orientacja we wszystkich mini-mapach (RELATIVE_Y_DOWN)
    - VISITED: wypełnienie jasnym kolorem teamu
    - FRONTIERS: obramowanie kolorem teamu
    """
    def __init__(self, master, cell: int = 18, **kwargs):
        super().__init__(master, **kwargs)
        self.cell = cell
        self.padding = 8
        self.team = 'GREEN'
        self.label = ''
        self.visited: Set[Tuple[int,int]] = set()
        self.frontiers: Set[Tuple[int,int]] = set()

    def set_label(self, text: str):
        self.label = text
        self.redraw()

    def set_team(self, team: str):
        self.team = team
        self.redraw()

    def apply_visited(self, coords: Set[Tuple[int,int]]):
        self.visited = set(coords)
        self.redraw()

    def apply_frontiers(self, coords: Set[Tuple[int,int]]):
        self.frontiers = set(coords)
        self.redraw()

    def clear(self):
        self.visited.clear()
        self.frontiers.clear()
        self.redraw()

    def redraw(self):
        self.delete('all')
        pts = {(0,0)} | self.visited | self.frontiers
        minx = min((x for x,_ in pts), default=0)
        maxx = max((x for x,_ in pts), default=0)
        miny = min((y for _,y in pts), default=0)
        maxy = max((y for _,y in pts), default=0)
        minx -= 1; miny -= 1; maxx += 1; maxy += 1
        width = max(9, maxx - minx + 1)
        height = max(9, maxy - miny + 1)

        cs = self.cell
        W = width*cs + 2*self.padding
        H = height*cs + 2*self.padding
        self.config(width=W, height=H)

        base = COLOR_MAP.get(self.team.upper(), '#28a745')
        light = lighten(base, 1.35)

        def to_pix(rx:int, ry:int) -> Tuple[int,int,int,int]:
            # Wspólna orientacja: jeśli RELATIVE_Y_DOWN True -> rośnie w dół (jak główna mapa)
            cy = ry if RELATIVE_Y_DOWN else -ry
            cx = rx
            px = self.padding + (cx - minx)*cs
            py = self.padding + (cy - miny)*cs
            return px, py, px+cs, py+cs

        # siatka
        self.create_rectangle(0,0,W,H, fill='#ffffff', outline='')
        for i in range(width+1):
            x = self.padding + i*cs
            self.create_line(x, self.padding, x, self.padding+height*cs, fill='#dddddd')
        for j in range(height+1):
            y = self.padding + j*cs
            self.create_line(self.padding, y, self.padding+width*cs, y, fill='#dddddd')

        # VISITED
        for (rx,ry) in self.visited:
            x0,y0,x1,y1 = to_pix(rx,ry)
            self.create_rectangle(x0,y0,x1,y1, fill=light, outline='')

        # FRONTIERS
        for (rx,ry) in self.frontiers:
            x0,y0,x1,y1 = to_pix(rx,ry)
            self.create_rectangle(x0,y0,x1,y1, outline=base, width=2)

        # (0,0)
        x0,y0,x1,y1 = to_pix(0,0)
        self.create_rectangle(x0,y0,x1,y1, outline=darken(base,0.6), width=2)
        self.create_text((x0+x1)//2, (y0+y1)//2, text='●', fill=base, font=('Helvetica','10','bold'))

        # etykieta
        self.create_text(W//2, self.padding//2, text=self.label, fill='#444444', font=('Helvetica','10','bold'))

# --------- KONTROLER ---------
class Controller:
    def __init__(self, root: tk.Tk, log_path: str):
        self.root = root
        self.root.title("Agentar Dashboard — only .1.1.1..4, unified orientation")
        self.log_path = log_path
        self.model = LogModel()
        self.play_index = 0
        self.play_speed = 1.0
        self.playing = False
        self.follow_live = tk.BooleanVar(value=False)
        self.tail_thread: Optional[threading.Thread] = None
        self.tail_stop = threading.Event()

        main = ttk.Frame(root); main.grid(row=0, column=0, sticky='nsew')
        root.grid_rowconfigure(0, weight=1); root.grid_columnconfigure(0, weight=1)

        self.canvas = WorldCanvas(main, cell_size=30, bg='#f7f7f7', highlightthickness=0)
        self.canvas.grid(row=0, column=0, columnspan=6, padx=10, pady=10, sticky='nsew')
        main.grid_rowconfigure(0, weight=1)
        for c in range(6): main.grid_columnconfigure(c, weight=1)

        # grid_panel = ttk.Frame(main)
        # grid_panel.grid(row=1, column=0, columnspan=6, sticky='nsew', padx=10, pady=(0,10))
        # for r in range(2): grid_panel.grid_rowconfigure(r, weight=1)
        # for c in range(2): grid_panel.grid_columnconfigure(c, weight=1)

        grid_panel = ttk.Frame(main)
        grid_panel.grid(row=1, column=0, columnspan=6, sticky='nsew', padx=10, pady=(0,10))
        grid_panel.grid_rowconfigure(0, weight=1)
        for c in range(len(ALLOWED_AGENTS)):
            grid_panel.grid_columnconfigure(c, weight=1)

        # Kolejność slotów jest z góry ustalona pod .1.1.1..4
        # self.slots = [".1.1.1", ".1.1.2", ".1.1.3", ".1.1.4"]
        # self.mini_maps: Dict[str, AgentMiniMap] = {}
        # self.mini_frames: Dict[str, ttk.LabelFrame] = {}
        # for i, aid in enumerate(self.slots):
        #     lf = ttk.LabelFrame(grid_panel, text=f"Agent {last_number(aid)}  ({aid})")
        #     r, c = divmod(i, 2)
        #     lf.grid(row=r, column=c, padx=6, pady=6, sticky='nsew')
        #     mini = AgentMiniMap(lf, cell=18, bg='#ffffff', highlightthickness=0)
        #     mini.pack(fill='both', expand=True, padx=6, pady=6)
        #     self.mini_frames[aid] = lf
        #     self.mini_maps[aid] = mini
        self.slots = [".1.1.1", ".1.1.2", ".1.1.3", ".1.1.4"]
        self.mini_maps: Dict[str, AgentMiniMap] = {}
        self.mini_frames: Dict[str, ttk.LabelFrame] = {}
        for i, aid in enumerate(self.slots):
            lf = ttk.LabelFrame(grid_panel, text=f"Agent {last_number(aid)}  ({aid})")
            lf.grid(row=0, column=i, padx=6, pady=6, sticky='nsew')
            mini = AgentMiniMap(lf, cell=18, bg='#ffffff', highlightthickness=0)
            mini.pack(fill='both', expand=True, padx=6, pady=6)
            self.mini_frames[aid] = lf
            self.mini_maps[aid] = mini

        controls = ttk.Frame(root); controls.grid(row=1, column=0, sticky='ew', padx=10, pady=6)
        ttk.Button(controls, text='Otwórz log…', command=self.open_file).pack(side='left', padx=4)
        self.play_btn = ttk.Button(controls, text='Start', command=self.toggle_play); self.play_btn.pack(side='left', padx=4)
        ttk.Button(controls, text='⏮︎ Początek', command=self.restart).pack(side='left', padx=4)
        ttk.Label(controls, text='Szybkość').pack(side='left', padx=(12,4))
        self.speed = tk.DoubleVar(value=1.0)
        ttk.Scale(controls, from_=0.1, to=10.0, variable=self.speed,
                  command=lambda e: self.on_speed(), orient='horizontal', length=200).pack(side='left')
        ttk.Checkbutton(controls, text='Śledź na żywo (tail)', variable=self.follow_live,
                        command=self.on_follow_toggle).pack(side='left', padx=12)

        self.load_log(self.log_path)

    # -- utils --
    def on_speed(self): self.play_speed = self.speed.get()

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

        # Czyścimy start/odwiedziny i mini-mapki (będą ustawiane WYŁĄCZNIE zdarzeniami)
        self.canvas.set_start_cells({})
        self.canvas.agent_positions.clear()
        self.canvas.visited_by_team.clear()
        self.canvas.redraw()
        for aid in self.slots:
            self.mini_maps[aid].clear()
            self.mini_maps[aid].set_label(f"Rel (0,0) w {aid}")

        self.play_index = 0

    def toggle_play(self):
        self.playing = not self.playing
        self.play_btn.config(text='Pauza' if self.playing else 'Start')
        if self.playing: self.root.after(0, self.play_step)

    def restart(self):
        self.playing = False
        self.play_btn.config(text='Start')
        self.play_index = 0
        self.canvas.set_start_cells({})
        self.canvas.agent_positions.clear()
        self.canvas.visited_by_team.clear()
        self.canvas.redraw()
        self.model.agents.clear()
        for aid in self.slots:
            self.mini_maps[aid].clear()
            self.mini_maps[aid].set_label(f"Rel (0,0) w {aid}")

    def play_step(self):
        if not self.playing:
            return
        if self.play_index < len(self.model.events):
            ev = self.model.events[self.play_index]
            self.apply_event(ev)
            self.play_index += 1
            delay = int(1000 / max(0.1, self.play_speed))
            self.root.after(delay, self.play_step)
        else:
            if self.follow_live.get():
                self.root.after(400, self.play_step)
            else:
                self.playing = False
                self.play_btn.config(text='Start')

    def apply_event(self, ev: Event):
        et = ev.type
        aid = ev.agent_id

        # TEAM (może dotyczyć .1.1; zapisujemy dla koloru odwiedzin)
        if et == 'team' and aid and ev.team:
            st = self.model.agents.setdefault(aid, AgentState())
            st.team = ev.team.upper()
            if aid.startswith('.1.1'):
                self.model.master_team = st.team
                self.canvas.set_team_name(st.team)
            # jeżeli to allowed agent (1..4) – ustaw kolor jego mini-mapy
            if aid in ALLOWED_AGENTS:
                self.mini_maps[aid].set_team(st.team)

        # START
        elif et == 'start' and ev.team is not None and ev.x is not None and ev.y is not None:
            self.model.start_cells[(ev.x, ev.y)] = ev.team.upper()
            self.canvas.set_start_cells(self.model.start_cells)

        # VISITED / FRONTIERS tylko dla allowed agentów
        elif et == 'visited' and aid in ALLOWED_AGENTS:
            st = self.model.agents.setdefault(aid, AgentState())
            st.visited_rel = set(ev.coords or [])
            self.mini_maps[aid].apply_visited(st.visited_rel)

        elif et == 'frontiers' and aid in ALLOWED_AGENTS:
            st = self.model.agents.setdefault(aid, AgentState())
            st.frontiers_rel = set(ev.coords or [])
            self.mini_maps[aid].apply_frontiers(st.frontiers_rel)

        # POS tylko dla allowed agentów
        elif et == 'pos' and aid in ALLOWED_AGENTS and ev.x is not None and ev.y is not None:
            st = self.model.agents.setdefault(aid, AgentState())
            team = st.team or 'GREEN'
            st.team = (team or 'GREEN').upper()
            st.pos = (ev.x, ev.y)
            self.canvas.update_agent(aid, ev.x, ev.y, st.team)
            self.mini_maps[aid].set_team(st.team)

    # ----- tail -----
    def on_follow_toggle(self):
        if self.follow_live.get(): self.start_tail()
        else: self.stop_tail()

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
                        f.seek(where); continue
                    ev = self.build_event_from_line(line)
                    if ev:
                        self.model.events.append(ev)
                        self.root.after(0, lambda e=ev: self.apply_event(e))
        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror("Tail błąd", str(e)))

    def build_event_from_line(self, line: str) -> Optional[Event]:
        m = TEAM_RE.search(line)
        if m:
            return Event(t=time.time(), type='team', agent_id=m.group(1), team=m.group(2).upper())

        m = START_RE.search(line)
        if m:
            return Event(t=time.time(), type='start', agent_id=m.group(1),
                         team=m.group(2).upper(), x=int(m.group(3)), y=int(m.group(4)))

        if '(LOGGING)' in line and ('VISITED' in line or 'FRONTIERS' in line):
            m_aid = re.search(r'INFO:\s*([.\d]+)\S*::', line)
            if m_aid:
                aid = m_aid.group(1)
                if aid in ALLOWED_AGENTS:
                    kind, coords = parse_frontiers_visited(line)
                    if kind == 'visited':
                        return Event(t=time.time(), type='visited', agent_id=aid, coords=set(coords))
                    elif kind == 'frontiers':
                        return Event(t=time.time(), type='frontiers', agent_id=aid, coords=set(coords))

        m = POS_RE.search(line)
        if m:
            aid = m.group(1)
            if aid not in ALLOWED_AGENTS:
                return None
            if m.group(2) and m.group(3):
                x, y = int(m.group(2)), int(m.group(3))
            else:
                x, y = int(m.group(4)), int(m.group(5))
            return Event(t=time.time(), type='pos', agent_id=aid, x=x, y=y)

        return None

# --------- main ---------
def main():
    if len(sys.argv) > 1:
        log_path = sys.argv[1]
    else:
        log_path = os.path.join(os.getcwd(), 'logs/agentar.log')
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
