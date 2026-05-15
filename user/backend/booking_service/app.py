from flask import Flask, request, jsonify

app = Flask(__name__)

bookings = []

@app.route('/bookings', methods=['POST'])
def create_booking():
    booking = request.json
    bookings.append(booking)
    # Here you would typically send an email via the email-service
    return jsonify({"message": "Booking received", "data": booking}), 201

@app.route('/bookings', methods=['GET'])
def get_bookings():
    return jsonify(bookings)

if __name__ == '__main__':
    app.run(port=5003, debug=True)
