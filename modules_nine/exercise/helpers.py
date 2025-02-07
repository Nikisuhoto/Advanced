import tkinter as tk
from canvas import app


def clean_screen():
    for el in app.grid_slaves():
        el.destroy()

    tk.Button(app, text="Exit", command=app.destroy).grid(row=1000, column=1000, pady=10, padx=10)
