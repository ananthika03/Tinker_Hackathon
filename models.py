from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# --- USER ROLES ---
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    # New: Distinguish between customer and business provider
    role = db.Column(db.String(20), default="customer") # 'customer' or 'provider'
    email = db.Column(db.String(120), unique=True)

# --- VENUE MODEL (Already exists, keeping same) ---
class Venue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50)) 
    location = db.Column(db.String(100))
    capacity = db.Column(db.Integer)
    price = db.Column(db.Float) 
    contact = db.Column(db.String(50))
    image_url = db.Column(db.String(500))
    # New: Link venue to the provider who owns it
    provider_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Venue {self.name}>'

# --- PROFESSIONAL SERVICES (Gourmet, Architecture, Visual) ---
class ProfessionalService(db.Model):
    """ Consolidated model for Gourmet (Catering), Architecture, and Visual sections """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    # service_type will be: 'Catering', 'Architecture', or 'Visual'
    service_type = db.Column(db.String(50), nullable=False) 
    price_info = db.Column(db.String(100)) 
    location = db.Column(db.String(100))
    contact = db.Column(db.String(50))
    image_url = db.Column(db.String(500))
    provider_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Service {self.name} ({self.service_type})>'

# --- UNIFIED BOOKING SYSTEM ---
class Booking(db.Model):
    """ Saves user bookings for either a Venue or a Professional Service """
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    # Can link to a Venue ID OR a Service ID
    venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'), nullable=True)
    service_id = db.Column(db.Integer, db.ForeignKey('professional_service.id'), nullable=True)
    
    booking_date = db.Column(db.String(50))
    status = db.Column(db.String(20), default="Pending") # Pending, Confirmed, Cancelled