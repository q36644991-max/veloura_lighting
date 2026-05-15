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
    {"id": 1, "name": "Grand Chandelier", "category": "Chandeliers", "price": 5000, "stock": 12},
    {"id": 2, "name": "Modern Pendant", "category": "Pendant Lights", "price": 1200, "stock": 45},
    {"id": 3, "name": "Smart Ambient System", "category": "Smart Lighting", "price": 3000, "stock": 8},
]

bookings_db = [
    {"id": 1, "client": "John Doe", "email": "john@example.com", "type": "Luxury Villa", "status": "Pending", "date": "2026-05-14"},
    {"id": 2, "client": "Sarah Smith", "email": "sarah@hotel.com", "type": "Hotel Lobby", "status": "Confirmed", "date": "2026-05-12"},
]

# --- AUTH LOGIC ---
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
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

# --- API ROUTES ---
@app.route('/api/admin/stats', methods=['GET'])
@token_required
def get_stats():
    return jsonify({
        "total_products": len(products_db),
        "active_inquiries": 18,
        "consultations": len(bookings_db),
        "portfolio_projects": 12,
        "revenue": 145800,
        "growth": 12.5
    })

@app.route('/api/admin/products', methods=['GET', 'POST'])
@token_required
def manage_products():
    if request.method == 'GET':
        return jsonify(products_db)
    
    if request.method == 'POST':
        new_product = request.json
        new_product['id'] = len(products_db) + 1
        products_db.append(new_product)
        return jsonify(new_product), 201

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

@app.route('/api/admin/bookings', methods=['GET'])
@token_required
def get_bookings():
    return jsonify(bookings_db)

@app.route('/api/admin/bookings/<int:bid>/status', methods=['PATCH'])
@token_required
def update_booking_status(bid):
    status = request.json.get('status')
    for b in bookings_db:
        if b['id'] == bid:
            b['status'] = status
            return jsonify(b), 200
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
