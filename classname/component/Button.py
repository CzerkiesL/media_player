from tkinter import *

from style.style import style

class Btn(Button):
    def __init__(self, container, text, side, callback, *args):
        Button.__init__(
            self,
            container,
            text=text,
            bg=style["border_color"],
            fg = style["root_background"],
            activebackground = style["root_background"],
            activeforeground = style["border_color"],
            command = lambda: callback(*args)
        )
        self.pack(
            padx=4,
            pady=8,
            ipady = 10,
            side=side,
            anchor="center"
        )
        self.configure(font=style["btn_font"])
