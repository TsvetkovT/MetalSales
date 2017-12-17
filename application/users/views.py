from flask import Blueprint
from wtforms import Form, StringField, PasswordField
from wtforms.validators import DataRequired, Length


users = Blueprint('users',__name__,template_folder='templates')


class LoginForm(Form):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired(), Length(min=6)])


@users.route('/me')
def me():
    return 'My page under users', 200