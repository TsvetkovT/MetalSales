import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#define flask app:
app = Flask(__name__)
'''config database'''
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Bene1979@127.0.0.1/trade'
db = SQLAlchemy(app)
'''config secret key'''
app.secret_key = os.urandom(24)
'''app main models and views'''
import application.models
import application.views

#config users blueprint app and flask_login:
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from application.users.views import users
from application.users import models as user_models
app.register_blueprint(users, url_prefix ='/users')


#Config Login Manager:
login_manager = LoginManager()
login_manager.init_app(app)
'''here we declare var with the same name as ext'''
flask_bcrypt = Bcrypt(app)

'''flask_login must know how to load a user from the db'''
@login_manager.user_loader
def load_user(user_id):
    return application.user_models.query.get(int(user_id))


