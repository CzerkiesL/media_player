import os
import shutil

def copy_music_file(p_music_list, p_new_dir, p_playlist_name):
    new_path = f"{p_new_dir}/music_{p_playlist_name}"
    os.makedirs(new_path)
    
    for piste in p_music_list:
        shutil.copy(piste.get_path(), new_path)
        end_path = f"{piste.get_path().split("/")[-1]}"
        piste.set_path(f"{new_path}/{end_path}")

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

def name_is_valid(p_pistes_list, p_name, p_popup):
    p_popup.destroy()

    if len(p_name) > 0:
        create_playlist_m3u(p_pistes_list, p_name)
    else:
        create_playlist_m3u(p_pistes_list, "playlist")

#######################################################################################################################
#######################################################################################################################
#######################################################################################################################

def create_playlist_m3u(p_pistes_list, p_playlist_name):
    try:
        new_dir = f"{"/".join(os.path.abspath(f"./playlist/{p_playlist_name}").split("\\"))}"
        copy_music_file(p_pistes_list, new_dir, p_playlist_name)
        
        with open(f"{new_dir}/{p_playlist_name}.m3u", 'w', encoding='utf-8') as f:
            f.write("#EXTM3U8\n")
            for piste in range(len(p_pistes_list)):
                f.write(
                    f"#EXTINF:{p_pistes_list[piste].get_duration()},"
                    f"{p_pistes_list[piste].get_title()}, "
                    f"{p_pistes_list[piste].get_artist()}\n "
                )
                f.write(f"{p_pistes_list[piste].get_path()}\n")

        print(f"Playlist '{p_playlist_name}' créée avec succès.")

    except Exception as e:
        print(f"Erreur lors de la création de la playlist : {e}")
