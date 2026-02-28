from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(20), nullable=False)

class Venue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50))
    location = db.Column(db.String(100))
    capacity = db.Column(db.Integer)
    price = db.Column(db.Float)
    contact = db.Column(db.String(50))
    image_url = db.Column(db.String(500))

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    service_type = db.Column(db.String(50))
    price_per_head = db.Column(db.Float)
    contact = db.Column(db.String(50))