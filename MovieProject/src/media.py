from video import Video


class Movie(Video):
    def __init__(self, title, duration, poster_image_url, trailer_youtube_url):
        self.trailer_youtube_url = trailer_youtube_url
        Video.__init__(self, title, duration, poster_image_url)
        

class TvShow(Video):
    def __index__(self, title, duration, poster_image_url):
        Video.__init__(title, duration, poster_image_url)