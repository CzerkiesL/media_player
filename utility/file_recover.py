from tkinter import filedialog
from types import NoneType
from tinytag import TinyTag
import mimetypes
import os
import asyncio

from classname.Music import Music
from variable.global_var import *
from utility.wrtie_json import *
from window.root.playlist_creator.music_selection_table import create_music_checkbox

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

def browse_file():
    file_list = filedialog.askdirectory(initialdir="/", title="selectionner un dossier")
    check_all_files(file_list)

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

def check_all_files(p_dir_path):
    browse_music_list = list()
    for path, dirs, files in os.walk(p_dir_path):
        for file in files:
            mimetype = mimetypes.guess_type(file)[0]
            if type(mimetype) != NoneType:
                if mimetype.startswith("audio/"):
                    browse_music_list.append(f"{"/".join(path.split("\\"))}/{file}")
    browse_music_list = check_unique_file(browse_music_list, file_path_list)
    asyncio.run(write_on_json_file(f"{"/".join(os.path.abspath(f"./data/file_path_data.json").split("\\"))}", file_path_list))
    get_metadata(browse_music_list)

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

def get_metadata(p_path):
    for path in p_path:

        try:
            tag = TinyTag.get(path)
            music = Music(tag.title, tag.artist, tag.genre, tag.duration, tag.album, tag.year, path)

            create_filter(music)
            complete_music_list.append(music)
            display_music_list.append(music)

        except Exception as e:
            print(f"Erreur lors de l'extraction des metadonnées : {e}")

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

def check_unique_file(p_file_list, p_compare_file_list):
    copi_file_list = list()

    for file in p_file_list:

        try:
            test = p_compare_file_list.index(file)
        except:
            test = -1

        if test == -1:
            p_compare_file_list.append(file)
            copi_file_list.append(file)

    p_file_list.clear()
    return copi_file_list

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

def create_filter(p_music):
    if type(p_music.get_genre()) != NoneType and p_music.get_genre() not in filter_genre_set:
        new_filter_genre.add(p_music.get_genre())
        filter_genre_set.add(p_music.get_genre())

    if type(p_music.get_artist()) != NoneType and p_music.get_artist() not in filter_artist_set:
        new_filter_artist.add(p_music.get_artist())
        filter_artist_set.add(p_music.get_artist())

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

"""
def set_playlist(p_music, p_checked):
    music_checkboxes = create_music_checkbox(p_frame, music_list)
    if p_checked.get() == "1":
        music_list.append(p_music)
    else:
        music_list.pop(music_list.index(p_music))
"""
