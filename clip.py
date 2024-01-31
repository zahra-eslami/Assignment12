from media import Media

class Clip(Media):
    def __init__(self, type,name, director, imdb_score, url, duration, casts, category):
        super().__init__(type,name, director, imdb_score, url, duration, casts)
        self.category = category
