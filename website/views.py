from flask import Blueprint, render_template

views = Blueprint('views', __name__)

# home
@views.route('/')
def home():
    return "Reserve movies here"
