from flask import Blueprint
from .services import movies_service


movies = Blueprint('movies', __name__)


# GET Movies
@movies.route('/movies')
def list_movies():
    movies = movies_service.list_movies()
    return movies, 200

# GET Genres
@movies.route('/movies/genre/<genre>')
def list_movies_by_genre(genre):
    movies = movies_service.list_movies_by_genre(genre)
    return movies, 200


# GET Movie
@movies.route('/movies/id/<movie_id>')
def list_movie_by_id(movie_id):
    movies = movies_service.list_movies_by_id(movie_id)
    return movies, 200
    


# POST Movie (admin)


# PUT Movie (admin)


# DELETE Movie (admin)


