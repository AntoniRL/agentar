import ast
import os
import re
import tkinter as tk
from tkinter import filedialog, messagebox

# =============== Konfiguracja ===============
# Kolory są "slotami" 1..4, które możesz przypisać do dowolnych ID z logu
AGENT_SLOTS = {
    "1": {"label": "Slot 1", "color": "#14b84a", "light": "#a6e9b7"},
    "2": {"label": "Slot 2", "color": "#1f6fff", "light": "#a8c8ff"},
    "3": {"label": "Slot 3", "color": "#ff7f0e", "light": "#ffd1a6"},
    "4": {"label": "Slot 4", "color": "#f2c200", "light": "#ffeb99"},
}

TOP_CELL = 26
SUB_CELL = 16
MARGIN = 8

SUB_N = 17
CENTER = SUB_N // 2
PAN_MARGIN = 1

# =============== Wzorce z logów (obsługują wielocyfrowe ID) ===============
WORLD_RE  = re.compile(r"WORLD::\s*(\[\[.*\]\])")
START_RE  = re.compile(r"START POSSITION::\s*\((\d+),\s*(\d+)\)")

#      pełny znacznik .1.1.<ID> łapiemy jako grupa(1), same <ID> jako grupa(2)
MOVE_RE   = re.compile(
    r"\.(1\.1\.(\d+))::.*GLOBAL POSSITION::\s*(-?\d+)\s+(-?\d+)\s+RELATIV POSSITION::\s*(-?\d+)\s+(-?\d+)"
)
VIS_RE    = re.compile(r"\.(1\.1\.(\d+))::.*VISITED::\s*(\{.*\})")
FRONT_RE  = re.compile(r"\.(1\.1\.(\d+))::.*FRONTIERS::\s*(\{.*\})")
AREA_RE   = re.compile(r"\.(1\.1\.(\d+))::.*area:\s*(\d+)", re.IGNORECASE)

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
class ScrollableCanvas(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master)
        self.vbar = tk.Scrollbar(self, orient="vertical")
        self.hbar = tk.Scrollbar(self, orient="horizontal")
        self.canvas = tk.Canvas(self, bg="white",
                                xscrollcommand=self.hbar.set,
                                yscrollcommand=self.vbar.set, **kwargs)
        self.vbar.config(command=self.canvas.yview)
        self.hbar.config(command=self.canvas.xview)
        self.canvas.grid(row=0, column=0, sticky="nsew")
        self.vbar.grid(row=0, column=1, sticky="ns")
        self.hbar.grid(row=1, column=0, sticky="ew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.canvas.bind("<Enter>", self._bind_wheel)
        self.canvas.bind("<Leave>", self._unbind_wheel)

    def set_scrollregion(self, x0, y0, x1, y1):
        self.canvas.config(scrollregion=(x0, y0, x1, y1))

    def _bind_wheel(self, _):
        self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)
        self.canvas.bind_all("<Shift-MouseWheel>", self._on_shift_wheel)
        self.canvas.bind_all("<Button-4>", self._on_linux_up)
        self.canvas.bind_all("<Button-5>", self._on_linux_down)

    def _unbind_wheel(self, _):
        self.canvas.unbind_all("<MouseWheel>")
        self.canvas.unbind_all("<Shift-MouseWheel>")
        self.canvas.unbind_all("<Button-4>")
        self.canvas.unbind_all("<Button-5>")

    def _on_mousewheel(self, event):
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
    DOT_TAG = "agent_pos_dot"

    def __init__(self, root, slot_id, title, color, light):
        self.slot_id = slot_id  # "1".."4" – slot kolorystyczny
        self.color = color
        self.light = light
        self.frame = tk.Frame(root, bd=2, relief="groove")
        self.title_label = tk.Label(self.frame, text=title)
        self.title_label.pack()

        w = SUB_N * SUB_CELL
        h = SUB_N * SUB_CELL
        self.canvas = tk.Canvas(self.frame, width=w, height=h, bg="white")
        self.canvas.pack(padx=6, pady=6)

        self.total_white = 0
        self.steps = 0
        self.area_here = None
        self.stats_var = tk.StringVar(value="Frontiery: 0\nOdkryte: 0/0 (0.0%)\nKroki: 0\nArea tu: -")
        tk.Label(self.frame, textvariable=self.stats_var, justify="left").pack(pady=(0,6))

        self.vx = -CENTER
        self.vy = -CENTER

        self.known_not_visited = set()
        self.visited_self = set()
        self.frontiers = set()

        self.pos = (0, 0)
        self.dot_id = None

        self._redraw_all()

    def set_title(self, text):
        self.title_label.config(text=text)

    def _grid(self):
        for i in range(SUB_N + 1):
            p = i * SUB_CELL
            self.canvas.create_line(p, 0, p, SUB_N * SUB_CELL, fill="#ddd")
            self.canvas.create_line(0, p, SUB_N * SUB_CELL, p, fill="#ddd")

    def _cell_bbox(self, rx, ry):
        rx_rel = rx - self.vx
        ry_rel = ry - self.vy
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

    def _update_stats_label(self):
        discovered_set = set(self.known_not_visited) | set(self.visited_self) | {(0, 0)}
        discovered = len(discovered_set)
        total = max(1, int(self.total_white))
        pct = (discovered / total) * 100.0
        front = len(self.frontiers)
        area_txt = "-" if self.area_here is None else str(self.area_here)
        self.stats_var.set(
            f"Frontiery: {front}\nOdkryte: {discovered}/{total} ({pct:.1f}%)\nKroki: {self.steps}\nArea tu: {area_txt}"
        )

    def _ensure_visible_point(self, rx, ry):
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
        if not pts:
            return False
        xs = [x for x, _ in pts]
        ys = [y for _, y in pts]
        cx = (min(xs) + max(xs)) // 2
        cy = (min(ys) + max(ys)) // 2
        return self._ensure_visible_point(cx, cy)

    def _redraw_all(self):
        self.canvas.delete("all")
        self._grid()
        self._draw_start_frame()

        for (rx, ry) in self.known_not_visited:
            if (rx, ry) == (0, 0):
                continue
            bb = self._cell_bbox(rx, ry)
            if not bb:
                continue
            x0, y0, x1, y1 = bb
            self.canvas.create_rectangle(x0+1, y0+1, x1-1, y1-1, fill="#d9d9d9", outline="")

        for (rx, ry) in self.visited_self:
            if (rx, ry) == (0, 0):
                continue
            bb = self._cell_bbox(rx, ry)
            if not bb:
                continue
            x0, y0, x1, y1 = bb
            self.canvas.create_rectangle(x0+1, y0+1, x1-1, y1-1, fill=self.light, outline="")

        for (rx, ry) in self.frontiers:
            bb = self._cell_bbox(rx, ry)
            if not bb:
                continue
            x0, y0, x1, y1 = bb
            self.canvas.create_rectangle(x0+3, y0+3, x1-3, y1-3, outline="#7f7f7f", width=2)

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

    def set_relative_pos(self, rx, ry):
        self.pos = (rx, ry)
        if self._ensure_visible_point(rx, ry):
            self._redraw_all()
        else:
            self._draw_dot_at_current_pos()
        self._update_stats_label()

    def paint_known(self):
        self._redraw_all()

    def update_knowledge(self, visited_set=None, frontier_set=None, path_point=None):
        moved = False
        if visited_set:
            for p in visited_set:
                if p not in self.visited_self:
                    self.known_not_visited.add(p)
            moved = self._ensure_visible_points(visited_set) or moved

        if frontier_set is not None:
            self.frontiers = set(frontier_set)
            moved = self._ensure_visible_points(self.frontiers) or moved

        if path_point:
            self.visited_self.add(path_point)

        if moved:
            self._redraw_all()
        else:
            self.paint_known()

        self._update_stats_label()

    def set_area(self, val:int):
        self.area_here = val
        self._update_stats_label()


class WorldView:
    """Górna plansza świata. Kolory – wg slotów 1..4."""
    def __init__(self, canvas, world, start_xy):
        self.canvas = canvas
        self.world = world
        self.h = len(world)
        self.w = len(world[0]) if self.h else 0
        self.start_xy = start_xy
        self.agent_text_ids = {"1": None, "2": None, "3": None, "4": None}
        self.first_owner = {}
        self.draw_base()

    def grid_bbox(self, gx, gy):
        x0 = MARGIN + gx * TOP_CELL
        y0 = MARGIN + gy * TOP_CELL
        return x0, y0, x0 + TOP_CELL, y0 + TOP_CELL

    def draw_base(self):
        self.canvas.delete("all")
        W = MARGIN * 2 + self.w * TOP_CELL
        H = MARGIN * 2 + self.h * TOP_CELL
        self.canvas.config(bg="white")
        self.canvas.config(scrollregion=(0, 0, W, H))
        self.canvas.create_rectangle(0, 0, W, H, fill="white", outline="")

        for y in range(self.h):
            for x in range(self.w):
                x0, y0, x1, y1 = self.grid_bbox(x, y)
                val = self.world[y][x]
                fill = "black" if val == -1 else "white"
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=fill, outline="#ddd")

        # Start – cztery kolorowe rożki (sloty 1..4)
        sx, sy = self.start_xy
        x0, y0, x1, y1 = self.grid_bbox(sx, sy)
        corners = [
            ("1", [(x0, y0), ((x0+x1)/2, y0), (x0, (y0+y1)/2)]),
            ("2", [((x0+x1)/2, y0), (x1, y0), (x1, (y0+y1)/2)]),
            ("3", [(x0, (y0+y1)/2), (x0, y1), ((x0+x1)/2, y1)]),
            ("4", [((x0+x1)/2, y1), (x1, y1), (x1, (y0+y1)/2)]),
        ]
        for slot, pts in corners:
            self.canvas.create_polygon(*sum(pts, ()), fill=AGENT_SLOTS[slot]["color"], outline="")

        for i in range(self.w + 1):
            x = MARGIN + i * TOP_CELL
            self.canvas.create_line(x, MARGIN, x, H - MARGIN, fill="#bbb")
        for j in range(self.h + 1):
            y = MARGIN + j * TOP_CELL
            self.canvas.create_line(MARGIN, y, W - MARGIN, y, fill="#bbb")

    def put_agent_number(self, slot, gx, gy, shown_id_text):
        # pokoloruj własność (poza startem) wg slotu
        if (gx, gy) != self.start_xy and (gx, gy) not in self.first_owner:
            self.first_owner[(gx, gy)] = slot
            x0, y0, x1, y1 = self.grid_bbox(gx, gy)
            tri = [(x0, y0), (x1, y0), (x0, y1)]
            self.canvas.create_polygon(*sum(tri, ()), fill=AGENT_SLOTS[slot]["color"], outline="")

        x0, y0, x1, y1 = self.grid_bbox(gx, gy)
        tx = (x0 + x1) / 2
        ty = (y0 + y1) / 2

        tag = f"agent_{slot}"
        self.canvas.delete(tag)

        text_id = self.canvas.create_text(
            tx, ty, text=shown_id_text, fill="black",
            font=("Helvetica", int(TOP_CELL * 0.45), "bold"),
            tags=(tag,)
        )

        bx0, by0, bx1, by1 = self.canvas.bbox(text_id)
        pad = max(2, int(TOP_CELL * 0.08))
        rx = (bx1 - bx0) / 2 + pad

        circle_id = self.canvas.create_oval(
            tx - rx, ty - rx, tx + rx, ty + rx,
            fill="white", outline="black", tags=(tag,)
        )
        self.canvas.tag_lower(circle_id, text_id)
        self.canvas.tag_raise(text_id)

        self.agent_text_ids[slot] = text_id

# =============== Aplikacja ===============
class App:
    def __init__(self, root):
        self.root = root
        root.title("Przeszukiwanie terenu — wizualizacja")
        root.bind("<space>", self.on_space)

        self.top_scroller = ScrollableCanvas(root)
        self.top_scroller.pack(side="top", fill="both", expand=True, padx=6, pady=6)
        self.top_canvas = self.top_scroller.canvas

        self.bottom = tk.Frame(root)
        self.bottom.pack(side="top", fill="x", padx=6, pady=6)

        # --- mapowanie: ID z logu -> slot ("1".."4")
        self.slot_ids = ["1", "2", "3", "4"]  # domyślnie ID = 1,2,3,4
        self.id_to_slot = {sid: slot for sid, slot in zip(self.slot_ids, ["1","2","3","4"])}

        # widoki agentów (sloty 1..4)
        self.agent_views = {}
        for i, slot in enumerate(["1","2","3","4"]):
            title = f"{AGENT_SLOTS[slot]['label']} (.1.1.{self.slot_ids[i]})"
            v = AgentView(self.bottom, slot, title, AGENT_SLOTS[slot]["color"], AGENT_SLOTS[slot]["light"])
            v.frame.grid(row=0, column=i, padx=4, pady=4, sticky="n")
            self.agent_views[slot] = v

        # --- Panel sterowania
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

        # --- NOWE: wybór ID agentów (4 liczby lub pełne 1.1.X) ---
        tk.Label(controls, text="ID agentów (4 wartości, przecinkami):").pack(side="left", padx=(12,4))
        self.ids_entry = tk.Entry(controls, width=22)
        self.ids_entry.insert(0, "1,2,3,4")
        self.ids_entry.pack(side="left")
        tk.Button(controls, text="Zastosuj ID", command=self.apply_ids_from_entry).pack(side="left", padx=6)

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

    # --- pomoc: parsowanie wpisanych ID ---
    def _normalize_id(self, token: str) -> str:
        token = token.strip()
        if token.startswith("1.1."):
            token = token.split(".")[-1]
        return token  # zwracamy samą część liczbową jako str (np. "7")

    def apply_ids_from_entry(self):
        raw = self.ids_entry.get().strip()
        parts = [p for p in raw.split(",") if p.strip()]
        if len(parts) != 4:
            messagebox.showerror("Błąd", "Podaj dokładnie 4 ID, np. 5,6,7,8 lub 1.1.5, 1.1.6, 1.1.7, 1.1.8")
            return

        new_ids = [self._normalize_id(p) for p in parts]
        if not all(idp.isdigit() for idp in new_ids):
            messagebox.showerror("Błąd", "ID muszą być liczbami (np. 5,6,7,8).")
            return

        self.slot_ids = new_ids
        self.id_to_slot = {sid: slot for sid, slot in zip(self.slot_ids, ["1","2","3","4"])}

        # zaktualizuj tytuły
        for i, slot in enumerate(["1","2","3","4"]):
            self.agent_views[slot].set_title(f"{AGENT_SLOTS[slot]['label']} (.1.1.{self.slot_ids[i]})")

        # odśwież startowy kafel (kolory są te same; tytuły już zmienione)
        if self.world:
            self.reset_geometry()
            self.reset_events()

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

            ma = AREA_RE.search(ln)
            if ma:
                log_id = ma.group(2)  # np. "7"
                area_val = int(ma.group(3))
                push("area", aid=log_id, area=area_val)

            mv = VIS_RE.search(ln)
            if mv:
                log_id = mv.group(2)
                pts = parse_dict_of_pairs(mv.group(3))
                push("visited", aid=log_id, pts=pts)

            mf = FRONT_RE.search(ln)
            if mf:
                log_id = mf.group(2)
                pts = parse_dict_of_pairs(mf.group(3))
                push("frontiers", aid=log_id, pts=pts)

            mm = MOVE_RE.search(ln)
            if mm:
                log_id = mm.group(2)
                gx, gy = int(mm.group(3)), int(mm.group(4))
                rx, ry = int(mm.group(5)), int(mm.group(6))
                push("move", aid=log_id, gx=gx, gy=gy, rx=rx, ry=ry)

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
            v.area_here = None
            v._redraw_all()
            v._update_stats_label()

    def reset_events(self):
        self.stop_loop()
        self.ei = 0
        for slot in self.agent_views:
            v = self.agent_views[slot]
            v.set_relative_pos(0, 0)
            v.steps = 0
            v.area_here = None
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

    # --- pomoc: mapowanie ID z logu -> slot 1..4 (albo None jeśli ignorujemy)
    def _slot_for_log_id(self, log_id: str):
        return self.id_to_slot.get(log_id)

    # --- zastosowanie zdarzeń ---
    def apply_event(self, kind, payload):
        if kind == "world":
            self.world = payload["world"]
            self.reset_geometry()
        elif kind == "start":
            self.start_xy = payload["start"]
            self.reset_geometry()
        elif kind == "visited":
            log_id = payload["aid"]
            slot = self._slot_for_log_id(log_id)
            if slot:
                self.agent_views[slot].update_knowledge(visited_set=payload["pts"])
        elif kind == "frontiers":
            log_id = payload["aid"]
            slot = self._slot_for_log_id(log_id)
            if slot:
                self.agent_views[slot].update_knowledge(frontier_set=payload["pts"])
        elif kind == "area":
            log_id = payload["aid"]
            slot = self._slot_for_log_id(log_id)
            if slot:
                self.agent_views[slot].set_area(payload["area"])
        elif kind == "move":
            log_id = payload["aid"]
            slot = self._slot_for_log_id(log_id)
            if slot:
                self.agent_views[slot].steps += 1
                gx, gy, rx, ry = payload["gx"], payload["gy"], payload["rx"], payload["ry"]
                # na górze w kółku pokażemy samo ID (np. "7")
                self.world_view.put_agent_number(slot, gx, gy, log_id)
                self.agent_views[slot].set_relative_pos(rx, ry)
                self.agent_views[slot].update_knowledge(path_point=(rx, ry))

# =============== Start programu ===============
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
