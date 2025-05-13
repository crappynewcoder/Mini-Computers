import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import os
import sys
import json
from datetime import datetime

# Cache file path
CACHE_FILE = "minicomputer_cache.json"

# Initialize cache if it doesn't exist
if not os.path.exists(CACHE_FILE):
    with open(CACHE_FILE, "w") as f:
        json.dump({}, f)

class MiniComputer:
    def __init__(self, root):
        self.root = root
        self.root.withdraw()  # Hide the main window initially
        self.open_apps = set()
        self.system_info_window = None

        self.show_login_screen()

    def show_login_screen(self):
        login = tk.Toplevel()
        login.title("Welcome to MiniComputer")
        login.geometry("400x250")
        login.configure(bg="#ddeeff")

        label = tk.Label(login, text="Welcome! Click to Start.", font=("Segoe UI", 18), bg="#ddeeff")
        label.pack(pady=60)
        tk.Button(login, text="Login", font=("Segoe UI", 14), bg="#6699ff", fg="white", command=lambda: self.start_computer(login)).pack()

    def start_computer(self, login_window):
        login_window.destroy()
        self.root.deiconify()
        self.root.title("Mini Computer")
        self.root.geometry("1000x650")
        self.root.configure(bg="#f0f4ff")
        self.create_ui()

    def create_ui(self):
        self.create_sidebar()
        self.create_start_menu_button()
        self.create_search_box()
        self.create_desktop()

    def create_desktop(self):
        self.desktop_label = tk.Label(self.root, text="Desktop", bg="#f0f4ff", font=("Segoe UI", 16))
        self.desktop_label.pack(pady=20)

    def create_sidebar(self):
        sidebar = tk.Frame(self.root, bg="#ccddee", width=120)
        sidebar.pack(side="left", fill="y")

        apps = [
            ("Explorer", self.open_file_explorer),
            ("Editor", self.open_text_editor),
            ("Calc", self.open_calculator),
            ("Ball", self.open_bouncyball),
            ("SysInfo", self.open_system_info),
            ("Terminal", self.open_terminal)
        ]
        for name, cmd in apps:
            tk.Button(sidebar, text=name, width=14, bg="#aaccff", command=cmd).pack(pady=5)

    def create_start_menu_button(self):
        tk.Button(self.root, text="Start", bg="#6688cc", fg="white", command=self.show_start_menu).place(x=10, y=610, width=80)

    def show_start_menu(self):
        menu = tk.Toplevel(self.root)
        menu.title("Start Menu")
        menu.geometry("200x150+10+450")
        menu.configure(bg="#ccddee")

        tk.Button(menu, text="Reboot", width=20, command=self.reboot).pack(pady=10)
        tk.Button(menu, text="Shut Down", width=20, command=self.root.quit).pack(pady=10)

    def create_search_box(self):
        self.search_window = None
        self.root.bind('<Control-f>', self.toggle_search_box)

    def toggle_search_box(self, _):
        if self.search_window and self.search_window.winfo_exists():
            self.search_window.destroy()
        else:
            self.search_window = tk.Toplevel(self.root)
            self.search_window.title("Search")
            self.search_window.geometry("400x200+300+300")
            entry = tk.Entry(self.search_window, font=("Segoe UI", 14))
            entry.pack(pady=20, padx=20)
            results = tk.Listbox(self.search_window, width=40)
            results.pack()

            with open(CACHE_FILE, "r") as f:
                files = json.load(f)

            def search():
                query = entry.get().lower()
                results.delete(0, tk.END)
                for name in files:
                    if query in name.lower():
                        results.insert(tk.END, name)

            entry.bind("<Return>", lambda _: search())

    def reboot(self):
        python = sys.executable
        os.execl(python, python, *sys.argv)

    def open_file_explorer(self):
        explorer = tk.Toplevel(self.root)
        explorer.title("File Explorer")
        explorer.geometry("500x400")

        listbox = tk.Listbox(explorer, width=60)
        listbox.pack(pady=10)

        with open(CACHE_FILE, "r") as f:
            files = json.load(f)
        for fname in files:
            listbox.insert(tk.END, fname)

    def open_text_editor(self):
        self.open_apps.add("Editor")
        win = tk.Toplevel(self.root)
        win.title("Text Editor")
        win.geometry("500x400")

        area = tk.Text(win)
        area.pack(expand=True, fill='both')

        def save():
            filename = simpledialog.askstring("Filename", "Enter file name:")
            if filename:
                content = area.get("1.0", tk.END)
                with open(CACHE_FILE, "r") as f:
                    data = json.load(f)
                data[filename] = content
                with open(CACHE_FILE, "w") as f:
                    json.dump(data, f)
                messagebox.showinfo("Saved", "File saved internally.")

        tk.Button(win, text="Save", command=save).pack()

        def on_close():
            self.open_apps.discard("Editor")
            win.destroy()
        win.protocol("WM_DELETE_WINDOW", on_close)

    def open_calculator(self):
        self.open_apps.add("Calculator")
        win = tk.Toplevel(self.root)
        win.title("Calculator")
        win.geometry("300x400")

        expr = tk.StringVar()
        entry = tk.Entry(win, textvariable=expr, font=("Arial", 20), justify="right")
        entry.pack(fill="x", padx=10, pady=10)

        buttons = '789/', '456*', '123-', 'C0=+'

        for row in buttons:
            f = tk.Frame(win)
            f.pack()
            for btn in row:
                action = lambda b=btn: self.calc_press(expr, b)
                tk.Button(f, text=btn, width=5, height=2, command=action).pack(side="left")

        def on_close():
            self.open_apps.discard("Calculator")
            win.destroy()
        win.protocol("WM_DELETE_WINDOW", on_close)

    def calc_press(self, expr, key):
        if key == "=":
            try:
                expr.set(str(eval(expr.get())))
            except:
                expr.set("Error")
        elif key == "C":
            expr.set("")
        else:
            expr.set(expr.get() + key)

    def open_bouncyball(self):
        self.open_apps.add("BouncyBall")
        win = tk.Toplevel(self.root)
        win.title("BouncyBall")
        win.geometry("400x300")
        canvas = tk.Canvas(win, bg="white")
        canvas.pack(fill="both", expand=True)
        ball = canvas.create_oval(10, 10, 30, 30, fill="red")
        dx, dy = 3, 3

        def move():
            nonlocal dx, dy
            canvas.move(ball, dx, dy)
            pos = canvas.coords(ball)
            if pos[2] >= canvas.winfo_width() or pos[0] <= 0:
                dx = -dx
            if pos[3] >= canvas.winfo_height() or pos[1] <= 0:
                dy = -dy
            canvas.after(20, move)

        move()

        def on_close():
            self.open_apps.discard("BouncyBall")
            win.destroy()
        win.protocol("WM_DELETE_WINDOW", on_close)

    def open_terminal(self):
        win = tk.Toplevel(self.root)
        win.title("Mini Terminal")
        win.geometry("500x300")

        output = tk.Text(win, height=15)
        output.pack()
        input_box = tk.Entry(win)
        input_box.pack(fill="x")

        def run_command(event=None):
            cmd = input_box.get()
            try:
                result = str(eval(cmd)) if not cmd.startswith("print") else exec(cmd)
            except Exception as e:
                result = str(e)
            output.insert(tk.END, f"> {cmd}\n{result}\n")
            input_box.delete(0, tk.END)

        input_box.bind("<Return>", run_command)

    def open_system_info(self):
        if self.system_info_window and self.system_info_window.winfo_exists():
            return
        self.system_info_window = tk.Toplevel(self.root)
        self.system_info_window.title("System Info")
        self.system_info_window.geometry("300x200")
        cpu_label = tk.Label(self.system_info_window, text="CPU: ")
        gpu_label = tk.Label(self.system_info_window, text="GPU: ")
        ram_label = tk.Label(self.system_info_window, text="RAM: ")
        cpu_label.pack()
        gpu_label.pack()
        ram_label.pack()

        def update():
            load = {
                "Editor": (5, 0, 20),
                "Calculator": (2, 0, 10),
                "BouncyBall": (10, 10, 30),
                "Terminal": (4, 0, 15)
            }
            cpu = sum(load[app][0] for app in self.open_apps if app in load)
            gpu = sum(load[app][1] for app in self.open_apps if app in load)
            ram = sum(load[app][2] for app in self.open_apps if app in load)

            cpu_label.config(text=f"MiniCPU Usage: {cpu}%")
            gpu_label.config(text=f"MiniGPU Usage: {gpu}%")
            ram_label.config(text=f"MiniRAM Usage: {ram}MB")

            self.system_info_window.after(1000, update)

        update()

if __name__ == "__main__":
    root = tk.Tk()
    MiniComputer(root)
    root.mainloop()
