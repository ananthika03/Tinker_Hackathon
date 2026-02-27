from flask import Flask, render_template, request, redirect, url_for
from models import db, Venue  # Import the db and Venue model

app = Flask(__name__)

# Configure the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///event_booking.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database with the app
db.init_app(app)

# Create the database tables automatically
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('landing.html') # This matches your landing page file

# Route for the login page
@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)