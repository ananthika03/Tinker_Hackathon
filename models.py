from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Venue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50)) # e.g., 'Cultural' or 'Professional'
    location = db.Column(db.String(100))
    capacity = db.Column(db.Integer)
    price = db.Column(db.Float) # Total price or prize
    contact = db.Column(db.String(50))
    image_url = db.Column(db.String(500))

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    service_type = db.Column(db.String(50)) # e.g., 'Catering'
    price_per_head = db.Column(db.Float)
    contact = db.Column(db.String(50))