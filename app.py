import os
from flask import Flask, render_template, request, redirect, url_for, flash, session
from models import db, User, Venue, Service

app = Flask(__name__)

# Database Configuration
app.secret_key = 'super_secret_key_change_this_later'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'instance', 'event_booking.db')
print("DB PATH:", os.path.join(basedir, 'instance', 'event_booking.db'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)

with app.app_context():
    if not os.path.exists('instance'):
        os.makedirs('instance')
    db.create_all()

# --- ROUTES ---

@app.route('/')
def start():
    return render_template('start.html')

@app.route('/landing')
def index():
    return render_template('landing.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        role = request.form.get('role') # 'customer' or 'provider'

        # Check if email already exists
        user_exists = User.query.filter_by(email=email).first()
        if user_exists:
            flash("Email already registered. Please login.")
            return redirect(url_for('login'))

        new_user = User(username=username, email=email, password=password, role=role)
        db.session.add(new_user)
        db.session.commit()

        flash("Account created successfully! Please login.")
        return redirect(url_for('login'))

    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")
        role = request.form.get("role")

        user = User.query.filter_by(email=email, role=role).first()

        if user and user.password == password:
            session['user_id'] = user.id
            session['role'] = user.role

            if role == 'provider':
                return redirect(url_for('provider_dashboard'))
            else:
                return redirect(url_for('index'))
        else:
            flash("Invalid credentials.")
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/providerdash')
def provider_dashboard():
    if 'role' not in session or session['role'] != 'provider':
        flash("Unauthorized access.")
        return redirect(url_for('login'))
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