from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/send-email', methods=['POST'])
def send_email():
    data = request.json
    recipient = data.get('to')
    subject = data.get('subject')
    body = data.get('body')
    
    # Placeholder for actual email sending logic (e.g., SendGrid, Mailgun)
    print(f"Sending email to {recipient} with subject: {subject}")
    
    return jsonify({"message": "Email sent successfully"}), 200

if __name__ == '__main__':
    app.run(port=5005, debug=True)
