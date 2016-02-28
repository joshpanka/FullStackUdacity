"""
media.py contains the definition of respective media classes
"""

class Movie(object):
    """
    Initializes and allows for the modification of a Movie
    Attributes:
	    movie_title (str): The title of the respective movie
        trailer_youtube_url (str): The youtube url for the given movie title
        poster_image_url (str): Any url that points to the given movie poster
    """

    def __init__(self, movie_title, trailer_youtube_url, poster_image_url):
        self.title = movie_title
        self.trailer_youtube_url = trailer_youtube_url
        self.poster_image_url = poster_image_url

    def add_movie_title(self, movie_title):
        """
    	Change or add the Movie's title
    	Attributes:
    		movie_title (str): The title of the respective movie
    	"""
        self.title = movie_title

    def add_movie_trailer_url(self, trailer_youtube_url):
        """
    	Change or add the Movie's youtube trailer url
    	Attributes:
    	    trailer_youtube_url (str): The url to the respective movie trailer
    	"""
        self.trailer_youtube_url = trailer_youtube_url

    def add_movie_poster_url(self, poster_image_url):
        """
    	Change or add the Movie's poster url
    	Attributes:
    	    poster_image_url (str): Any url that points towards
    	    the respecive Movie's poster
    	"""
        self.poster_image_url = poster_image_url
