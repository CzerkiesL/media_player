import tkinter as tk

class App(tk.Tk):
    def __init__(self, width, height, background):
        super().__init__()

        def get_column_width():
            return  width / 40

        def get_row_height():
            return height / 25

        self.configure(
            background=background,
            padx=get_column_width(),
            pady=get_row_height(),
        )
        self.title("Media Player")
        self.resizable(False, False)
        self.geometry(f"{width}x{height}")
        self.anchor("nw")