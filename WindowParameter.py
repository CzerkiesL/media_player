from tkinter import *
from tkinter import ttk

from Create_Playlist_File import *
from File_Recover import *

root = Tk()

root.configure(background="#3c3c3c", padx=200, pady=100)

frame = Frame(root, bg="red", height=200, width=200, borderwidth=30)
frame.pack()

frame.grid(row=3, column=3)

root.geometry("600x600")

ttk.Button(frame, text="parcourir", command= lambda: browse_file(frame)).grid(column=0, row=0)
ttk.Button(frame, text="creer la playlist", command= lambda: creer_playlist_m3u("ma_playlist.m3u", music_path_list)).grid(column=0, row=1)
