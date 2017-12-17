from flask import Blueprint

users = Blueprint('users',__name__)

@users.route('/me')
def me():
    return 'My page under users', 200