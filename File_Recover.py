import tkinter as tk
from tkinter import filedialog
import mimetypes
import os

music_path_list = list()


def browse_file(P_frame):
    file_list = filedialog.askdirectory(initialdir="/", title="selectionner un dossier")
    check_all_files(file_list, P_frame)

#######################################################################################################################

def check_all_files(P_dir_path, P_frame):
    files_list = []
    for path, dirs, files in os.walk(P_dir_path):
        for file in files:
            if mimetypes.guess_type(file)[0].startswith("audio/"):
                music_path_list.append(f"{"/".join(path.split("\\"))}/{file}")
                files_list.append(file)
    music_checkboxes = create_music_checkbox(P_frame, files_list, music_path_list)

#######################################################################################################################

def create_music_checkbox(P_frame, P_music_list, P_music_path):
    music_checkboxes = []

    for i in range(len(P_music_list)):
        checked = tk.StringVar()
        checkbox = tk.Checkbutton(
            P_frame,
            text=P_music_list[i],
            variable=checked,
            command=lambda path_value=P_music_path[i],  var=checked: set_playlist(path_value, var),
        )
        checkbox.pack()
        checkbox.select()
        music_checkboxes.append(checked)
    return music_checkboxes

#######################################################################################################################

def set_playlist(P_path_value, P_checked):
    if P_checked.get() == "1":
        music_path_list.append(P_path_value)
    else:
        music_path_list.pop(music_path_list.index(P_path_value))
