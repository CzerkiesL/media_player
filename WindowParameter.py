from tkinter import *

from Create_Playlist_File import *
from File_Recover import *

root = Tk()
root.configure(
    background="#3c3c3c",
    padx=20,
    pady=20)
root.geometry("1024x800")

btn_container = Frame(
    root,
    bg="red",
    height=200,
    width=200,
    borderwidth=15
)
btn_container.grid(row=0, column=0)

list_container = Frame(
    root,
    bg="blue",
    borderwidth=15
)
list_container.grid(row=0, column=1)

btn_browse = tk.Button(
    btn_container,
    text="parcourir",
    command= lambda: browse_file(list_container)
)
btn_browse.grid(row=0, column=0)

btn_create_playlist = tk.Button(
    btn_container,
    text="creer la playlist",
    command= lambda: open_playlist_name_popup(music_list)
)
btn_create_playlist.grid(column=0, row=1)

