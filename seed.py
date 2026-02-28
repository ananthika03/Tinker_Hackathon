from app import app
from models import db, User

with app.app_context():

    print("Users before:", User.query.count())

    # Clear old users
    User.query.delete()
    db.session.commit()

    user1 = User(
        username="testuser",
        email="test@gmail.com",
        password="password123",
        role="customer"
    )

    user2 = User(
        username="provideruser",
        email="provider@gmail.com",
        password="password123",
        role="provider"
    )

    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()

    print("Users after:", User.query.count())
    print("Test users created successfully!")