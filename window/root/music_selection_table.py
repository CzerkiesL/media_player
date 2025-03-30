import tkinter as tk
from utility.file_recover import *


def create_music_checkbox(p_frame, p_music_list):
    music_checkboxes = []

    for i in range(len(p_music_list)):
        checked = tk.StringVar()
        checkbox = tk.Checkbutton(
            p_frame,
            text=p_music_list[i].get_title(),
            variable=checked,
            command=lambda music=p_music_list[i],  var=checked: set_playlist(music, var),
        )
        checkbox.pack()
        checkbox.select()
        music_checkboxes.append(checked)
    return music_checkboxes