from web_app import db
from flask_login import UserMixin
from web_app import login


@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        return '<User {}>'.format(self.username)
