from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/sign-in')
def sign_in():
    return "<p>Sign-in</p>"

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up')
def sign_up():
    return "<p>Sign-up</p>"