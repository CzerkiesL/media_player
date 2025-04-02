
from classname.App import App
from utility.screen_info import get_screen
from style.style import style
from window.root.playlist_creator.playlist_creator_tab import create_playlist_tab

window_size = get_screen()
root = App(
    window_size["width"],
    window_size["height"],
    style["root_background"],
)

create_playlist_tab(root)

