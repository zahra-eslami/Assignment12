from pytube import YouTube
from actor import Actor

class Media:
    def __init__(self, type,name, director, imdb_score, url, duration, casts):
        self.type = type
        self.name = name
        self.director = director
        self.imdb_score = imdb_score
        self.url = url
        self.duration = duration
        self.casts = casts


    # # @staticmethod
    # def show_info(movie_name):
    #     for media in Media.MEDIA:
    #         if media.name == movie_name:
    #             print(f"Name: {media.name}")
    #             print(f"Director: {media.director}")
    #             print(f"IMDB Score: {media.imdb_score}")
    #             print(f"URL: {media.url}")
    #             print(f"Duration: {media.duration} minutes")
    #             print("Casts:")
    #             for actor in media.casts:
    #                 print(f"- {actor.name}")
    #             return
    #     print("Movie not found!")

    def download(self):
        try:
            yt = YouTube(self.url)
            stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
            stream.download()
            print("Download complete!")
        except Exception as e:
            print(f"Error downloading video: {e}")