import ast
import os
import re
import tkinter as tk
from tkinter import filedialog, messagebox

# =============== Konfiguracja ===============
# kolory agentów (ciemny – kropka/ramka; jasny – pole odwiedzone przez siebie)
AGENTS = {
    "1": {"name": "Agent 1 (.1.1.1)", "color": "#14b84a", "light": "#a6e9b7"},
    "2": {"name": "Agent 2 (.1.1.2)", "color": "#1f6fff", "light": "#a8c8ff"},
    "3": {"name": "Agent 3 (.1.1.3)", "color": "#ff7f0e", "light": "#ffd1a6"},
    "4": {"name": "Agent 4 (.1.1.4)", "color": "#f2c200", "light": "#ffeb99"},
}

TOP_CELL = 26     # rozmiar kafla górnej planszy
SUB_CELL = 16     # rozmiar kafla dolnych plansz (mniejsze)
MARGIN = 8

SUB_N = 17        # dolna mapa NxN (nieparzyste, środek = start)
CENTER = SUB_N // 2

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
    """Parsuje np. {(0, 0): 1, (-1, 0): 1} -> set([(0,0),(-1,0)])"""
    try:
        d = ast.literal_eval(s)
        pts = set()
        for k in d.keys():
            if isinstance(k, tuple) and len(k) == 2:
                pts.add((int(k[0]), int(k[1])))
        return pts
    except Exception:
        return set()

# =============== Widoki ===============
class AgentView:
    """Dolna plansza pojedynczego agenta (oś Y w dół)."""
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
        self._draw_grid()
        self._draw_start_frame()
        self.dot_id = None
        self.known_not_visited = set()
        self.visited_self = set()
        self.frontiers = set()

    def _draw_grid(self):
        for i in range(SUB_N + 1):
            p = i * SUB_CELL
            self.canvas.create_line(p, 0, p, SUB_N * SUB_CELL, fill="#ddd")
            self.canvas.create_line(0, p, SUB_N * SUB_CELL, p, fill="#ddd")

    def _cell_bbox(self, rx, ry):
        """rx, ry – współrzędne relatywne (Y w dół)."""
        cx = CENTER + rx
        cy = CENTER + ry            # <-- Y w dół
        x0 = cx * SUB_CELL
        y0 = cy * SUB_CELL
        return x0, y0, x0 + SUB_CELL, y0 + SUB_CELL

    def _draw_start_frame(self):
        x0, y0, x1, y1 = self._cell_bbox(0, 0)
        self.canvas.create_rectangle(x0+2, y0+2, x1-2, y1-2, outline=self.color, width=3)

    def _raise_dot(self):
        """Zapewnij, że kropka pozycji jest zawsze na wierzchu."""
        self.canvas.tag_raise(self.DOT_TAG)

    def set_relative_pos(self, rx, ry):
        # narysuj/odśwież kropkę pozycji agenta (w jego kolorze)
        x0, y0, x1, y1 = self._cell_bbox(rx, ry)
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

    def paint_known(self):
        # szare – znane ale nie odwiedzone (NIE malujemy startu 0,0)
        for (rx, ry) in self.known_not_visited:
            if (rx, ry) == (0, 0):
                continue  # nie przykrywaj pola startowego
            x0, y0, x1, y1 = self._cell_bbox(rx, ry)
            self.canvas.create_rectangle(x0+1, y0+1, x1-1, y1-1, fill="#d9d9d9", outline="")

        # jaśniejszy kolor – odwiedzone przez siebie (NIE malujemy startu 0,0)
        for (rx, ry) in self.visited_self:
            if (rx, ry) == (0, 0):
                continue  # nie koloruj, gdy agent stoi/ wszedł na start
            x0, y0, x1, y1 = self._cell_bbox(rx, ry)
            self.canvas.create_rectangle(x0+1, y0+1, x1-1, y1-1, fill=self.light, outline="")

        # frontiers – szara ramka
        for (rx, ry) in self.frontiers:
            x0, y0, x1, y1 = self._cell_bbox(rx, ry)
            self.canvas.create_rectangle(x0+3, y0+3, x1-3, y1-3, outline="#7f7f7f", width=2)

        # kropka ma być na wierzchu
        self._raise_dot()

    def update_knowledge(self, visited_set=None, frontier_set=None, path_point=None):
        if path_point:
            self.visited_self.add(path_point)
        if visited_set is not None:
            for p in visited_set:
                if p not in self.visited_self:
                    self.known_not_visited.add(p)
        if frontier_set is not None:
            self.frontiers = set(frontier_set)
        self.paint_known()


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
        """gx,gy – współrzędne globalne (Y w dół)."""
        x0 = MARGIN + gx * TOP_CELL
        y0 = MARGIN + gy * TOP_CELL
        return x0, y0, x0 + TOP_CELL, y0 + TOP_CELL

    def draw_base(self):
        self.canvas.delete("all")
        W = MARGIN * 2 + self.w * TOP_CELL
        H = MARGIN * 2 + self.h * TOP_CELL
        self.canvas.config(width=W, height=H, bg="white")

        # komórki 0/−1
        for y in range(self.h):
            for x in range(self.w):
                x0, y0, x1, y1 = self.grid_bbox(x, y)
                val = self.world[y][x]
                fill = "black" if val == -1 else "white"
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=fill, outline="#ddd")

        # start – cztery kolorowe rożki (w kolorach agentów)
        sx, sy = self.start_xy
        x0, y0, x1, y1 = self.grid_bbox(sx, sy)
        corners = [
            ("1", [(x0, y0), ((x0+x1)/2, y0), (x0, (y0+y1)/2)]),      # lewy górny
            ("2", [((x0+x1)/2, y0), (x1, y0), (x1, (y0+y1)/2)]),      # prawy górny
            ("3", [(x0, (y0+y1)/2), (x0, y1), ((x0+x1)/2, y1)]),      # lewy dolny
            ("4", [((x0+x1)/2, y1), (x1, y1), (x1, (y0+y1)/2)]),      # prawy dolny
        ]
        for aid, pts in corners:
            self.canvas.create_polygon(*sum(pts, ()), fill=AGENTS[aid]["color"], outline="")

        # siatka
        for i in range(self.w + 1):
            x = MARGIN + i * TOP_CELL
            self.canvas.create_line(x, MARGIN, x, H - MARGIN, fill="#bbb")
        for j in range(self.h + 1):
            y = MARGIN + j * TOP_CELL
            self.canvas.create_line(MARGIN, y, W - MARGIN, y, fill="#bbb")

    def put_agent_number(self, aid, gx, gy):
        """Numer agenta nad tłem trójkąta (zawsze widoczny)."""
        # nie kolorujemy pola startowego
        if (gx, gy) != self.start_xy and (gx, gy) not in self.first_owner:
            self.first_owner[(gx, gy)] = aid
            x0, y0, x1, y1 = self.grid_bbox(gx, gy)
            tri = [(x0, y0), (x1, y0), (x0, y1)]  # górny-lewy trójkąt
            self.canvas.create_polygon(*sum(tri, ()), fill=AGENTS[aid]["color"], outline="")
        # numer (po trójkącie -> na wierzchu)
        if self.agent_text_ids[aid]:
            self.canvas.delete(self.agent_text_ids[aid])
        x0, y0, x1, y1 = self.grid_bbox(gx, gy)
        tx = (x0 + x1) / 2
        ty = (y0 + y1) / 2
        self.agent_text_ids[aid] = self.canvas.create_text(
            tx, ty, text=aid, fill="black",
            font=("Helvetica", int(TOP_CELL * 0.6), "bold")
        )
        self.canvas.tag_raise(self.agent_text_ids[aid])


# =============== Aplikacja ===============
class App:
    def __init__(self, root):
        self.root = root
        root.title("Przeszukiwanie terenu - wizualizacja")
        root.bind("<space>", self.on_space)  # spacja = pauza/start

        # górna plansza
        self.top_canvas = tk.Canvas(root, bg="white")
        self.top_canvas.pack(side="top", fill="both", expand=False, padx=6, pady=6)

        # dolne 4 plansze
        self.bottom = tk.Frame(root)
        self.bottom.pack(side="top", fill="x", padx=6, pady=6)

        self.agent_views = {}
        for i, aid in enumerate(["1", "2", "3", "4"]):
            v = AgentView(
                self.bottom, aid,
                title=f"{AGENTS[aid]['name']}",
                color=AGENTS[aid]["color"],
                light=AGENTS[aid]["light"]
            )
            v.frame.grid(row=0, column=i, padx=4, pady=4, sticky="n")
            self.agent_views[aid] = v

        # sterowanie
        controls = tk.Frame(root)
        controls.pack(side="bottom", fill="x", padx=6, pady=6)

        tk.Button(controls, text="Otwórz log…", command=self.open_log).pack(side="left")
        self.btn_start = tk.Button(controls, text="Start", command=self.toggle_play)
        self.btn_start.pack(side="left", padx=6)
        tk.Button(controls, text="Początek", command=self.reset).pack(side="left")

        tk.Label(controls, text="Szybkość").pack(side="left", padx=(12,4))
        self.speed = tk.Scale(controls, from_=1, to=8, orient="horizontal")
        self.speed.set(4)
        self.speed.pack(side="left")

        # stan
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

    # ---------- Obsługa spacji ----------
    def on_space(self, _event):
        self.toggle_play()

    # ---------- Parsowanie i ładowanie ----------
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

    # ---------- Inicjalizacja widoków ----------
    def reset_geometry(self):
        self.world_view = WorldView(self.top_canvas, self.world, self.start_xy)
        for v in self.agent_views.values():
            v.canvas.delete("all")
            v._draw_grid()
            v._draw_start_frame()
            v.dot_id = None
            v.known_not_visited.clear()
            v.visited_self.clear()
            v.frontiers.clear()

    def reset_events(self):
        self.stop_loop()
        self.ei = 0
        for aid in self.agent_views:
            self.agent_views[aid].set_relative_pos(0, 0)
        self.btn_start.config(text="Start")

    # ---------- Sterowanie ----------
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
        self.timer = self.root.after(max(20, delay), self.loop)

    # ---------- Zastosowanie zdarzeń ----------
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
            gx, gy, rx, ry = payload["gx"], payload["gy"], payload["rx"], payload["ry"]
            # górna plansza – najpierw tło (z pominięciem startu), potem numer (na wierzchu)
            self.world_view.put_agent_number(aid, gx, gy)
            # dolna plansza – kropka + oznaczenie „odwiedził” (bez kolorowania startu)
            self.agent_views[aid].set_relative_pos(rx, ry)
            self.agent_views[aid].update_knowledge(path_point=(rx, ry))

# =============== Start programu ===============
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()