import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import jwt
import datetime
from functools import wraps

app = Flask(__name__, static_folder='frontend')
CORS(app)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your_secret_key')

# --- MOCK DATA ---
products_db = [
    {"id": 1, "name": "Grand Chandelier", "category": "Chandeliers", "price": 5000, "stock": 12, "description": "A magnificent crystal centerpiece for luxury grand halls.", "image_url": "collection-1.png"},
    {"id": 2, "name": "Modern Pendant", "category": "Pendant Lights", "price": 1200, "stock": 45, "description": "Sleek geometric design with a matte brass finish.", "image_url": "collection-2.png"},
    {"id": 3, "name": "Smart Ambient System", "category": "Smart Lighting", "price": 3000, "stock": 8, "description": "Fully integrated RGBW architectural lighting.", "image_url": "collection-3.png"},
]

bookings_db = [
    {"id": 1, "client": "John Doe", "email": "john@example.com", "phone": "+971 50 123 4567", "type": "Luxury Villa", "status": "Pending", "date": "2026-05-14", "description": "Looking for a full lighting overhaul for our new villa in Jumeirah."},
    {"id": 2, "client": "Sarah Smith", "email": "sarah@hotel.com", "phone": "+971 4 555 0199", "type": "Hotel Lobby", "status": "Confirmed", "date": "2026-05-12", "description": "Grand lobby installation with smart controls."},
]

portfolio_db = [
    {"id": 1, "title": "The Sapphire Villa", "location": "Jumeirah, Dubai", "type": "Residential", "description": "A comprehensive lighting architecture project that seamlessly integrates smart ambient systems.", "image_url": "detail-2.png"},
    {"id": 2, "title": "Grand Meridian Lobby", "location": "Abu Dhabi", "type": "Commercial", "description": "Custom-designed crystal chandelier centerpiece balancing majesty with functionality.", "image_url": "collection-1.png"},
]

content_db = {
    "index": {
        "hero_subtitle": "Premium Lighting Design",
        "hero_title": "Illuminating Luxury Spaces",
        "hero_desc": "Experience the art of architectural lighting. We craft bespoke illumination that transforms interiors into masterpieces of warmth and elegance.",
        "story_title": "More Than Just Light",
        "story_desc": "At Veloura, we believe lighting is the soul of an interior. It defines the mood, highlights the architecture, and creates an emotional connection to the space.",
    },
    "about": {
        "hero_title": "Crafting Light, Defining Space",
        "hero_desc": "Veloura Lighting was born from a passion for architectural elegance and the transformative power of light.",
        "vision_title": "Our Vision",
        "vision_desc": "To be the global benchmark for luxury architectural lighting, where technical innovation meets artistic mastery.",
        "legacy_title": "Our Legacy",
        "legacy_desc": "We believe that light is the most important element of interior design. It has the power to elevate architecture.",
    },
    "contact": {
        "hero_title": "Get in Touch",
        "hero_desc": "Speak with our lighting consultants to bring your vision to life.",
        "form_title": "Send an Inquiry",
    },
    "portfolio": {
        "hero_title": "Our Masterpieces",
        "hero_desc": "Witness the transformation of spaces through the art of lighting design.",
    },
    "booking": {
        "hero_title": "Reserve a Consultation",
        "hero_desc": "Experience a personalized lighting design session with our expert team.",
    },
    "collections": {
        "hero_title": "Exquisite Collections",
        "hero_desc": "Browse our curated selection of premium lighting fixtures.",
    },
    "global": {
        "contact_address": "123 Luxury Lane, Dubai, UAE",
        "contact_email": "concierge@veloura.lighting",
        "contact_phone": "+971 4 000 0000"
    }
}

# --- AUTH LOGIC ---
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        try:
            jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        except:
            return jsonify({'message': 'Token is invalid!'}), 401
        return f(*args, **kwargs)
    return decorated

@app.route('/api/login', methods=['POST'])
def login():
    auth = request.authorization
    if auth and auth.username == 'admin' and auth.password == 'password':
        token = jwt.encode({
            'user': auth.username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
        }, app.config['SECRET_KEY'])
        return jsonify({'token': token})
    return jsonify({'message': 'Could not verify'}), 401

# --- ADMIN API ---
@app.route('/api/admin/stats', methods=['GET'])
@token_required
def get_stats():
    return jsonify({
        "total_products": len(products_db),
        "active_inquiries": len([b for b in bookings_db if b['status'] == 'Pending']),
        "consultations": len(bookings_db),
        "portfolio_projects": len(portfolio_db),
        "revenue": 145800,
        "growth": 12.5
    })

@app.route('/api/admin/products', methods=['GET', 'POST'])
@token_required
def manage_products():
    if request.method == 'GET': return jsonify(products_db)
    if request.method == 'POST':
        new_p = request.json
        new_p['id'] = len(products_db) + 1
        products_db.append(new_p)
        return jsonify(new_p), 201

@app.route('/api/admin/products/<int:pid>', methods=['DELETE', 'PUT'])
@token_required
def single_product(pid):
    global products_db
    if request.method == 'DELETE':
        products_db = [p for p in products_db if p['id'] != pid]
        return jsonify({"message": "Deleted"}), 200
    if request.method == 'PUT':
        data = request.json
        for p in products_db:
            if p['id'] == pid:
                p.update(data)
                return jsonify(p), 200
        return jsonify({"message": "Not found"}), 404

@app.route('/api/admin/portfolio', methods=['GET', 'POST'])
@token_required
def manage_portfolio():
    if request.method == 'GET': return jsonify(portfolio_db)
    if request.method == 'POST':
        new_proj = request.json
        new_proj['id'] = len(portfolio_db) + 1
        portfolio_db.append(new_proj)
        return jsonify(new_proj), 201

@app.route('/api/admin/portfolio/<int:pid>', methods=['DELETE', 'PUT'])
@token_required
def single_portfolio(pid):
    global portfolio_db
    if request.method == 'DELETE':
        portfolio_db = [p for p in portfolio_db if p['id'] != pid]
        return jsonify({"message": "Deleted"}), 200
    if request.method == 'PUT':
        data = request.json
        for p in portfolio_db:
            if p['id'] == pid:
                p.update(data)
                return jsonify(p), 200
        return jsonify({"message": "Not found"}), 404

@app.route('/api/admin/bookings', methods=['GET'])
@token_required
def get_bookings(): return jsonify(bookings_db)

@app.route('/api/admin/bookings/<int:bid>/status', methods=['PATCH'])
@token_required
def update_booking_status(bid):
    status = request.json.get('status')
    for b in bookings_db:
        if b['id'] == bid:
            b['status'] = status
            return jsonify(b), 200
    return jsonify({"message": "Not found"}), 404

@app.route('/api/admin/content', methods=['GET', 'PUT'])
@token_required
def manage_content():
    if request.method == 'GET': return jsonify(content_db)
    if request.method == 'PUT':
        content_db.update(request.json)
        return jsonify(content_db), 200

# --- PUBLIC API ---
@app.route('/api/content', methods=['GET'])
def get_public_content(): return jsonify(content_db)

@app.route('/api/portfolio', methods=['GET'])
def get_public_portfolio(): return jsonify(portfolio_db)

@app.route('/api/products', methods=['GET'])
def get_public_products(): return jsonify(products_db)

@app.route('/api/products/<int:pid>', methods=['GET'])
def get_public_product(pid):
    for p in products_db:
        if p['id'] == pid: return jsonify(p)
    return jsonify({"message": "Not found"}), 404

# --- STATIC FILES ---
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_frontend(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 4000))
    app.run(host='0.0.0.0', port=port)
