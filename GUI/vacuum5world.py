import tkinter as tk
import threading
import time
import ast
import os

LOG_FILE = "agentar.log"
GRID_SIZE = 5
CELL_COLORS = {
    0: "white",
    1: "gray",
    2: "black"
}

class AgentarGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Agentar System - Plansza 5x5")

        self.cells = [[None for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.cleaner_label = None
        self.cleaner_pos = None  # Zapamiętaj ostatnią pozycję A (x, y)

        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                frame = tk.Frame(root, width=70, height=70, bg="white", borderwidth=1, relief="solid")
                frame.grid(row=row, column=col, padx=2, pady=2)
                frame.grid_propagate(False)
                self.cells[row][col] = frame

        threading.Thread(target=self.tail_log, daemon=True).start()

    def update_grid(self, matrix):
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                value = matrix[row][col]
                color = CELL_COLORS.get(value, "white")
                self.cells[row][col].configure(bg=color)

        # Odrysuj A jeśli była ostatnia znana pozycja
        if self.cleaner_pos:
            x, y = self.cleaner_pos
            self.draw_cleaner(x, y)

    def draw_cleaner(self, x, y):
        if not (0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE):
            return
        if self.cleaner_label:
            self.cleaner_label.destroy()
            self.cleaner_label = None

        label = tk.Label(
            self.cells[x][y],
            text="A",
            fg="red",
            bg=self.cells[x][y]["bg"],
            font=("Helvetica", 20, "bold")
        )
        label.place(relx=0.5, rely=0.5, anchor="center")
        self.cleaner_label = label
        self.cleaner_pos = (x, y)

    def tail_log(self):
        last_logged_matrix = None

        while True:
            try:
                with open(LOG_FILE, "r") as f:
                    lines = f.readlines()
                for line in lines:
                    if "(LOGGING)" in line and "Cleaner pos" not in line:
                        try:
                            matrix_str = line.split("(LOGGING)")[1].strip()
                            matrix = ast.literal_eval(matrix_str)
                            if matrix != last_logged_matrix:
                                self.root.after(0, self.update_grid, matrix)
                                last_logged_matrix = matrix
                        except Exception as e:
                            print("Błąd przy parsowaniu macierzy:", e)

                    elif "Cleaner pos" in line:
                        try:
                            parts = line.split("Cleaner pos:")[1].strip()
                            parts = parts.replace("x=", "").replace("y=", "").split()
                            x = int(parts[0])
                            y = int(parts[1])
                            self.root.after(0, self.draw_cleaner, x, y)
                        except Exception as e:
                            print("Błąd przy parsowaniu pozycji Cleanera:", e)

            except Exception as e:
                print("Błąd przy odczycie pliku:", e)

            time.sleep(0.5)

if __name__ == "__main__":
    root = tk.Tk()
    app = AgentarGUI(root)
    root.mainloop()