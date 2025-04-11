import tkinter as tk
from tkinter import messagebox
from app.logic import process_input
from app.database import init_db

def run_desktop_gui():
    init_db()

    def submit():
        username = username_entry.get()
        try:
            size = float(size_entry.get())
            actual = process_input(username, size)
            messagebox.showinfo("Result", f"Actual Size: {actual:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Invalid size input.")

    root = tk.Tk()
    root.title("Microscope Size Calculator")

    tk.Label(root, text="Username").grid(row=0)
    username_entry = tk.Entry(root)
    username_entry.grid(row=0, column=1)

    tk.Label(root, text="Microscope Size (μm)").grid(row=1)
    size_entry = tk.Entry(root)
    size_entry.grid(row=1, column=1)

    tk.Button(root, text="Calculate", command=submit).grid(row=2, columnspan=2)

    root.mainloop()
