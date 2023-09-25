"""
given a list of actors and a dictionary of movies, write the function find_movies (sig. list, dict -> list[str])
that accepts the list of actors and the movies as arugments and returns a list of movies that both actors cast in together.
"""


def find_movies(actors_dict, movies):
    retval = []
    actors_list = []
    for items in actors_dict:
        actors_list.append(items['name'])

    for (movie, info) in movies:
        cast = info['cast']
        if

