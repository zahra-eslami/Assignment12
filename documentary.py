from media import Media

class Documentary(Media):
    def __init__(self, type,name, director, imdb_score, url, duration, casts, topic):
        super().__init__(type,name, director, imdb_score, url, duration, casts)
        self.topic = topic
