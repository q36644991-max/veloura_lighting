from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock data for initial development
products = [
    {"id": 1, "name": "Grand Chandelier", "category": "Chandeliers", "price": 5000, "image_url": "collection-1.png"},
    {"id": 2, "name": "Modern Pendant", "category": "Pendant Lights", "price": 1200, "image_url": "collection-2.png"},
    {"id": 3, "name": "Smart Ambient System", "category": "Smart Lighting", "price": 3000, "image_url": "collection-3.png"},
]

@app.route('/products', methods=['GET'])
def get_products():
    category = request.args.get('category')
    if category:
        filtered = [p for p in products if p['category'] == category]
        return jsonify(filtered)
    return jsonify(products)

@app.route('/products', methods=['POST'])
def add_product():
    new_product = request.json
    products.append(new_product)
    return jsonify(new_product), 201

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        return jsonify(product)
    return jsonify({"message": "Product not found"}), 404

if __name__ == '__main__':
    app.run(port=5002, debug=True)
