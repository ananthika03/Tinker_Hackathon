from flask import Flask, render_template, request, jsonify
from models import db, Venue, Service

app = Flask(__name__)

# SQLite configuration: No installation needed, creates a local file
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///event_booking.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Create the database and tables automatically on startup
with app.app_context():
    db.create_all()

# --- WEB PAGE ROUTES ---
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/browse')
def browse_page():
    return render_template('customer_browse.html')

# --- API ENDPOINTS (The "Brain") ---

@app.route('/api/venues', methods=['GET'])
def get_venues():
    """Returns all venues for the browsing page"""
    venues = Venue.query.all()
    return jsonify([{
        "id": v.id, "name": v.name, "location": v.location,
        "capacity": v.capacity, "price": v.price, 
        "category": v.category, "contact": v.contact
    } for v in venues])

@app.route('/api/assist', methods=['POST'])
def assist_feature():
    """Rule-based scoring for recommendations"""
    data = request.json
    budget = float(data.get('budget', 0))
    guests = int(data.get('guests', 0))
    
    # 1. Filter: Find venues that can actually hold the guest count
    matches = Venue.query.filter(Venue.capacity >= guests).all()
    
    # 2. Score: Rank by how close the price is to the user's budget
    # The 'abs()' function finds the difference; smaller is better
    recommendations = sorted(matches, key=lambda v: abs(v.price - budget))
    
    return jsonify([{
        "name": r.name, "price": r.price, "location": r.location
    } for r in recommendations[:2]]) # Return top 2

if __name__ == '__main__':
    app.run(debug=True)