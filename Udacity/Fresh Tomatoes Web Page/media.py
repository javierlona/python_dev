# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define the class Movie. You could do this
# directly in entertainment_center.py but many developers keep their
# class definitions separate from the rest of their code. This also
# gives you practice importing Python files.

import webbrowser

class Movie():
    # This class provides a way to store movie related information

    def __init__(self, title, poster_image_url, trailer_youtube_url):
        """ Initialize instance of class Movie
        Args:
            param1 (str): the title of the film
            param2 (str): poster image url for the film
            param3 (str): Youtube Trailer URL for the film
        """
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    # Accessor Methods
    def title(self):
        """ Returns: the title of the film """
        return self.title

    def get_poster_image_url(self):
        """ Returns: the Poster Image URL for the film """
        return self.poster_image_url

    def trailer_youtube_url(self):
        """ Returns: the YouTube trailer URL for the film """
        return self.trailer_youtube_url
