import ast
import os
import re
import tkinter as tk
from tkinter import filedialog, messagebox

# =============== Konfiguracja ===============
AGENTS = {
    "1": {"name": "Agent 1 (.1.1.1)", "color": "#14b84a", "light": "#a6e9b7"},
    "2": {"name": "Agent 2 (.1.1.2)", "color": "#1f6fff", "light": "#a8c8ff"},
    "3": {"name": "Agent 3 (.1.1.3)", "color": "#ff7f0e", "light": "#ffd1a6"},
    "4": {"name": "Agent 4 (.1.1.4)", "color": "#f2c200", "light": "#ffeb99"},
}

TOP_CELL = 26     # górna mapa
SUB_CELL = 16     # dolne mapy
MARGIN = 8

SUB_N = 17        # okno widoku dolnych map (nieparzyste)
CENTER = SUB_N // 2
PAN_MARGIN = 1    # margines (w polach) zanim zaczniemy przesuwać

# =============== Wzorce z logów ===============
WORLD_RE  = re.compile(r"WORLD::\s*(\[\[.*\]\])")
START_RE  = re.compile(r"START POSSITION::\s*\((\d+),\s*(\d+)\)")
MOVE_RE   = re.compile(
    r"\.(1\.1\.(\d))::.*GLOBAL POSSITION::\s*(-?\d+)\s+(-?\d+)\s+RELATIV POSSITION::\s*(-?\d+)\s+(-?\d+)"
)
VIS_RE    = re.compile(r"\.(1\.1\.(\d))::.*VISITED::\s*(\{.*\})")
FRONT_RE  = re.compile(r"\.(1\.1\.(\d))::.*FRONTIERS::\s*(\{.*\})")

# =============== Pomocnicze ===============
def parse_dict_of_pairs(s):
    try:
        d = ast.literal_eval(s)
        pts = set()
        for k in d.keys():
            if isinstance(k, tuple) and len(k) == 2:
                pts.add((int(k[0]), int(k[1])))
        return pts
    except Exception:
        return set()
    

# =============== Scrollable Canvas ================
# TODO: changes for sliding window
class ScrollableCanvas(tk.Frame):
    """Ramka z Canvasem + suwakami. Użyta dla górnej planszy."""
    def __init__(self, master, **kwargs):
        super().__init__(master)
        self.vbar = tk.Scrollbar(self, orient="vertical")
        self.hbar = tk.Scrollbar(self, orient="horizontal")
        self.canvas = tk.Canvas(self, bg="white",
                                xscrollcommand=self.hbar.set,
                                yscrollcommand=self.vbar.set, **kwargs)

        self.vbar.config(command=self.canvas.yview)
        self.hbar.config(command=self.canvas.xview)

        # Układ w siatce (prawy i dolny suwak jak w typowych aplikacjach)
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.vbar.grid(row=0, column=1, sticky="ns")
        self.hbar.grid(row=1, column=0, sticky="ew")

        # Rozciąganie canvasa
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Obsługa kółka myszy (pion) i Shift+scroll (poziom)
        self.canvas.bind("<Enter>", self._bind_wheel)
        self.canvas.bind("<Leave>", self._unbind_wheel)

    def set_scrollregion(self, x0, y0, x1, y1):
        self.canvas.config(scrollregion=(x0, y0, x1, y1))

    # --- obsługa kółka myszy na różnych platformach ---
    def _bind_wheel(self, _):
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)      # Windows / macOS (delta)
        self.canvas.bind_all("<Shift-MouseWheel>", self._on_shift_wheel)
        self.canvas.bind_all("<Button-4>", self._on_linux_up)          # Linux
        self.canvas.bind_all("<Button-5>", self._on_linux_down)

    def _unbind_wheel(self, _):
        self.canvas.unbind_all("<MouseWheel>")
        self.canvas.unbind_all("<Shift-MouseWheel>")
        self.canvas.unbind_all("<Button-4>")
        self.canvas.unbind_all("<Button-5>")

    def _on_mousewheel(self, event):
        # macOS daje mniejsze delta, ale yview_scroll liczy „jednostki”
        direction = -1 if event.delta > 0 else 1
        self.canvas.yview_scroll(direction, "units")

    def _on_shift_wheel(self, event):
        direction = -1 if event.delta > 0 else 1
        self.canvas.xview_scroll(direction, "units")

    def _on_linux_up(self, _event):
        self.canvas.yview_scroll(-1, "units")

    def _on_linux_down(self, _event):
        self.canvas.yview_scroll(1, "units")

# =============== Widoki ===============
class AgentView:
    """Dolna plansza pojedynczego agenta (oś Y w dół) z auto-panningiem."""
    DOT_TAG = "agent_pos_dot"

    def __init__(self, root, aid, title, color, light):
        self.aid = aid
        self.color = color
        self.light = light
        self.frame = tk.Frame(root, bd=2, relief="groove")
        tk.Label(self.frame, text=title).pack()
        w = SUB_N * SUB_CELL
        h = SUB_N * SUB_CELL
        self.canvas = tk.Canvas(self.frame, width=w, height=h, bg="white")
        self.canvas.pack(padx=6, pady=6)

        # --- statystyki agenta ---
        # TODO: new
        self.total_white = 0   # App uzupełni po wczytaniu WORLD
        self.steps = 0
        self.stats_var = tk.StringVar(value="Frontiery: 0\nOdkryte: 0/0 (0.0%)\nKroki: 0")
        tk.Label(self.frame, textvariable=self.stats_var, justify="left").pack(pady=(0,6))

        # „okno” widoku (lew. górny narożnik) w ukł. relatywnym agenta:
        self.vx = -CENTER
        self.vy = -CENTER

        # stan wiedzy
        self.known_not_visited = set()
        self.visited_self = set()
        self.frontiers = set()

        # pozycja kropki (ostatnia znana)
        self.pos = (0, 0)
        self.dot_id = None

        self._redraw_all()

    # ---------- pomocnicze ----------
    def _grid(self):
        for i in range(SUB_N + 1):
            p = i * SUB_CELL
            self.canvas.create_line(p, 0, p, SUB_N * SUB_CELL, fill="#ddd")
            self.canvas.create_line(0, p, SUB_N * SUB_CELL, p, fill="#ddd")

    def _cell_bbox(self, rx, ry):
        # mapuje współrzędne relatywne -> piksele w aktualnym oknie; None jeżeli poza oknem
        rx_rel = rx - self.vx
        ry_rel = ry - self.vy  # Y w dół
        if not (0 <= rx_rel < SUB_N and 0 <= ry_rel < SUB_N):
            return None
        x0 = rx_rel * SUB_CELL
        y0 = ry_rel * SUB_CELL
        return x0, y0, x0 + SUB_CELL, y0 + SUB_CELL

    def _draw_start_frame(self):
        bb = self._cell_bbox(0, 0)
        if bb:
            x0, y0, x1, y1 = bb
            self.canvas.create_rectangle(x0+2, y0+2, x1-2, y1-2, outline=self.color, width=3)

    def _raise_dot(self):
        self.canvas.tag_raise(self.DOT_TAG)

    # TODO: new
    def _update_stats_label(self):
        # pole (0,0) traktujemy jako odkryte
        discovered_set = set(self.known_not_visited) | set(self.visited_self) | {(0, 0)}
        discovered = len(discovered_set)
        total = max(1, int(self.total_white))  # unikamy dzielenia przez zero
        pct = (discovered / total) * 100.0
        front = len(self.frontiers)
        self.stats_var.set(f"Frontiery: {front}\nOdkryte: {discovered}/{total} ({pct:.1f}%)\nKroki: {self.steps}")

    # ---------- panning ----------
    def _ensure_visible_point(self, rx, ry):
        """Pan tak, aby punkt był w oknie (z marginesem). Zwraca True jeśli zmieniono okno."""
        changed = False
        rx_rel = rx - self.vx
        ry_rel = ry - self.vy
        if rx_rel < PAN_MARGIN:
            self.vx = rx - PAN_MARGIN
            changed = True
        elif rx_rel > SUB_N - 1 - PAN_MARGIN:
            self.vx = rx - (SUB_N - 1 - PAN_MARGIN)
            changed = True
        if ry_rel < PAN_MARGIN:
            self.vy = ry - PAN_MARGIN
            changed = True
        elif ry_rel > SUB_N - 1 - PAN_MARGIN:
            self.vy = ry - (SUB_N - 1 - PAN_MARGIN)
            changed = True
        return changed

    def _ensure_visible_points(self, pts):
        """Pan tak, by nowe znane punkty były w oknie (wystarczy objąć środek ich bboxa)."""
        if not pts:
            return False
        xs = [x for x, _ in pts]
        ys = [y for _, y in pts]
        cx = (min(xs) + max(xs)) // 2
        cy = (min(ys) + max(ys)) // 2
        return self._ensure_visible_point(cx, cy)

    # ---------- pełne przerysowanie okna ----------
    def _redraw_all(self):
        self.canvas.delete("all")
        self._grid()
        self._draw_start_frame()

        # 1) znane-ale-nieodwiedzone (nie kolorujemy startu)
        for (rx, ry) in self.known_not_visited:
            if (rx, ry) == (0, 0):
                continue
            bb = self._cell_bbox(rx, ry)
            if not bb:
                continue
            x0, y0, x1, y1 = bb
            self.canvas.create_rectangle(x0+1, y0+1, x1-1, y1-1, fill="#d9d9d9", outline="")

        # 2) odwiedzone przez siebie (nie kolorujemy startu)
        for (rx, ry) in self.visited_self:
            if (rx, ry) == (0, 0):
                continue
            bb = self._cell_bbox(rx, ry)
            if not bb:
                continue
            x0, y0, x1, y1 = bb
            self.canvas.create_rectangle(x0+1, y0+1, x1-1, y1-1, fill=self.light, outline="")

        # 3) frontiery – szara ramka
        for (rx, ry) in self.frontiers:
            bb = self._cell_bbox(rx, ry)
            if not bb:
                continue
            x0, y0, x1, y1 = bb
            self.canvas.create_rectangle(x0+3, y0+3, x1-3, y1-3, outline="#7f7f7f", width=2)

        # 4) kropka pozycji – zawsze na wierzchu
        self._draw_dot_at_current_pos()

    def _draw_dot_at_current_pos(self):
        rx, ry = self.pos
        bb = self._cell_bbox(rx, ry)
        if bb:
            x0, y0, x1, y1 = bb
            cx = (x0 + x1) / 2
            cy = (y0 + y1) / 2
            r = SUB_CELL * 0.35
            if self.dot_id is not None:
                self.canvas.delete(self.dot_id)
            self.dot_id = self.canvas.create_oval(
                cx - r, cy - r, cx + r, cy + r,
                fill=self.color, outline="", tags=(self.DOT_TAG,)
            )
            self._raise_dot()

    # ---------- aktualizacje ----------
    def set_relative_pos(self, rx, ry):
        self.pos = (rx, ry)
        # jeżeli okno musi się przesunąć — przerysuj całość (z kropką)
        if self._ensure_visible_point(rx, ry):
            self._redraw_all()
        else:
            # tylko zaktualizuj kropkę
            self._draw_dot_at_current_pos()
        
        # TODO: new
        self._update_stats_label()

    def paint_known(self):
        # pełny redraw, żeby wszystko „pojechało” razem
        self._redraw_all()

    def update_knowledge(self, visited_set=None, frontier_set=None, path_point=None):
        # nowe informacje mogą wypchnąć poza okno -> też pan
        moved = False
        if visited_set:
            # dodaj do znanych
            for p in visited_set:
                if p not in self.visited_self:
                    self.known_not_visited.add(p)
            moved = self._ensure_visible_points(visited_set) or moved

        if frontier_set is not None:
            self.frontiers = set(frontier_set)
            moved = self._ensure_visible_points(self.frontiers) or moved

        if path_point:
            self.visited_self.add(path_point)

        # przerysuj (jeśli było przesunięcie) albo odśwież bez zmiany okna
        if moved:
            self._redraw_all()
        else:
            self.paint_known()

        # TODO: new
        # --- aktualizacja statystyk ---
        self._update_stats_label()


class WorldView:
    """Górna plansza świata (oś Y w dół)."""
    def __init__(self, canvas, world, start_xy):
        self.canvas = canvas
        self.world = world
        self.h = len(world)
        self.w = len(world[0]) if self.h else 0
        self.start_xy = start_xy
        self.agent_text_ids = {"1": None, "2": None, "3": None, "4": None}
        self.first_owner = {}  # (gx,gy) -> aid
        self.draw_base()

    def grid_bbox(self, gx, gy):
        x0 = MARGIN + gx * TOP_CELL
        y0 = MARGIN + gy * TOP_CELL
        return x0, y0, x0 + TOP_CELL, y0 + TOP_CELL

    def draw_base(self):
        # TODO: changes for sliding window
        # self.canvas.delete("all")
        # W = MARGIN * 2 + self.w * TOP_CELL
        # H = MARGIN * 2 + self.h * TOP_CELL
        # self.canvas.config(width=W, height=H, bg="white")

        self.canvas.delete("all")
        W = MARGIN * 2 + self.w * TOP_CELL
        H = MARGIN * 2 + self.h * TOP_CELL
        self.canvas.config(bg="white")
        # umożliwia przewijanie, nawet jeśli content > viewport
        self.canvas.config(scrollregion=(0, 0, W, H))
        # (opcjonalnie) narysuj białe tło na cały obszar scrollowalny:
        self.canvas.create_rectangle(0, 0, W, H, fill="white", outline="")

        for y in range(self.h):
            for x in range(self.w):
                x0, y0, x1, y1 = self.grid_bbox(x, y)
                val = self.world[y][x]
                fill = "black" if val == -1 else "white"
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=fill, outline="#ddd")

        # start – cztery kolorowe rożki
        sx, sy = self.start_xy
        x0, y0, x1, y1 = self.grid_bbox(sx, sy)
        corners = [
            ("1", [(x0, y0), ((x0+x1)/2, y0), (x0, (y0+y1)/2)]),
            ("2", [((x0+x1)/2, y0), (x1, y0), (x1, (y0+y1)/2)]),
            ("3", [(x0, (y0+y1)/2), (x0, y1), ((x0+x1)/2, y1)]),
            ("4", [((x0+x1)/2, y1), (x1, y1), (x1, (y0+y1)/2)]),
        ]
        for aid, pts in corners:
            self.canvas.create_polygon(*sum(pts, ()), fill=AGENTS[aid]["color"], outline="")

        for i in range(self.w + 1):
            x = MARGIN + i * TOP_CELL
            self.canvas.create_line(x, MARGIN, x, H - MARGIN, fill="#bbb")
        for j in range(self.h + 1):
            y = MARGIN + j * TOP_CELL
            self.canvas.create_line(MARGIN, y, W - MARGIN, y, fill="#bbb")

    def put_agent_number(self, aid, gx, gy):
        # # nie kolorujemy własności na polu startowym
        # if (gx, gy) != self.start_xy and (gx, gy) not in self.first_owner:
        #     self.first_owner[(gx, gy)] = aid
        #     x0, y0, x1, y1 = self.grid_bbox(gx, gy)
        #     tri = [(x0, y0), (x1, y0), (x0, y1)]
        #     self.canvas.create_polygon(*sum(tri, ()), fill=AGENTS[aid]["color"], outline="")
        # # numer agenta nad tłem
        # if self.agent_text_ids[aid]:
        #     self.canvas.delete(self.agent_text_ids[aid])
        # x0, y0, x1, y1 = self.grid_bbox(gx, gy)
        # tx = (x0 + x1) / 2
        # ty = (y0 + y1) / 2
        # self.agent_text_ids[aid] = self.canvas.create_text(
        #     tx, ty, text=aid, fill="black", font=("Helvetica", int(TOP_CELL * 0.6), "bold")
        # )
        # self.canvas.tag_raise(self.agent_text_ids[aid])

        # nie kolorujemy własności na polu startowym
        if (gx, gy) != self.start_xy and (gx, gy) not in self.first_owner:
            self.first_owner[(gx, gy)] = aid
            x0, y0, x1, y1 = self.grid_bbox(gx, gy)
            tri = [(x0, y0), (x1, y0), (x0, y1)]
            self.canvas.create_polygon(*sum(tri, ()), fill=AGENTS[aid]["color"], outline="")

        x0, y0, x1, y1 = self.grid_bbox(gx, gy)
        tx = (x0 + x1) / 2
        ty = (y0 + y1) / 2

        # --- nowość: wspólny tag, żeby usuwać i numer, i kółko ---
        tag = f"agent_{aid}"
        self.canvas.delete(tag)  # usuń poprzednie kółko i numer tego agenta

        # najpierw rysujemy numer, żeby znać jego bbox
        text_id = self.canvas.create_text(
            tx, ty, text=aid, fill="black",
            font=("Helvetica", int(TOP_CELL * 0.6), "bold"),
            tags=(tag,)
        )

        # dopasuj kółko do rozmiaru tekstu z niewielkim marginesem
        bx0, by0, bx1, by1 = self.canvas.bbox(text_id)
        pad = max(2, int(TOP_CELL * 0.08))  # „lekko większe niż numer”
        rx = (bx1 - bx0) / 2 + pad
        ry = (by1 - by0) / 2 + pad

        circle_id = self.canvas.create_oval(
            tx - rx, ty - rx, tx + rx, ty + rx,
            fill="white", outline="black",
            tags=(tag,)
        )

        # upewnij się, że numer jest nad kółkiem
        self.canvas.tag_lower(circle_id, text_id)
        self.canvas.tag_raise(text_id)

        # zapamiętaj id tekstu (jeśli wykorzystujesz to gdzie indziej)
        self.agent_text_ids[aid] = text_id


# =============== Aplikacja ===============
class App:
    def __init__(self, root):
        self.root = root
        root.title("Przeszukiwanie terenu — wizualizacja")
        root.bind("<space>", self.on_space)  # spacja = pauza/start

        # TODO: changes for sliding window
        # self.top_canvas = tk.Canvas(root, bg="white")
        # self.top_canvas.pack(side="top", fill="both", expand=False, padx=6, pady=6)

        self.top_scroller = ScrollableCanvas(root)
        self.top_scroller.pack(side="top", fill="both", expand=True, padx=6, pady=6)
        self.top_canvas = self.top_scroller.canvas  # reszta kodu używa dalej self.top_canvas

        self.bottom = tk.Frame(root)
        self.bottom.pack(side="top", fill="x", padx=6, pady=6)

        self.agent_views = {}
        for i, aid in enumerate(["1", "2", "3", "4"]):
            v = AgentView(self.bottom, aid, AGENTS[aid]["name"], AGENTS[aid]["color"], AGENTS[aid]["light"])
            v.frame.grid(row=0, column=i, padx=4, pady=4, sticky="n")
            self.agent_views[aid] = v

        controls = tk.Frame(root)
        controls.pack(side="bottom", fill="x", padx=6, pady=6)

        tk.Button(controls, text="Otwórz log…", command=self.open_log).pack(side="left")
        self.btn_start = tk.Button(controls, text="Start", command=self.toggle_play)
        self.btn_start.pack(side="left", padx=6)
        tk.Button(controls, text="Początek", command=self.reset).pack(side="left")

        tk.Label(controls, text="Szybkość").pack(side="left", padx=(12,4))
        self.speed = tk.Scale(controls, from_=1, to=50, orient="horizontal")
        self.speed.set(4)
        self.speed.pack(side="left")

        self.world = []
        self.start_xy = (0, 0)
        self.world_view = None
        self.events = []
        self.ei = 0
        self.timer = None
        self.playing = False

        default = "/mnt/data/agentar.log"
        if os.path.exists(default):
            self.load_log(default)

    # --- sterowanie klawiaturą ---
    def on_space(self, _event):
        self.toggle_play()

    # --- logi ---
    def load_log(self, path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                lines = f.readlines()
        except Exception as e:
            messagebox.showerror("Błąd", f"Nie można odczytać pliku:\n{e}")
            return

        self.events.clear()
        world = None
        start_xy = None

        def push(kind, **kw):
            self.events.append((kind, kw))

        for ln in lines:
            ln = ln.strip()

            mw = WORLD_RE.search(ln)
            if mw and world is None:
                try:
                    world = ast.literal_eval(mw.group(1))
                    push("world", world=world)
                except Exception:
                    pass
                continue

            ms = START_RE.search(ln)
            if ms and start_xy is None:
                start_xy = (int(ms.group(1)), int(ms.group(2)))
                push("start", start=start_xy)
                continue

            mv = VIS_RE.search(ln)
            if mv:
                aid = mv.group(2)
                pts = parse_dict_of_pairs(mv.group(3))
                push("visited", aid=aid, pts=pts)
                continue

            mf = FRONT_RE.search(ln)
            if mf:
                aid = mf.group(2)
                pts = parse_dict_of_pairs(mf.group(3))
                push("frontiers", aid=aid, pts=pts)
                continue

            mm = MOVE_RE.search(ln)
            if mm:
                aid = mm.group(2)
                gx, gy = int(mm.group(3)), int(mm.group(4))
                rx, ry = int(mm.group(5)), int(mm.group(6))
                push("move", aid=aid, gx=gx, gy=gy, rx=rx, ry=ry)
                continue

        if not world or start_xy is None:
            messagebox.showerror("Błąd", "Brak WORLD lub START POSSITION w logu.")
            return

        self.world = world
        self.start_xy = start_xy
        self.reset_geometry()
        self.reset_events()

    # --- inicjalizacja widoków ---
    def reset_geometry(self):
        self.world_view = WorldView(self.top_canvas, self.world, self.start_xy)

        # TODO: new
        # --- policz łączną liczbę białych pól (nie-ścian) ---
        self.total_white = 0
        for row in self.world:
            for val in row:
                if val != -1:
                    self.total_white += 1

        for v in self.agent_views.values():
            v.vx, v.vy = -CENTER, -CENTER
            v.known_not_visited.clear()
            v.visited_self.clear()
            v.frontiers.clear()
            v.pos = (0, 0)
            v.dot_id = None
            v.steps = 0
            v.total_white = self.total_white
            v._redraw_all()
            v._update_stats_label()

    def reset_events(self):
        self.stop_loop()
        self.ei = 0
        for aid in self.agent_views:
            v = self.agent_views[aid]
            v.set_relative_pos(0, 0)
            v.steps = 0
            v._update_stats_label()
        self.btn_start.config(text="Start")

    # --- sterowanie odtwarzaniem ---
    def open_log(self):
        path = filedialog.askopenfilename(
            title="Wybierz plik logów",
            filetypes=[("Log files", "*.log *.txt"), ("All files", "*.*")]
        )
        if path:
            self.load_log(path)

    def toggle_play(self):
        if self.playing:
            self.stop_loop()
            self.btn_start.config(text="Start")
        else:
            self.playing = True
            self.btn_start.config(text="Pauza")
            self.loop()

    def stop_loop(self):
        self.playing = False
        if self.timer is not None:
            self.root.after_cancel(self.timer)
            self.timer = None

    def reset(self):
        self.reset_geometry()
        self.reset_events()

    def loop(self):
        if not self.playing:
            return
        if self.ei >= len(self.events):
            self.stop_loop()
            self.btn_start.config(text="Start")
            return

        kind, payload = self.events[self.ei]
        self.apply_event(kind, payload)
        self.ei += 1

        delay = int(600 / self.speed.get())
        self.timer = self.root.after(max(5, delay), self.loop)

    # --- zastosowanie zdarzeń ---
    def apply_event(self, kind, payload):
        if kind == "world":
            self.world = payload["world"]
            self.reset_geometry()
        elif kind == "start":
            self.start_xy = payload["start"]
            self.reset_geometry()
        elif kind == "visited":
            aid = payload["aid"]
            self.agent_views[aid].update_knowledge(visited_set=payload["pts"])
        elif kind == "frontiers":
            aid = payload["aid"]
            self.agent_views[aid].update_knowledge(frontier_set=payload["pts"])
        elif kind == "move":
            aid = payload["aid"]
            self.agent_views[aid].steps += 1
            gx, gy, rx, ry = payload["gx"], payload["gy"], payload["rx"], payload["ry"]
            self.world_view.put_agent_number(aid, gx, gy)
            self.agent_views[aid].set_relative_pos(rx, ry)
            self.agent_views[aid].update_knowledge(path_point=(rx, ry))

# =============== Start programu ===============
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
