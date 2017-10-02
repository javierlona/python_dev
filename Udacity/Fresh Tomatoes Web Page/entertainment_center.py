#!/usr/bin/python3.5
# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

import media
import fresh_tomatoes

# Creating my instances
rambo_2 = media.Movie('Rambo 2',
                      'http://www.crankycritic.com/archive/posters/rambo2_2.jpg',
                      'https://www.youtube.com/watch?v=WQGJAIYtWD4')

terminator_2 = media.Movie('Terminator 2',
                           'https://upload.wikimedia.org/wikipedia/en/8/85/Terminator2poster.jpg',
                           'https://www.youtube.com/watch?v=7QXDPzx71jQ')

dumb_and_dumber = media.Movie('Dumb and Dumber',
                              'http://static.rogerebert.com/uploads/movie/movie_poster/dumb-and-dumber-1994/large_st4P2TtPrAfNwu8HLXoPsPPii42.jpg',
                              'https://www.youtube.com/watch?v=l13yPhimE3o')

rocky_4 = media.Movie('Rocky 4',
                      'https://www.movieposter.com/posters/archive/main/67/MPW-33838',
                      'https://www.youtube.com/watch?v=bwJJkeOTT6Y')

# My list of movies
movies = [rambo_2, terminator_2, dumb_and_dumber, rocky_4]

# Creates the HTML file
fresh_tomatoes.open_movies_page(movies)
