import datetime

from application import db

from sqlalchemy.ext.hybrid import hybrid_property
from flask_bcrypt import generate_password_hash


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String(255),index=True,unique=True)
    user_login = db.Column(db.String(60),index=True,unique=True)
    display_name = db.Column(db.String(100), index=True, unique=True)
    user_pass = db.Column(db.String(300), nullable=False)
    created_on = db.Column(db.DATETIME,default=datetime.datetime.utcnow())
    enquiries = db.relationship('enquiry', backref='requestor',lazy='dynamic')

    def __repr__(self):
        return '<User {!r}>'.format(self.user_login)

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
        try:
            return (self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3

    @hybrid_property
    def password(self):
        return self.user_pass;

    @password.setter
    def password(self,user_pass):
        self.user_pass = generate_password_hash(user_pass)

class enquiry(db.Model):

    encID = db.Column(db.Integer,primary_key=True)
    Ime = db.Column(db.String(200),nullable=True)
    reqestor = db.Column(db.String(60), db.ForeignKey('users.id'), nullable=True)
    Kompania = db.Column(db.String(200),nullable=True)
    Telefon = db.Column(db.String(200),nullable=True)
    Email = db.Column(db.String(50),nullable=True)
    Adres = db.Column(db.String(400),nullable=True)
    Tiptransport = db.Column(db.String(400),nullable=True)
    Datad = db.Column(db.String(50),nullable=True)
    Vypros = db.Column(db.TEXT)
    Zapitvane = db.Column(db.TEXT)

    def __repr__(self):
        return '<enquiry {!r}>'.format(self.Zapitvane)