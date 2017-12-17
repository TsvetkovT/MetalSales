from flask import Flask
from application.users.views import users

from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from sqlalchemy.orm import synonym
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt

import os


#define flask app
app = Flask(__name__)
import application.models
import application.views
app.register_blueprint(users, url_prefix ='/users')
#
app.secret_key = os.urandom(24)


#Config MySQL

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Bene1979'
app.config['MYSQL_DB'] = 'trade'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

#Config of flask-admin

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Bene1979@127.0.0.1/trade'
db = SQLAlchemy(app)


# admin = Admin(app)




# admin.add_view(ModelView(wp_users, db.session))



#init MySQL
mysql = MySQL(app)





#running app parameters
if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0')