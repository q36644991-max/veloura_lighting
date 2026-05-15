import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__, static_folder='frontend')
CORS(app)

# --- MOCK DATA (Consolidated from services) ---
products_db = [
    {"id": 1, "name": "Grand Chandelier", "category": "Chandeliers", "price": 5000, "image_url": "collection-1.png"},
    {"id": 2, "name": "Modern Pendant", "category": "Pendant Lights", "price": 1200, "image_url": "collection-2.png"},
    {"id": 3, "name": "Smart Ambient System", "category": "Smart Lighting", "price": 3000, "image_url": "collection-3.png"},
]

projects_db = [
    {
        "id": 1,
        "title": "Royal Palm Villa",
        "category": "Villas",
        "description": "Full interior lighting design for a 7-bedroom luxury villa in Palm Jumeirah.",
        "images": ["detail-2.png"]
    },
    {
        "id": 2,
        "title": "Emerald Hotel Lobby",
        "category": "Hotels",
        "description": "Custom chandelier installation and ambient lighting for the main lobby.",
        "images": ["collection-1.png"]
    }
]

bookings_db = []

# --- PRODUCT SERVICE ROUTES ---
@app.route('/api/product/products', methods=['GET'])
def get_products():
    category = request.args.get('category')
    if category:
        filtered = [p for p in products_db if p['category'] == category]
        return jsonify(filtered)
    return jsonify(products_db)

@app.route('/api/product/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((p for p in products_db if p['id'] == product_id), None)
    if product:
        return jsonify(product)
    return jsonify({"message": "Product not found"}), 404

# --- BOOKING SERVICE ROUTES ---
@app.route('/api/booking/bookings', methods=['POST'])
def create_booking():
    booking = request.json
    bookings_db.append(booking)
    return jsonify({"message": "Booking received", "data": booking}), 201

# --- PORTFOLIO SERVICE ROUTES ---
@app.route('/api/portfolio/projects', methods=['GET'])
def get_projects():
    return jsonify(projects_db)

# --- EMAIL SERVICE ROUTES ---
@app.route('/api/email/send-email', methods=['POST'])
def send_email():
    data = request.json
    recipient = data.get('to')
    print(f"Sending email to {recipient}")
    return jsonify({"message": "Email sent successfully"}), 200

# --- STATIC FILES ---
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_frontend(path):
    if path != "" and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=port)
