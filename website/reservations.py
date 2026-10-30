from flask import Blueprint

reservations = Blueprint('reservations', __name__)

# home
@reservations.route('/reservations')
def list_reservation():
    return "<h1>Reservations</h1>"