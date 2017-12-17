import datetime
from application import db
from sqlalchemy.ext.hybrid import hybrid_property
from flask_bcrypt import generate_password_hash


class users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String(255), unique=True)
    user_login = db.Column(db.String(60))
    user_pass = db.Column(db.String(300), nullable=False)
    created_on = db.Column(db.DATETIME,default=datetime.datetime.utcnow())

    def __repr__(self):
        return '<user {!r}>'.format(self.user_login)

    def is_authenticated(self):
        #All registered users are authenticated
        return True

    def is_active(self):
        #All users are active
        return True

    def is_anonymous(self):
        #check is user authenticated
        return False

    def get_id(self):
        #getting users id as Unicode
        return (self.id)

    @hybrid_property
    def password(self):
        return self.user_pass;

    @password.setter
    def password(self,user_pass):
        self.user_pass = generate_password_hash(user_pass)
