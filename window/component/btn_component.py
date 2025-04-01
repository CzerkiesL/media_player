from tkinter import *
import tkinter as tk

from window.style import style

def create_btn(p_container, p_text, p_side,p_callback, *args):
    btn = tk.Button(
        p_container,
        text=p_text,
        bg=style["border_color"],
        fg=style["root_background"],
        activebackground=style["root_background"],
        activeforeground=style["border_color"],
        command= lambda : p_callback(*args)
    )
    btn.pack(
        padx=(4, 4),
        pady=10,
        ipady=4,
        side=p_side,
        anchor="center",
    )
    btn.configure(font=style["btn_font"])