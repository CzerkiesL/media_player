from WindowParameter import root

root.mainloop()

def creer_playlist_m3u(nom_fichier, pistes):
    """
    Crée un fichier .m3u avec la liste de pistes donnée.

    :param nom_fichier: Nom du fichier M3U à créer (ex: 'playlist.m3u')
    :param pistes: Liste de chemins vers les fichiers audio/vidéo
    """
    try:
        with open(nom_fichier, 'w', encoding='utf-8') as f:
            f.write("#EXTM3U\n")  # Entête obligatoire pour le format étendu
            for piste in pistes:
                f.write(f"#EXTINF:-1,{piste.split('/')[-1]}\n")  # Nom de la piste
                f.write(f"{piste}\n")
        print(f"Playlist '{nom_fichier}' créée avec succès.")
    except Exception as e:
        print(f"Erreur lors de la création de la playlist : {e}")

# Exemple d'utilisation
if __name__ == "__main__":
    pistes_audio = [
        "B:/Music/test/01. U2 - Vertigo (Remastered 2024).m4a",
    ]
    creer_playlist_m3u("ma_playlist.m3u", pistes_audio)