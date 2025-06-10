from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Replace this with your actual Supabase connection string
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:GDakshita%2023@db.fylubgkzkgtvmkqaooth.supabase.co:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    attendance = db.Column(db.Integer)

@app.route("/")
def home():
    return "Student Attendance DB is live 🎓"

@app.route("/add", methods=["POST"])
def add_student():
    data = request.get_json()
    new_student = Student(name=data["name"], attendance=data["attendance"])
    db.session.add(new_student)
    db.session.commit()
    return jsonify({"message": "Student added successfully!"})

@app.route("/students")
def get_students():
    students = Student.query.all()
    return jsonify([{"id": s.id, "name": s.name, "attendance": s.attendance} for s in students])

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
