from flask import Blueprint, flash, render_template,url_for,redirect,g
from application import app
from .forms import LoginForm

from flask_login import login_user, logout_user, current_user

from flask_wtf import FlaskForm
from wtforms import Form,StringField,PasswordField
from wtforms.validators import DataRequired, Length
users = Blueprint('users',__name__,template_folder='templates')


from application.users.models import User
from flask_bcrypt import Bcrypt



@users.route('/login',methods=['GET',"POST"])
def login():
    form = LoginForm()
    return render_template('login.html',form=form)
