from media import Media

class Film(Media):
    def __init__(self,type, name, director, imdb_score, url, duration, casts, genre):
        super().__init__(type,name, director, imdb_score, url, duration, casts)
        self.genre = genre

# def __str__(self):
#         return f"Type: Film\nName: {self.name}\nDirector: {self.director}\nIMDB Score: {self.imdb_score}\nURL: {self.url}\nDuration: {self.duration} minutes\nGenre: {self.genre}\nCasts: {', '.join(self.casts)}"
