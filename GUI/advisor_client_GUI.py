import re
from collections import deque, defaultdict
from datetime import datetime, timedelta
from pathlib import Path
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

# ---------------- Parsing patterns ----------------
LOG_TIME_FMT = "%H:%M:%S"

CLIENT_NEW_RE = re.compile(r"^\[(?P<ts>\d{2}:\d{2}:\d{2})\].*?\.(?P<prefix>[\d.]+)\.2\.(?P<cid>\d+):: \(LOGGING\) Client of request type:: (?P<rtype>[ABC])")
ADVISOR_TYPE_RE = re.compile(r"^\[(?P<ts>\d{2}:\d{2}:\d{2})\].*?\.(?P<aid>[\d.]+):: \(LOGGING\) I am advir?or of type\s+(?P<atype>[ABC])")
HAVE_CLIENT_RE = re.compile(r"^\[(?P<ts>\d{2}:\d{2}:\d{2})\].*?\.(?P<aid>[\d.]+):: \(LOGGING\) I have a client: (?P<client>[\d.]+)")
DOING_JOB_RE = re.compile(r"^\[(?P<ts>\d{2}:\d{2}:\d{2})\].*?\.(?P<aid>[\d.]+):: \(LOGGING\) Doing job for: (?P<client>[\d.]+)")
SLEEPING_RE = re.compile(r"^\[(?P<ts>\d{2}:\d{2}:\d{2})\].*?\.(?P<aid>[\d.]+):: Sleeping for (?P<secs>\d+) seconds")

# ---------------- Domain model ----------------
class Advisor:
    def __init__(self, agent_id: str):
        self.agent_id = agent_id  # '.1.1.1' etc.
        self.type: str | None = None  # 'A' | 'B' | 'C'
        self.current_client: str | None = None
        self.started_at: datetime | None = None
        self.last_update_ts: datetime | None = None
        self.total_done: int = 0  # per-advisor served count

class AgentarState:
    def __init__(self):
        # Queues per request type
        self.queues = {"A": deque(), "B": deque(), "C": deque()}
        self.served_counts = {"A": 0, "B": 0, "C": 0}
        # Only these advisors are tracked & shown
        self.allowed_advisors = [".1.1.1", ".1.1.2", ".1.1.3"]
        self.advisors_by_id: dict[str, Advisor] = {aid: Advisor(aid) for aid in self.allowed_advisors}
        # Map type -> advisor id (if discovered in logs)
        self.advisor_ids_by_type: dict[str, str] = {}
        # client id -> request type
        self.clients_type: dict[str, str] = {}

    def ensure_advisor(self, aid: str) -> Advisor:
        if aid not in self.advisors_by_id:
            # create but we won't show non-allowed advisors in the table
            self.advisors_by_id[aid] = Advisor(aid)
        return self.advisors_by_id[aid]

    def finish_job(self, aid: str, ts: datetime):
        adv = self.ensure_advisor(aid)
        if adv.current_client:
            client = adv.current_client
            rtype = self.clients_type.get(client)
            if rtype:
                self.served_counts[rtype] += 1
            adv.total_done += 1
            adv.current_client = None
            adv.started_at = None
            adv.last_update_ts = ts

# ---------------- Parser ----------------
class Parser:
    def __init__(self, state: AgentarState):
        self.state = state

    @staticmethod
    def _parse_ts(ts_str: str) -> datetime:
        base = datetime.combine(datetime.today().date(), datetime.min.time())
        t = datetime.strptime(ts_str, LOG_TIME_FMT).time()
        return datetime.combine(base.date(), t)

    def feed_line(self, line: str):
        m = ADVISOR_TYPE_RE.match(line)
        if m:
            ts = self._parse_ts(m['ts'])
            aid = f".{m['aid']}" if not m['aid'].startswith('.') else f"{m['aid']}"
            atype = m['atype']
            adv = self.state.ensure_advisor(aid)
            adv.type = atype
            adv.last_update_ts = ts
            if aid in self.state.allowed_advisors:
                self.state.advisor_ids_by_type[atype] = aid
            return

        m = CLIENT_NEW_RE.match(line)
        if m:
            ts = self._parse_ts(m['ts'])
            cid = f".{m['prefix']}.2.{m['cid']}"
            rtype = m['rtype']
            self.state.clients_type[cid] = rtype
            self.state.queues[rtype].append(cid)
            return

        m = HAVE_CLIENT_RE.match(line)
        if m:
            ts = self._parse_ts(m['ts'])
            aid = f".{m['aid']}" if not m['aid'].startswith('.') else f"{m['aid']}"
            client = m['client']
            client = client if client.startswith('.') else f".{client}"
            adv = self.state.ensure_advisor(aid)
            adv.last_update_ts = ts
            rtype = self.state.clients_type.get(client)
            if rtype and client in self.state.queues[rtype]:
                try:
                    self.state.queues[rtype].remove(client)
                except ValueError:
                    pass
            return

        m = DOING_JOB_RE.match(line)
        if m:
            ts = self._parse_ts(m['ts'])
            aid = f".{m['aid']}" if not m['aid'].startswith('.') else f"{m['aid']}"
            client = m['client']
            client = client if client.startswith('.') else f".{client}"
            adv = self.state.ensure_advisor(aid)
            adv.current_client = client
            adv.started_at = ts
            adv.last_update_ts = ts
            return

        m = SLEEPING_RE.match(line)
        if m:
            ts = self._parse_ts(m['ts'])
            aid = f".{m['aid']}" if not m['aid'].startswith('.') else f"{m['aid']}"
            adv = self.state.ensure_advisor(aid)
            if adv.current_client is not None:
                self.state.finish_job(aid, ts)
            else:
                adv.last_update_ts = ts
            return

# ---------------- Replay engine ----------------
class Replay:
    """Collect events from static log (order by time). Playback speed = lines per minute."""
    def __init__(self, path: Path):
        self.path = path
        self.events: list[tuple[timedelta, str]] = []
        self.cursor = 0

    def load(self):
        try:
            with open(self.path, 'r', encoding='utf-8', errors='replace') as f:
                raw_lines = [ln.rstrip('\n') for ln in f]
        except Exception as e:
            raise RuntimeError(f"Nie udało się wczytać logu: {e}")

        tmp: list[tuple[datetime, str]] = []
        for line in raw_lines:
            m = re.match(r"^\[(?P<ts>\d{2}:\d{2}:\d{2})\]", line)
            if not m:
                continue
            ts = datetime.combine(datetime.today().date(), datetime.strptime(m['ts'], LOG_TIME_FMT).time())
            tmp.append((ts, line))

        tmp.sort(key=lambda x: x[0])
        # we only need order; pacing is driven by LPM
        self.events = [(timedelta(0), line) for _, line in tmp]
        self.cursor = 0

    def reset(self):
        self.cursor = 0

    def has_next(self) -> bool:
        return self.cursor < len(self.events)

# ---------------- Tooltip helper ----------------
class Tooltip:
    def __init__(self, widget, *, text="", delay=300):
        self.widget = widget
        self.text = text
        self.delay = delay
        self._after = None
        self.tw = None

    def show(self, x, y):
        self.hide()
        self.tw = tk.Toplevel(self.widget)
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry(f"+{x}+{y}")
        label = ttk.Label(self.tw, text=self.text, background="#ffffe0", relief=tk.SOLID, borderwidth=1, padding=(6,4))
        label.pack()

    def schedule(self, x, y):
        self.cancel()
        self._after = self.widget.after(self.delay, lambda: self.show(x, y))

    def cancel(self):
        if self._after is not None:
            self.widget.after_cancel(self._after)
            self._after = None

    def hide(self):
        if self.tw is not None:
            self.tw.destroy()
            self.tw = None

# ---------------- GUI ----------------
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Agentar Queue Visualizer — Replay v3")
        self.geometry("1180x720")

        # ttk styles for nicer look
        style = ttk.Style(self)
        try:
            style.theme_use('clam')
        except tk.TclError:
            pass
        style.configure('Header.TLabel', font=("Segoe UI", 14, "bold"))
        style.configure('Count.TLabel', font=("Segoe UI", 12, "bold"))
        style.configure('Count.TLabel', foreground="#000000")  # black
        style.configure('Mini.TLabel', foreground="#666")
        style.configure('Card.TLabelframe', padding=10)
        style.configure('Card.TLabelframe.Label', font=("Segoe UI", 12, "bold"))
        style.configure('Treeview.Heading', font=("Segoe UI", 10, "bold"))

        self.state_model = AgentarState()
        self.parser = Parser(self.state_model)
        self.replay: Replay | None = None
        self._playing = False
        self._after_id: str | None = None  # handle for scheduled tick

        self._build_ui()

    # ---------------- UI build ----------------
    def _build_ui(self):
        menubar = tk.Menu(self)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Otwórz log...", command=self.open_log)
        filemenu.add_separator()
        filemenu.add_command(label="Zakończ", command=self.destroy)
        menubar.add_cascade(label="Plik", menu=filemenu)
        self.config(menu=menubar)

        root = ttk.Frame(self, padding=12)
        root.pack(fill=tk.BOTH, expand=True)

        # Controls row
        controls = ttk.Frame(root)
        controls.pack(fill=tk.X, pady=(0,12))

        ttk.Label(controls, text="Agentar — odtwarzanie", style='Header.TLabel').pack(side=tk.LEFT)

        # Lines-per-minute slider (instant effect)
        ttk.Label(controls, text="Szybkość (linie/min):").pack(side=tk.LEFT, padx=(20,6))
        self.lpm_var = tk.DoubleVar(value=120.0)
        self.lpm_scale = ttk.Scale(
            controls, from_=10.0, to=2000.0, orient=tk.HORIZONTAL,
            variable=self.lpm_var, command=self.on_lpm_change
        )
        self.lpm_scale.pack(side=tk.LEFT, fill=tk.X, expand=True)

        # Start ↔ Pauza toggle button
        self.btn_toggle = ttk.Button(controls, text="▶️ Start", command=self.toggle_play, state=tk.DISABLED)
        self.btn_toggle.pack(side=tk.LEFT, padx=6)
        self.btn_step = ttk.Button(controls, text="➡️ Krok", command=self.step, state=tk.DISABLED)
        self.btn_step.pack(side=tk.LEFT, padx=6)
        self.btn_reset = ttk.Button(controls, text="⏲ Reset", command=self.reset, state=tk.DISABLED)
        self.btn_reset.pack(side=tk.LEFT, padx=6)

        self.status_var = tk.StringVar(value="Wczytaj plik, aby rozpocząć.")
        ttk.Label(controls, textvariable=self.status_var, style='Mini.TLabel').pack(side=tk.RIGHT)

        # Two-column layout
        left = ttk.Frame(root)
        left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0,12))
        right = ttk.Frame(root)
        right.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # ---- Queues panel ----
        ttk.Label(left, text="Kolejki klientów", style='Header.TLabel').pack(anchor=tk.W)
        queues_frame = ttk.Frame(left)
        queues_frame.pack(fill=tk.BOTH, expand=True)

        self.queue_labels = {}
        self.queue_lists = {}
        for i, rtype in enumerate(["A", "B", "C"]):
            col = ttk.Labelframe(queues_frame, text=f"Typ {rtype}", style='Card.TLabelframe')
            col.grid(row=0, column=i, sticky="nsew", padx=6, pady=6)
            queues_frame.grid_columnconfigure(i, weight=1)

            info = ttk.Label(col, text="w kolejce: 0  |  obsłużeni: 0", style='Count.TLabel')
            info.pack(anchor=tk.W, pady=(0,6))
            self.queue_labels[rtype] = info

            # Fixed-size listbox + scrollbar
            lb_frame = ttk.Frame(col)
            lb_frame.pack(fill=tk.BOTH)
            lb = tk.Listbox(lb_frame, height=18, width=28, exportselection=False)
            lb.grid(row=0, column=0, sticky='nsew')
            sb = ttk.Scrollbar(lb_frame, orient=tk.VERTICAL, command=lb.yview)
            sb.grid(row=0, column=1, sticky='ns')
            lb.configure(yscrollcommand=sb.set)
            lb_frame.grid_rowconfigure(0, weight=1)
            lb_frame.grid_columnconfigure(0, weight=1)
            self.queue_lists[rtype] = lb

        # ---- Advisors panel (3 columns only) ----
        ttk.Label(right, text="Advisorzy", style='Header.TLabel').pack(anchor=tk.W)
        self.advisor_tree = ttk.Treeview(right, columns=("aid","type","done"), show="headings", height=20)
        for col, txt, w in [
            ("aid","Agent ID",180),
            ("type","Typ",80),
            ("done","Obsłużone",120)
        ]:
            self.advisor_tree.heading(col, text=txt)
            self.advisor_tree.column(col, width=w, anchor=tk.CENTER if col!="aid" else tk.W)
        self.advisor_tree.pack(fill=tk.BOTH, expand=True, pady=(6,0))

        # Tooltip on hover: shows current client & since
        self._tree_tooltip = Tooltip(self.advisor_tree, text="")
        self.advisor_tree.bind('<Motion>', self._on_tree_hover)
        self.advisor_tree.bind('<Leave>', lambda e: self._tree_tooltip.hide())

    # ---------------- Controls ----------------
    def open_log(self):
        path = filedialog.askopenfilename(title="Wybierz agentar.log", filetypes=[("Logi", "*.log"), ("Wszystkie pliki", "*.*")])
        if not path:
            return
        try:
            self.replay = Replay(Path(path))
            self.replay.load()
            self._enable_after_load(True)
            self.status_var.set(f"Załadowano {len(self.replay.events)} zdarzeń.")
            self._render_state(force_clear=True)
        except Exception as e:
            messagebox.showerror("Błąd", str(e))
            self.replay = None

    def _enable_after_load(self, loaded: bool):
        state = tk.NORMAL if loaded else tk.DISABLED
        self.btn_toggle.configure(state=state)
        self.btn_step.configure(state=state)
        self.btn_reset.configure(state=state)

    def on_lpm_change(self, _val: str):
        lpm = max(1, int(float(self.lpm_var.get())))
        self.status_var.set(f"Szybkość: {lpm} linie/min")
        # Natychmiastowy efekt: przerysuj harmonogram
        if self._playing and self._after_id is not None:
            try:
                self.after_cancel(self._after_id)
            except Exception:
                pass
            self._after_id = self.after(0, self._pump)

    def toggle_play(self):
        # Start → Pauza i z powrotem
        if self._playing:
            self._playing = False
            if self._after_id is not None:
                try:
                    self.after_cancel(self._after_id)
                except Exception:
                    pass
                self._after_id = None
            self.btn_toggle.configure(text="▶️ Start")
            self.status_var.set("Wstrzymane")
        else:
            if not self.replay or not self.replay.events:
                return
            self._playing = True
            self.btn_toggle.configure(text="⏸️ Pauza")
            self.status_var.set("Odtwarzanie…")
            self._after_id = self.after(0, self._pump)

    def reset(self):
        if not self.replay:
            return
        self.replay.reset()
        self._playing = False
        if self._after_id is not None:
            try:
                self.after_cancel(self._after_id)
            except Exception:
                pass
            self._after_id = None
        self.btn_toggle.configure(text="▶️ Start")
        # clear runtime state
        self.state_model = AgentarState()
        self.parser = Parser(self.state_model)
        self._render_state(force_clear=True)
        self.status_var.set("Zresetowano.")

    def step(self):
        if not self.replay or not self.replay.has_next():
            return
        _, line = self.replay.events[self.replay.cursor]
        self.replay.cursor += 1
        self.parser.feed_line(line)
        self._render_state()
        self.status_var.set(f"Krok {self.replay.cursor}/{len(self.replay.events)}")

    def _pump(self):
        if not (self.replay and self._playing):
            return
        if not self.replay.has_next():
            self._playing = False
            self.btn_toggle.configure(text="▶️ Start")
            self.status_var.set("Koniec odtwarzania.")
            self._after_id = None
            return

        # Emit exactly one event per tick
        _, line = self.replay.events[self.replay.cursor]
        self.replay.cursor += 1
        self.parser.feed_line(line)
        self._render_state()

        # Schedule next tick according to lines-per-minute
        lpm = max(1, int(float(self.lpm_var.get())))
        delay = int(60000 / lpm)  # ms per line
        self._after_id = self.after(delay, self._pump)

    # ---------------- Rendering ----------------
    def _render_state(self, force_clear: bool = False):
        # Queues + summaries
        for rtype, lb in self.queue_lists.items():
            lb.delete(0, tk.END)
            if not force_clear:
                for cid in list(self.state_model.queues[rtype]):
                    lb.insert(tk.END, cid)
            waiting = 0 if force_clear else len(self.state_model.queues[rtype])
            served = 0 if force_clear else self.state_model.served_counts[rtype]
            self.queue_labels[rtype].configure(text=f"w kolejce: {waiting}  |  obsłużeni: {served}")

        # Advisors table: exactly the three required advisors
        for row in self.advisor_tree.get_children():
            self.advisor_tree.delete(row)
        for aid in [".1.1.1", ".1.1.2", ".1.1.3"]:
            adv = self.state_model.advisors_by_id.get(aid) or Advisor(aid)
            atype = adv.type or "?"
            done = 0 if force_clear else adv.total_done
            self.advisor_tree.insert("", tk.END, values=(aid, atype, done))

    # ---------------- Tooltips ----------------
    def _on_tree_hover(self, event):
        # Show current client and since for row under mouse
        iid = self.advisor_tree.identify_row(event.y)
        if not iid:
            self._tree_tooltip.hide()
            return
        values = self.advisor_tree.item(iid, 'values')
        if not values:
            self._tree_tooltip.hide()
            return
        aid = values[0]
        adv = self.state_model.advisors_by_id.get(aid)
        if not adv:
            self._tree_tooltip.hide()
            return
        client = adv.current_client or "—"
        since = adv.started_at.strftime(LOG_TIME_FMT) if adv.started_at else "—"
        txt = f"Klient: {client}  |  Od: {since}"
        # place tooltip near cursor
        x_root = self.advisor_tree.winfo_rootx() + event.x + 15
        y_root = self.advisor_tree.winfo_rooty() + event.y + 10
        self._tree_tooltip.text = txt
        self._tree_tooltip.schedule(x_root, y_root)

# ---------------- Main ----------------
def main():
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()
