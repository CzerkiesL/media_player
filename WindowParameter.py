from tkinter import *
from tkinter import ttk
from tkinter import filedialog

import os

def browse_file():
    dir_name_path = filedialog.askdirectory(initialdir="b:/Music", title="selectionner un dossier")

    for path, dirs, files in os.walk(dir_name_path):
        for file in files:
            print(file)


root = Tk()

root.configure(background="#3c3c3c", padx=200, pady=100)

frame = Frame(root, bg="red", height=200, width=200, borderwidth=30)
frame.pack()

frame.grid(row=3, column=3)

root.geometry("600x600")

ttk.Label(frame, text="hello").grid(column=1, row=1)
ttk.Button(frame, text="test", command=browse_file).grid(column=0, row=0)
ttk.Label(frame, text="test").grid(column=2, row=2)

