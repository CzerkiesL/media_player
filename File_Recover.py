from tkinter import filedialog
import mimetypes
import os

music_path_list = list()

def browse_file(p_frame):
    file_list = filedialog.askdirectory(initialdir="/", title="selectionner un dossier")
    check_all_files(file_list, p_frame)

def check_all_files(p_dir_path, p_frame):
    for path, dirs, files in os.walk(p_dir_path):
        for file in files:
            if mimetypes.guess_type(file)[0].startswith("audio/"):
                new_path = "/".join(path.split("\\"))
                music_path = f"{new_path}/{file}"
                music_path_list.append(music_path)
                print(music_path_list)
