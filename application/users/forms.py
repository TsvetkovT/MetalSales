from flask_wtf import FlaskForm
from wtforms import Form, StringField, validators, BooleanField,TextField,PasswordField


# class LoginForm(FlaskForm):
#     openid = StringField('openid', validators=[DataRequired()])
#     remember_me = BooleanField('remember_me', default=False)

class RegistrationForm(FlaskForm):
    display_name = StringField('', [validators.Length(min=4, max=30), validators.DataRequired('Enter your name')])
    username = StringField('', [validators.Length(min=4, max=20), validators.DataRequired('Enter your username')])
    email = StringField('', [validators.DataRequired(),validators.email(message='Invalid email')])
    password = PasswordField('', [validators.Length(min=6),
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('')



