from flask import Flask, render_template, request, jsonify
from models import db, Venue, Service

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///event_booking.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('landing.html')

@app.route('/venues')
def venues():
    return render_template('venues.html')

@app.route('/catering')
def catering():
    return render_template('catering.html')

@app.route('/architecture')
def architecture():
    return render_template('architecture.html')

@app.route('/visual')
def visual():
    return render_template('visual.html')

@app.route('/onboarding')
def onboarding():
    return render_template('providerdash.html')

if __name__ == '__main__':
    app.run(debug=True)