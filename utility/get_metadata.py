from types import NoneType

from tinytag import TinyTag
import mimetypes

from classname.Music import Music

music_list = list()

def get_metadata(p_path, p_file):
    mimetype = mimetypes.guess_type(p_file)[0]
    if type(mimetype) != NoneType:
        if mimetype.startswith("audio/"):
            music_path = f"{"/".join(p_path.split("\\"))}/{p_file}"

            try:
                tag = TinyTag.get(music_path)
                music = Music(tag.title, tag.artist, tag.genre, tag.duration, tag.album, tag.year, music_path)
                music_list.append(music)

            except Exception as e:
                print(f"Erreur lors de l'extraction des metadonnées : {e}")