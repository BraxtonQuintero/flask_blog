from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app import db


# Create a User class that inherits from the db.Model class
# CREATE TABLE user(id SERIAL PRIMARY KEY, email VARCHAR(50) UNIQUE NOT NULL, etc.)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(50), nullable = False, unique = True)
    username = db.Column(db.String(50), nullable = False, unique = True)
    password = db.Column(db.String(256), nullable = False)
    date_created = db.Column(db.DateTime(50), nullable = False, default=datetime.utcnow)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.set_password(kwargs.get('password', ''))
        db.session.add(self)
        db.session.commit()

    def __str__(self):
        return self.username

    def set_password(self,plain_password):
        self.password = generate_password_hash(plain_password)