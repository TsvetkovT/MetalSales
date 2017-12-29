from flask import Blueprint, flash,request,render_template,url_for,redirect,session,g
from flask_login import login_user,logout_user,current_user,login_required
from .forms import RegistrationForm
import datetime
from application import login_manager,db,oid
from application.users.models import User
import logging

from flask_wtf import FlaskForm
from wtforms import Form,StringField,PasswordField
from wtforms.validators import DataRequired, Length
users_blueprint = Blueprint('users',__name__,template_folder='templates')


#from application.users.models import User
from flask_bcrypt import Bcrypt

# @users_blueprint.before_request
# def before_request():
#     g.user = current_user


@users_blueprint.route('/signin/',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit() and request.method == 'POST':
        user = User(display_name=form.display_name.data,
                    user_email=form.email.data,
                    user_login=form.username.data,
                    user_pass=form.password.data,
                    created_on=datetime.datetime.now())
        db.session.add(user)
        db.session.commit()

        login_user(user)

        flash('Thank you for registering.', 'success')
        return redirect(url_for("login"))

    return render_template('testRegister.html', form=form)


@oid.after_login
def after_login(resp):
    if resp.email is None or resp.email == "":
        flash('Invalid login. Please try again.')
        return redirect(url_for('login'))
    user = User.query.filter_by(email=resp.email).first()
    if user is None:
        nickname = resp.nickname
        if nickname is None or nickname == "":
            nickname = resp.email.split('@')[0]
        user = User(nickname=nickname, email=resp.email)
        db.session.add(user)
        db.session.commit()
    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember = remember_me)
    return redirect(request.args.get('next') or url_for('index'))


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))
