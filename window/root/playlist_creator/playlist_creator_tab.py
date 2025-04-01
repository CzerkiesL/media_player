from tkinter import *
import tkinter as tk

from window.style import style
from window.component.btn_component import create_btn
from utility.file_recover import browse_file
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
    # create_filter_container(left_side_container,music_list, p_root)

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
    create_btn(btn_container, "créer la playlist", RIGHT, print, "ok")

# open_playlist_name_popup,music_list, p_root

def create_filter_container(p_frame, p_music_list, p_root):

    tab_filter_genre = set()
    tab_filter_artist = set()
    for music in p_music_list:
        tab_filter_genre.add(music.get_genre())
        tab_filter_artist.add(music.get_artist())
    for value in tab_filter_genre:
        create_btn(p_frame, value, LEFT, print(), "hello")
    for value in tab_filter_artist:
        create_btn(p_frame, value, RIGHT, print(), "hello")
    tab_filter_artist.clear()
    tab_filter_genre.clear()
    p_music_list.clear()

    #recupere les diferent filtre et afficher les boutons

    p_root.after(1000, create_filter_container, p_frame, p_music_list, p_root)
