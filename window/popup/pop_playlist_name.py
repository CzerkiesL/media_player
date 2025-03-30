import tkinter

from utility.create_playlist_File import name_is_valid

def open_playlist_name_popup(p_pistes_list, p_root):
    if len(p_pistes_list) == 0:
        return

#######################################################################################################################

    popup_name = tkinter.Toplevel()

    root_w, root_h = int(p_root.winfo_width()), int(p_root.winfo_height())
    popup_x, popup_y = 400, 200

    popup_name.title("Nom de la playlist")
    popup_name.geometry(f"{popup_x}x{popup_y}+{int(root_w / 2) + int(popup_x / 2)}+{int(root_h / 2) + int(popup_y / 2)}")
    popup_name.grab_set()
    popup_name.focus_set()

#######################################################################################################################

    question_name = tkinter.Label(popup_name, text="Donnez un nom à la playlist:")
    question_name.grid(row=0, column=0)

    name = tkinter.StringVar(popup_name)
    answer_name = tkinter.Entry(
        popup_name,
        textvariable=name
    )
    answer_name.grid(row=1, column=0)

#######################################################################################################################

    popup_name_btn_container = tkinter.Frame(popup_name)
    popup_name_btn_container.grid(row=2, column=0)

    btn_submit = tkinter.Button(
        popup_name_btn_container,
        text="créer la playlist",
        command= lambda: name_is_valid(p_pistes_list, name.get(), popup_name),
    )
    btn_submit.grid(row=0, column=0)

    btn_cancel = tkinter.Button(
        popup_name_btn_container,
        text="annuler",
        command=popup_name.destroy
    )
    btn_cancel.grid(row=0, column=1)

