from flask import Flask, render_template, flash, redirect, url_for, session, logging
from data import Categories
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
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
app.config['secret key'] = '1q2w3e4r'
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
    #
    # def __init__(self, user_login, user_pass):
    #     self.user_login = user_login
    #     self.user_pass = sha256_crypt.hash(user_pass)
    #
    # def validate_password(self, user_pass):
    #     return sha256_crypt.verify(user_pass, self.user_pass)
    #
    # def __repr__(self):
    #     return "<User('%s','%s')>" % (self.user_login, self.user_pass[:10] + '...')


admin.add_view(ModelView(wp_users, db.session))



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
    myCursor.execute('''SELECT GrupaBG FROM trade.wp_grupa''')
    category = myCursor.fetchall()

    return render_template('categories.html', data = category)


#running app parameters
if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0')
