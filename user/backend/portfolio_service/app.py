from flask import Flask, jsonify

app = Flask(__name__)

projects = [
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

@app.route('/projects', methods=['GET'])
def get_projects():
    return jsonify(projects)

if __name__ == '__main__':
    app.run(port=5004, debug=True)
