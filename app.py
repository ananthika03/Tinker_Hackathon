import os
from flask import Flask, render_template, request, redirect, url_for
from models import db, Venue, Service

app = Flask(__name__)

# This line automatically creates the database file in the right place
# You don't need to install anything for this to work!
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'instance', 'event_booking.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# This part ensures the database tables are created when you start the app
with app.app_context():
    if not os.path.exists('instance'):
        os.makedirs('instance')
    db.create_all()

@app.route('/')
def index():
    return render_template('landing.html')

@app.route('/venues')
def venues():
    all_venues = Venue.query.all()
    return render_template('venues.html', venues=all_venues)

@app.route('/catering')
def catering():
    return render_template('catering.html')
@app.route('/architecture')
def architecture():
    return render_template('architecture.html')

@app.route('/visual')
def visuals():
    return render_template('visual.html')




@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # This is where you'll eventually check the username/password
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)