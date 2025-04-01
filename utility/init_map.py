from utility.file_recover import get_metadata
from variable.global_var import *
from utility.wrtie_json import *

def init_app():
    new_filter_genre.add("tous")
    new_filter_artist.add("tous")

    get_metadata(file_path_list)
