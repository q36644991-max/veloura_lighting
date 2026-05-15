import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import jwt
import datetime
from functools import wraps

app = Flask(__name__, static_folder='frontend')
CORS(app)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your_secret_key')

# --- AUTH LOGIC (from auth_service) ---
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

@app.route('/api/verify', methods=['GET'])
@token_required
def verify():
    return jsonify({'message': 'Token is valid'})

# --- MANAGEMENT LOGIC (from management_service) ---
@app.route('/api/admin/stats', methods=['GET'])
@token_required
def get_stats():
    return jsonify({
        "total_products": 124,
        "active_inquiries": 18,
        "consultations": 5,
        "portfolio_projects": 12
    })

@app.route('/api/admin/products', methods=['POST', 'PUT', 'DELETE'])
@token_required
def manage_products():
    return jsonify({"message": "Product operation successful"})

@app.route('/api/admin/bookings', methods=['GET'])
@token_required
def get_bookings():
    return jsonify([
        {"id": 1, "client": "John Doe", "type": "Luxury Villa", "status": "Pending", "date": "2026-05-14"},
        {"id": 2, "client": "Sarah Smith", "type": "Hotel Lobby", "status": "Confirmed", "date": "2026-05-12"}
    ])

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
