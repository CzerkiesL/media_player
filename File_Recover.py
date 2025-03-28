import tkinter as tk
from tkinter import filedialog
import mimetypes
import os
from tinytag import TinyTag

from classname.Music import Music

music_list = list()


def browse_file(P_frame):
    file_list = filedialog.askdirectory(initialdir="/", title="selectionner un dossier")
    check_all_files(file_list, P_frame)

#######################################################################################################################

def check_all_files(P_dir_path, P_frame):
    for path, dirs, files in os.walk(P_dir_path):
        for file in files:
            if mimetypes.guess_type(file)[0].startswith("audio/"):
                music_path = f"{"/".join(path.split("\\"))}/{file}"

                try:
                    tag = TinyTag.get(music_path)
                    music = Music(tag.title, tag.artist, tag.genre, tag.duration, music_path)
                    music_list.append(music)

                except Exception as e:
                    print(f"Erreur lors de l'extraction des metadonnées : {e}")

    music_checkboxes = create_music_checkbox(P_frame, music_list)

#######################################################################################################################

def create_music_checkbox(P_frame, P_music_list):
    music_checkboxes = []

    for i in range(len(P_music_list)):
        checked = tk.StringVar()
        checkbox = tk.Checkbutton(
            P_frame,
            text=P_music_list[i].get_title(),
            variable=checked,
            command=lambda music=P_music_list[i],  var=checked: set_playlist(music, var),
        )
        checkbox.pack()
        checkbox.select()
        music_checkboxes.append(checked)
    return music_checkboxes

#######################################################################################################################

def set_playlist(P_music, P_checked):
    if P_checked.get() == "1":
        music_list.append(P_music)
    else:
        music_list.pop(music_list.index(P_music))
