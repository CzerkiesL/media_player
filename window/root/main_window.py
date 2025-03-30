from tkinter import *
import tkinter as tk

from utility.file_recover import *
from window.popup.pop_playlist_name import open_playlist_name_popup

root = Tk()
root.configure(
    background="#3c3c3c",
    padx=40,
    pady=40)
root.geometry("1920x1080")

btn_container = Frame(
    root,
    bg="red",
    height=1000,
    width=500,
    borderwidth=15
)
btn_container.pack(
    side=LEFT,
    anchor="n"
)

list_container = Frame(
    root,
    bg="blue",
    borderwidth=15
)
list_container.pack(
    side=LEFT,
    anchor="n"
)

btn_browse = tk.Button(
    btn_container,
    text="parcourir",
    command= lambda: browse_file(list_container)
)
btn_browse.grid(row=0, column=0)

btn_create_playlist = tk.Button(
    btn_container,
    text="creer la playlist",
    command= lambda: open_playlist_name_popup(music_list, root)
)
btn_create_playlist.grid(column=0, row=1)

