import webbrowser
class Movie():
     """A class about the information of a movie"""
     VALID_RATINGS = [ "G", "PG", "PG-13", "R"]
     def __init__(self, movie_name, movie_story_line, movie_poster_image, movie_trailer):
          self.title = movie_name
          self.story_line = movie_story_line
          self.poster = movie_poster_image
          self.trailer = movie_trailer

     def show_trailer(self):
          webbrowser.open(self.trailer)
