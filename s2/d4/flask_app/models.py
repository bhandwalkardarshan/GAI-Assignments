from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)  # Store hashed passwords

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), unique=True)
    # Add other profile fields as needed, e.g., full name, bio, etc.

    user = db.relationship('User', backref=db.backref('profile', uselist=False))

    def __init__(self, user_id):
        self.user_id = user_id
