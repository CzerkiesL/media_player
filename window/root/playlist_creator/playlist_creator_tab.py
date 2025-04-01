from tkinter import *
import tkinter as tk

from window.style import style
from window.component.btn_component import create_btn
from variable.global_var import *
from utility.file_recover import browse_file, playlist_music_list, complete_music_list
from window.popup.pop_playlist_name import open_playlist_name_popup


def create_playlist_tab(p_root):
    playlist_creator_tab = Frame(
        p_root,
        bg=style["border_color"],
        borderwidth=style["border_width"],
        relief="flat")
    playlist_creator_tab.pack(
        side=LEFT,
        anchor='nw',
        fill="both",
        expand=True
    )

    left_side_container = tk.Frame(
        playlist_creator_tab,
        bg=style["border_color"]
    )
    left_side_container.pack(
        side=LEFT,
        anchor="n",
        fill="both",
        expand=True,
        padx=(0, style["border_width"])
    )

    create_btn_container(left_side_container, p_root)
    create_filter_container(left_side_container, p_root)

    list_container = Frame(
        playlist_creator_tab,
        bg=style["frame_background"],
        borderwidth=150,
        width=1500
    )
    list_container.pack(
        side=RIGHT,
        anchor="n",
        fill="both"
    )

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

def create_btn_container(p_frame, p_root):
    btn_container = tk.Frame(
        p_frame,
        bg=style["frame_background"],
        height=500,
        borderwidth=4
    )
    btn_container.pack(
        anchor="n",
        fill="x",
        expand=True
    )
    create_btn(btn_container, "parcourir", LEFT, browse_file)
    create_btn(btn_container, "créer la playlist", RIGHT, open_playlist_name_popup,playlist_music_list, p_root)

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

def create_filter_container(p_frame, p_root):

    genre_filter_container = Frame(p_frame)
    artist_filter_container = Frame(p_frame)

    for value in new_filter_genre:
        create_btn(genre_filter_container, value, LEFT, print, "hello")
    for value in new_filter_artist:
        create_btn(artist_filter_container, value, RIGHT, print, "hello")

    new_filter_genre.clear()
    new_filter_artist.clear()

    p_root.after(100, create_filter_container, p_frame, p_root)
