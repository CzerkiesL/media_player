class Music:
    def __init__(self, title, artist, genre, duration, path):
        self.title = title
        self.artist = artist
        self.genre = genre
        self.duration = duration
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