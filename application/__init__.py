import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_openid import OpenID


#Import login manager
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

#define flask app:
app = Flask(__name__,instance_relative_config=True)
app.config.from_pyfile('config.py')
basedir = app.config['BASEDIR']

'''config database'''
db = SQLAlchemy(app)

'''app main models and views'''
from . import models, views



#Config Login Manager:
login_manager = LoginManager()
login_manager.init_app(app)
oid = OpenID(app,os.path.join(basedir,'tmp'))
'''here we declare var with the same name as ext'''
flask_bcrypt = Bcrypt(app)


'''users app main models and views'''
from .users.views import users_blueprint
from .users.models import User

#config users blueprint app:
app.register_blueprint(users_blueprint, url_prefix ='/users')

