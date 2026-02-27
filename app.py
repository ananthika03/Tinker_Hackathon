import os
from flask import Flask, render_template, request, redirect, url_for
from models import db, Venue, Service
from flask import session, redirect, url_for

app = Flask(__name__)

# Database Configuration
app.secret_key = 'super_secret_key_change_this_later'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'instance', 'event_booking.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    if not os.path.exists('instance'):
        os.makedirs('instance')
    db.create_all()

# --- ROUTES ---

@app.route('/')
def start():
    """The cinematic entry page."""
    return render_template('start.html')

@app.route('/landing')
def index():
    """The main customer landing page with the interactive globe."""
    return render_template('landing.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Handles role-based redirection."""
    if request.method == 'POST':
        # Capture the role from the hidden input field in login.html
        role = request.form.get('role', 'customer').lower()
        
        if role == 'provider':
            return redirect(url_for('provider_dashboard'))
        else:
            return redirect(url_for('index'))
            
    return render_template('login.html')

@app.route('/providerdash')
def provider_dashboard():
    """The service provider dashboard."""
    return render_template('providerdash.html')

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

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        return redirect(url_for('index'))
    return render_template('contact.html')
@app.route('/logout')
def logout():
   
    session.clear()
    
    return redirect(url_for('start'))
if __name__ == '__main__':
    app.run(debug=True)