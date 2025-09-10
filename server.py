from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

events = [
    {"id": 1, "title": "Yoga in the Park"},
    {"id": 2, "title": "Lake 5K Run"}
]

# Home route
@app.route("/", methods=["GET"])
def welcome():
    return jsonify({"message": "Welcome!"}), 200

# Events routes
@app.route("/events", methods=["GET"])
def get_events():
    return jsonify(events), 200

# Add new event
@app.route("/events", methods=["POST"])
def add_event():
    if not request.is_json:
        return jsonify({"error": "Invalid input"}), 400
    data = request.get_json()
    if "title" not in data:
        return jsonify({"error": "Missing title"}), 400
    new_id = max((e["id"] for e in events), default=0) + 1
    new_event = {"id": new_id, "title": data["title"]}
    events.append(new_event)
    return jsonify(new_event), 201

if __name__ == "__main__":
    app.run(debug=True)