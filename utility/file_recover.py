from tkinter import filedialog
import os

from utility.get_metadata import *
from window.root.music_selection_table import create_music_checkbox


def browse_file(p_frame):
    file_list = filedialog.askdirectory(initialdir="/", title="selectionner un dossier")
    check_all_files(file_list, p_frame)


#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

def check_all_files(p_dir_path, p_frame):
    for path, dirs, files in os.walk(p_dir_path):
        for file in files:
            get_metadata(path, file)
    music_checkboxes = create_music_checkbox(p_frame, music_list)

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

def set_playlist(p_music, p_checked):
    if p_checked.get() == "1":
        music_list.append(p_music)
    else:
        music_list.pop(music_list.index(p_music))
