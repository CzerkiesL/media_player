from tkinter import *

from window.style import style

from window.root.playlist_creator.playlist_creator_tab import create_playlist_tab

root = Tk()
root.configure(
    background=style["root_background"],
    padx=40,
    pady=40, )
root.resizable(False, False)
root.geometry("1820x980")

create_playlist_tab(root)

