import tkinter as tk
from tkinter import filedialog, messagebox
import os
import sys
import json

class MiniComputer:
    def __init__(self, root):
        self.root = root
        self.root.title("Mini Computer")
        self.root.geometry("800x600")
        self.root.configure(bg="lightblue")

        self.open_apps = set()
        self.create_sidebar()
        self.create_start_menu_button()
        self.create_desktop()

        self.system_info_window = None

    def create_desktop(self):
        self.desktop_label = tk.Label(self.root, text="Welcome to Mini Computer!", bg="lightblue", font=("Arial", 16))
        self.desktop_label.pack(pady=20)

    def create_sidebar(self):
        sidebar = tk.Frame(self.root, bg="gray", width=100)
        sidebar.pack(side="left", fill="y")

        tk.Button(sidebar, text="Explorer", command=self.open_file_explorer, width=12).pack(pady=10)
        tk.Button(sidebar, text="Editor", command=self.open_text_editor, width=12).pack(pady=10)
        tk.Button(sidebar, text="Calc", command=self.open_calculator, width=12).pack(pady=10)
        tk.Button(sidebar, text="BouncyBall", command=self.open_bouncyball, width=12).pack(pady=10)
        tk.Button(sidebar, text="Sys Info", command=self.open_system_info, width=12).pack(pady=10)

    def create_start_menu_button(self):
        start_btn = tk.Button(self.root, text="Start", bg="gray", fg="white", command=self.show_start_menu)
        start_btn.place(x=10, y=560, width=60)

    def show_start_menu(self):
        menu = tk.Toplevel(self.root)
        menu.title("Start Menu")
        menu.geometry("200x150+10+400")
        menu.configure(bg="gray")

        tk.Button(menu, text="Reboot", width=20, command=self.reboot).pack(pady=10)
        tk.Button(menu, text="Shut Down", width=20, command=self.root.quit).pack(pady=10)

    def reboot(self):
        python = sys.executable
        os.execl(python, python, *sys.argv)

    def open_file_explorer(self):
        explorer = tk.Toplevel(self.root)
        explorer.title("File Explorer")
        explorer.geometry("500x400")

        file_list = tk.Listbox(explorer, width=60)
        file_list.pack(pady=10)

        cache_file = "minicomputer_cache.json"
        if os.path.exists(cache_file):
            with open(cache_file, "r") as f:
                files = json.load(f)
        else:
            files = {}

        for filename in files.keys():
            file_list.insert(tk.END, filename)

    def open_text_editor(self):
        self.open_apps.add("Editor")
        editor = tk.Toplevel(self.root)
        editor.title("Text Editor")
        editor.geometry("500x400")

        text_area = tk.Text(editor, wrap='word')
        text_area.pack(expand=1, fill='both')

        def save_file():
            content = text_area.get("1.0", tk.END)
            file_name = filedialog.asksaveasfilename(defaultextension=".txt")
            if file_name:
                with open("minicomputer_cache.json", "r" if os.path.exists("minicomputer_cache.json") else "w+") as f:
                    try:
                        data = json.load(f)
                    except:
                        data = {}
                data[os.path.basename(file_name)] = content
                with open("minicomputer_cache.json", "w") as f:
                    json.dump(data, f)
                messagebox.showinfo("Saved", "File saved successfully.")

        def on_close():
            self.open_apps.discard("Editor")
            editor.destroy()

        editor.protocol("WM_DELETE_WINDOW", on_close)
        tk.Button(editor, text="Save", command=save_file).pack()

    def open_calculator(self):
        self.open_apps.add("Calculator")
        calc = tk.Toplevel(self.root)
        calc.title("Calculator")
        calc.geometry("300x400")

        expr = tk.StringVar()
        entry = tk.Entry(calc, textvariable=expr, font=("Arial", 20), justify="right")
        entry.pack(fill="x", padx=10, pady=10)

        def press(key):
            if key == "=":
                try:
                    result = eval(expr.get())
                    expr.set(str(result))
                except:
                    expr.set("Error")
            elif key == "C":
                expr.set("")
            else:
                expr.set(expr.get() + key)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        frame = tk.Frame(calc)
        frame.pack()

        for i, btn in enumerate(buttons):
            tk.Button(frame, text=btn, width=5, height=2, command=lambda b=btn: press(b)).grid(row=i//4, column=i%4)

        def on_close():
            self.open_apps.discard("Calculator")
            calc.destroy()

        calc.protocol("WM_DELETE_WINDOW", on_close)

    def open_bouncyball(self):
        self.open_apps.add("BouncyBall")
        ball_app = tk.Toplevel(self.root)
        ball_app.title("BouncyBall")
        ball_app.geometry("400x300")

        canvas = tk.Canvas(ball_app, bg="white")
        canvas.pack(fill="both", expand=True)

        ball = canvas.create_oval(10, 10, 30, 30, fill="red")
        dx, dy = 3, 3

        def move_ball():
            nonlocal dx, dy
            canvas.move(ball, dx, dy)
            pos = canvas.coords(ball)
            if pos[2] >= canvas.winfo_width() or pos[0] <= 0:
                dx = -dx
            if pos[3] >= canvas.winfo_height() or pos[1] <= 0:
                dy = -dy
            canvas.after(20, move_ball)

        move_ball()

        def on_close():
            self.open_apps.discard("BouncyBall")
            ball_app.destroy()

        ball_app.protocol("WM_DELETE_WINDOW", on_close)

    def open_system_info(self):
        if self.system_info_window and self.system_info_window.winfo_exists():
            return

        self.system_info_window = tk.Toplevel(self.root)
        self.system_info_window.title("Mini System Info")
        self.system_info_window.geometry("300x200")

        cpu_label = tk.Label(self.system_info_window, text="CPU Usage:")
        gpu_label = tk.Label(self.system_info_window, text="GPU Usage:")
        ram_label = tk.Label(self.system_info_window, text="RAM Usage:")

        cpu_label.pack(pady=5)
        gpu_label.pack(pady=5)
        ram_label.pack(pady=5)

        def update_stats():
            app_load = {
                "Editor": (5, 0, 20),
                "Calculator": (2, 0, 10),
                "BouncyBall": (15, 25, 30)
            }
            cpu = sum(app_load[app][0] for app in self.open_apps if app in app_load)
            gpu = sum(app_load[app][1] for app in self.open_apps if app in app_load)
            ram = sum(app_load[app][2] for app in self.open_apps if app in app_load)

            cpu_label.config(text=f"MiniCPU Usage: {cpu}%")
            gpu_label.config(text=f"MiniGPU Usage: {gpu}%")
            ram_label.config(text=f"MiniRAM Usage: {ram}MB")

            self.system_info_window.after(1000, update_stats)

        update_stats()

# Run the Mini Computer
if __name__ == "__main__":
    root = tk.Tk()
    app = MiniComputer(root)
    root.mainloop()







