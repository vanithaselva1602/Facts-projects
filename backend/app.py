from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

facts = [
    {"id": 1, "fact": "The sun is a star"},
    {"id": 2, "fact": "Water boils at 100°C"},
    {"id": 3, "fact": "Earth has one moon"}
]

@app.route("/")
def home():
    return "Backend is running!"

@app.route("/api/facts", methods=["GET"])
def get_facts():
    return jsonify(facts)

if __name__ == "__main__":
    app.run(debug=True)