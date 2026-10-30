from flask import Blueprint
from .services import movies_service


movies = Blueprint('movies', __name__)


# GET Movies
@movies.route('/movies')
def list_movies():
    movies = movies_service.list_movies()
    return movies, 200

# GET Genres


# GET Movie


# POST Movie (admin)


# PUT Movie (admin)


# DELETE Movie (admin)


