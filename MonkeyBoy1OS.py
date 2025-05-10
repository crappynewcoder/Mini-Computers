import tkinter as tk
import os
import sys

# Calculator app
def calculator_app():
    calc_win = tk.Toplevel()
    calc_win.title("Calculator")
    calc_win.geometry("300x200")

    entry = tk.Entry(calc_win, width=30)
    entry.pack(pady=10)

    result_label = tk.Label(calc_win, text="Result:")
    result_label.pack()

    def calculate():
        try:
            expression = entry.get()
            result = eval(expression)
            result_label.config(text=f"Result: {result}")
        except Exception as e:
            result_label.config(text=f"Error: {e}")

    calc_btn = tk.Button(calc_win, text="Calculate", command=calculate)
    calc_btn.pack(pady=5)

# Text Writer app
def text_writer_app():
    writer_win = tk.Toplevel()
    writer_win.title("Text Writer")
    writer_win.geometry("400x300")

    text_area = tk.Text(writer_win)
    text_area.pack(expand=True, fill='both')

    def save_text():
        filename = tk.filedialog.asksaveasfilename(defaultextension=".txt",
                                                  filetypes=[("Text files", "*.txt")])
        if filename:
            with open(filename, 'w') as f:
                f.write(text_area.get("1.0", tk.END))

    save_button = tk.Button(writer_win, text="Save", command=save_text)
    save_button.pack()

# Terminal app
def terminal_app():
    term_win = tk.Toplevel()
    term_win.title("Terminal")
    term_win.geometry("500x300")

    output = tk.Text(term_win, height=15)
    output.pack(fill='both', expand=True)

    command_entry = tk.Entry(term_win)
    command_entry.pack(fill='x')

    def run_command():
        cmd = command_entry.get()
        try:
            result = os.popen(cmd).read()
            output.insert(tk.END, f"> {cmd}\n{result}\n")
        except Exception as e:
            output.insert(tk.END, f"Error: {e}\n")

    run_btn = tk.Button(term_win, text="Run", command=run_command)
    run_btn.pack()

# System Info app
def system_info_app():
    info_win = tk.Toplevel()
    info_win.title("System Info")
    info_win.geometry("400x200")

    info = f"Platform: {sys.platform}\nPython Version: {sys.version}\nExecutable: {sys.executable}"
    tk.Label(info_win, text=info, justify="left").pack(padx=10, pady=10)

# Main OS GUI
def main_os():
    root = tk.Tk()
    root.title("Monkeyboy1 OS")
    root.geometry("800x600")
    root.configure(bg="#e0f0e0")

    sidebar = tk.Frame(root, width=150, bg="#a0c0ff")
    sidebar.pack(side="left", fill="y")

    tk.Label(sidebar, text="Apps", bg="#a0c0ff", font=("Arial", 14)).pack(pady=10)

    tk.Button(sidebar, text="Calculator", command=calculator_app).pack(pady=5, fill="x")
    tk.Button(sidebar, text="Text Writer", command=text_writer_app).pack(pady=5, fill="x")
    tk.Button(sidebar, text="Terminal", command=terminal_app).pack(pady=5, fill="x")
    tk.Button(sidebar, text="System Info", command=system_info_app).pack(pady=5, fill="x")

    root.mainloop()

if __name__ == "__main__":
    main_os()

















