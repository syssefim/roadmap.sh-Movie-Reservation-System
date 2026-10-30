from flask import Blueprint

movies = Blueprint('movies', __name__)


@movies.route('/')
@movies.route('/movies')
def list_movies():
    return "hi"
