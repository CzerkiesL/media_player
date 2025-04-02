from tkinter import *

class Frm(Frame):
    def __init__(self, container, background, border_width):
        Frame.__init__(
            self,
            container,
            bg=background,
            borderwidth=border_width,
            relief="flat"
        )
        self.pack(
            side=LEFT,
            anchor="n",
            fill="both",
            expand=True
        )