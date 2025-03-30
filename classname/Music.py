class Music:
    def __init__(self, title, artist, genre, duration, album, year, path):
        self.title = title
        self.artist = artist
        self.genre = genre
        self.duration = duration
        self.album = album
        self.year = year
        self.path = path

    def get_title(self):
        return self.title

    def get_artist(self):
        return self.artist

    def get_genre(self):
        return self.genre

    def get_duration(self):
        return self.duration

    def get_path(self):
        return self.path

    def set_path(self, p_new_path):
        self.path = p_new_path