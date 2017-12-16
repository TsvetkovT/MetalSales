from flask import Flask, render_template, flash, redirect, url_for, session, logging
from data import Categories
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import synonym
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from flask_bcrypt import generate_password_hash
import os


#define flask app
app = Flask(__name__)
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
#app.config['secret key'] = '1q2w3e4r'
db = SQLAlchemy(app)

admin = Admin(app)

class wp_users(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    user_login = db.Column(db.String(60))
    user_pass = db.Column(db.String(300), nullable=False)
    user_nicename = db.Column(db.String(50))
    user_email = db.Column(db.String(100))
    user_url = db.Column(db.String(100))
    user_registered = db.Column(db.DATETIME(timezone=False))
    user_activation_key = db.Column(db.String(60))
    user_status = db.Column(db.Integer)
    display_name = db.Column(db.String(250))

class users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_login = db.Column(db.String(60))
    user_pass = db.Column(db.String(300), nullable=False)

    @hybrid_property
    def password(self):
        return self.user_pass;


    @password.setter
    def password(self,user_pass):
        self.user_pass = generate_password_hash(user_pass)


admin.add_view(ModelView(users, db.session))



#init MySQL
mysql = MySQL(app)





#define data
Categories = Categories()





#define routes
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return  render_template('about.html')

@app.route('/categories')
def products():
    # configure MySQL cursor
    myCursor = mysql.connection.cursor()

    # retreiving data from database
    myCursor.execute('''SELECT * FROM trade.wp_grupa''')
    category = myCursor.fetchall()

    return render_template('categories.html', data = category)


#error handler

@app.errorhandler(404)
def error404(error):
    return render_template('404.html'), 404

#running app parameters
if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0')