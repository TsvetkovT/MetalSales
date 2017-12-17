from application import db
from sqlalchemy.ext.hybrid import hybrid_property
from flask_bcrypt import generate_password_hash


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
