import tkinter as tk
from tkinter import filedialog, messagebox
from core import make_collage

def select_folder():
    folder = filedialog.askdirectory()
    folder_var.set(folder)

def generate():
    folder = folder_var.get()
    if not folder:
        messagebox.showerror("Error", "Please select a folder.")
        return
    try:
        rows = int(rows_var.get())
        cols = int(cols_var.get())
        target_width = int(width_var.get())
        target_height = int(height_var.get())
        if rows <= 0 or cols <= 0 or target_width <= 0 or target_height <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Rows, columns, width, and height must be positive integers.")
        return

    # Call core function with empty captions (no caption input)
    make_collage(folder, rows, cols, target_width, target_height, captions=[])
    messagebox.showinfo("Success", "Collage saved as collage.jpg")

root = tk.Tk()
root.title("Collage Maker GUI")

tk.Label(root, text="Folder:").grid(row=0, column=0, sticky="e")
folder_var = tk.StringVar()
tk.Entry(root, textvariable=folder_var, width=40).grid(row=0, column=1)
tk.Button(root, text="Browse", command=select_folder).grid(row=0, column=2)

tk.Label(root, text="Rows:").grid(row=1, column=0, sticky="e")
rows_var = tk.StringVar()
tk.Entry(root, textvariable=rows_var).grid(row=1, column=1)

tk.Label(root, text="Columns:").grid(row=2, column=0, sticky="e")
cols_var = tk.StringVar()
tk.Entry(root, textvariable=cols_var).grid(row=2, column=1)

tk.Label(root, text="Target Width (px):").grid(row=3, column=0, sticky="e")
width_var = tk.StringVar()
tk.Entry(root, textvariable=width_var).grid(row=3, column=1)

tk.Label(root, text="Target Height (px):").grid(row=4, column=0, sticky="e")
height_var = tk.StringVar()
tk.Entry(root, textvariable=height_var).grid(row=4, column=1)

tk.Button(root, text="Generate Collage", command=generate).grid(row=5, column=1, pady=10)

root.mainloop()
