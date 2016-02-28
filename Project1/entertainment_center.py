"""
entertainment_center.py is run to open the fresh tomatoes web page
with content from the create_movies_list method
"""

import media
import fresh_tomatoes


def create_movies_list():
    """
    Return a list of movies to the user. The list of movies contains
    the movie name, trailer youtube url and a url to the movie poster
    """

	#Create various movie objects
    school_of_rock = media.Movie('School of Rock', \
		'https://www.youtube.com/watch?v=3PsUJFEBC74', \
		'http://ecx.images-amazon.com/images/I/51v8TQDTF-L.jpg')

    good_will_hunting = media.Movie('Good Will Hunting', \
		'https://www.youtube.com/watch?v=PaZVjZEFkRs', \
		'http://ecx.images-amazon.com/images/I/51w2eiMErKL.jpg')

    inception = media.Movie('Inception', \
		'https://www.youtube.com/watch?v=YoHD9XEInc0', \
		'http://ecx.images-amazon.com/images/I/61Ug%2BK8o5FL.jpg')

	#Append the movie objects into a movie list
    movies = []
    movies.append(school_of_rock)
    movies.append(good_will_hunting)
    movies.append(inception)

    return movies



def main():
    """
    Collect a list of movies and then open the fresh_tomatoes page
    using the movies_list data as page content
    """

    movies_list = create_movies_list()
    fresh_tomatoes.open_movies_page(movies_list)

main()

