import os
from utility.wrtie_json import *

file_path_list = get_data_from_json_file(f"{"/".join(os.path.abspath(f"./data/file_path_data.json").split("\\"))}")

complete_music_list = list()
display_music_list = list()
playlist_music_list = list()

filter_genre_set = set()
filter_artist_set = set()

new_filter_genre = set()
new_filter_artist = set()