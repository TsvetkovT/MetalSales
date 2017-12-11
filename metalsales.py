from flask import Flask, render_template, flash, redirect, url_for, session, logging
from data import Categories
from flask_mysqldb import MySQL

from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt

#define flask app
app = Flask(__name__)

#Config MySQL

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Bene1979'
app.config['MYSQL_DB'] = 'trade'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'



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
