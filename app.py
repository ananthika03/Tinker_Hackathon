from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Using SQLite (Zero-install database)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///event_booking.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# --- DATABASE MODELS ---
class Venue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100))
    capacity = db.Column(db.Integer)
    price = db.Column(db.Float)
    image_url = db.Column(db.String(500))

# Initialize DB
with app.app_context():
    db.create_all()

# --- ROUTES ---
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login_choice():
    return render_template('login_choice.html')

@app.route('/api/assist', methods=['POST'])
def assist_logic():
    data = request.json
    budget = float(data.get('budget', 0))
    guests = int(data.get('guests', 0))
    
    # Simple Logic: Filter by guests, sort by price closest to budget
    matches = Venue.query.filter(Venue.capacity >= guests).all()
    recommendations = sorted(matches, key=lambda v: abs(v.price - budget))
    
    return jsonify([{"name": r.name, "price": r.price} for r in recommendations[:2]])

if __name__ == '__main__':
    app.run(debug=True)