from flask import Blueprint

showtimes = Blueprint('showtimes', __name__)

# home
@showtimes.route('/showtimes')
def list_showtimes():
    return "<h1>Showtimes</h1>"