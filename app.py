from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

# Replace with your actual Supabase project values
SUPABASE_URL = "https://your-project-id.supabase.co"
SUPABASE_API_KEY = "your-supabase-secret-key"
SUPABASE_TABLE = "students"

headers = {
    "apikey": SUPABASE_API_KEY,
    "Authorization": f"Bearer {SUPABASE_API_KEY}",
    "Content-Type": "application/json"
}

@app.route("/")
def home():
    return jsonify({"message": "Student Attendance DB is live 🎓"})

@app.route("/add", methods=["POST"])
def add_student():
    data = request.get_json()
    response = requests.post(
        f"{SUPABASE_URL}/rest/v1/{SUPABASE_TABLE}",
        json={
            "name": data["name"],
            "attendance": data["attendance"]
        },
        headers=headers
    )
    if response.status_code in [200, 201]:
        return jsonify({"message": "Student added successfully!"})
    else:
        return jsonify({"error": "Failed to add student", "details": response.text}), 400

@app.route("/students", methods=["GET"])
def get_students():
    response = requests.get(
        f"{SUPABASE_URL}/rest/v1/{SUPABASE_TABLE}?select=*",
        headers=headers
    )
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Failed to fetch students", "details": response.text}), 400

if __name__ == "__main__":
    app.run(debug=True)
