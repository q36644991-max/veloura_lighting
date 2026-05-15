from flask import Flask, request, jsonify
import jwt
import datetime
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key' # In production, use environment variables

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

@app.route('/login', methods=['POST'])
def login():
    auth = request.authorization
    # This is a placeholder. In a real app, you'd check against Supabase or a DB.
    if auth and auth.username == 'admin' and auth.password == 'password':
        token = jwt.encode({
            'user': auth.username,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
        }, app.config['SECRET_KEY'])
        return jsonify({'token': token})

    return jsonify({'message': 'Could not verify'}), 401

@app.route('/verify', methods=['GET'])
@token_required
def verify():
    return jsonify({'message': 'Token is valid'})

if __name__ == '__main__':
    app.run(port=5001, debug=True)
