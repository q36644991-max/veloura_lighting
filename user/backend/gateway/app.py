from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

SERVICES = {
    'auth': 'http://localhost:5001',
    'product': 'http://localhost:5002',
    'booking': 'http://localhost:5003',
    'portfolio': 'http://localhost:5004',
    'email': 'http://localhost:5005',
}

@app.route('/api/<service>/<path:path>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def gateway(service, path):
    if service not in SERVICES:
        return jsonify({"error": "Service not found"}), 404
    
    url = f"{SERVICES[service]}/{path}"
    resp = requests.request(
        method=request.method,
        url=url,
        headers={k: v for k, v in request.headers if k != 'Host'},
        data=request.get_data(),
        cookies=request.cookies,
        allow_redirects=False,
        params=request.args
    )
    
    excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
    headers = [(name, value) for (name, value) in resp.raw.headers.items()
               if name.lower() not in excluded_headers]
    
    return (resp.content, resp.status_code, headers)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
