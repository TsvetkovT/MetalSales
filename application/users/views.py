from flask import Blueprint, flash, render_template,url_for,redirect,g
from .forms import LoginForm
from flask import current_app as app

import logging

from flask_login import login_user, logout_user, current_user

from flask_wtf import FlaskForm
from wtforms import Form,StringField,PasswordField
from wtforms.validators import DataRequired, Length
users_blueprint = Blueprint('users',__name__,template_folder='templates')


#from application.users.models import User
from flask_bcrypt import Bcrypt



@users_blueprint.route('/login/',methods=['GET',"POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/')
    return render_template('login.html',title='Sign In',form=form,providers=app.config['OPENID_PROVIDERS'])

