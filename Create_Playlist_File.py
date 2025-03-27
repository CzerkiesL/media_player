import tkinter

import WindowParameter as WP

def open_playlist_name_popup(P_pistes):
    if len(P_pistes) == 0:
        return

    popup_name = tkinter.Toplevel()

    root_w, root_h = int(WP.root.winfo_width()), int(WP.root.winfo_height())
    popup_x, popup_y = 400, 200

    popup_name.title("Nom de la playlist")
    popup_name.geometry(f"{popup_x}x{popup_y}+{int(root_w / 2) + int(popup_x / 2)}+{int(root_h / 2) + int(popup_y / 2)}")
    popup_name.grab_set()
    popup_name.focus_set()

    question_name = tkinter.Label(popup_name, text="Donnez un nom à la playlist:")
    question_name.grid(row=0, column=0)

    name = tkinter.StringVar()
    answer_name = tkinter.Entry(popup_name, textvariable=name)
    answer_name.grid(row=1, column=0)

    popup_name_btn_container = tkinter.Frame(popup_name)
    popup_name_btn_container.grid(row=2, column=0)

    btn_submit = tkinter.Button(popup_name_btn_container, text="creer", command= lambda: name_is_valid(P_pistes, name.get(), popup_name))
    btn_submit.grid(row=0, column=0)
    btn_cancel = tkinter.Button(popup_name_btn_container, text="annuler", command=popup_name.destroy)
    btn_cancel.grid(row=0, column=1)


#######################################################################################################################

def name_is_valid(P_pistes, P_name, P_popup):

    if len(P_name) > 0:
        create_playlist_m3u(P_pistes, P_name, P_popup)

#######################################################################################################################

def create_playlist_m3u(P_pistes, P_playlist_name, P_popup):

    P_popup.destroy()

    try:
        with open(f"{P_playlist_name}.m3u", 'w', encoding='utf-8') as f:
            f.write("#EXTM3U8\n")
            for piste in P_pistes:
                f.write(f"#EXTINF:-1,{piste.split('/')[-1]}\n")
                f.write(f"{piste}\n")
        print(f"Playlist '{P_playlist_name}' créée avec succès.")
    except Exception as e:
        print(f"Erreur lors de la création de la playlist : {e}")
