from app import app, db
from models import User

with app.app_context():
    # Create a customer
    user1 = User(email="test@gmail.com", password="password123", role="customer")
    # Create a provider
    user2 = User(email="provider@gmail.com", password="password123", role="provider")
    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()
    print("Test users created!")