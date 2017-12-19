from flask import render_template,request
from application import app


#define routes
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        return render_template('login.html')
        pass
    else:
        return render_template('login.html')
        pass


@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return  render_template('about.html')

# @app.route('/categories')
# def products():
#     # configure MySQL cursor
#     myCursor = mysql.connection.cursor()
#
#     # retreiving data from database
#     myCursor.execute('''SELECT * FROM trade.wp_grupa''')
#     category = myCursor.fetchall()
#
#     return render_template('categories.html', data = category)


#error handler

@app.errorhandler(404)
def error404(error):
    return render_template('404.html'), 404
