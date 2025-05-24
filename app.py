from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Replace the URL below with your actual connection string
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:yourPassword@db.xxxxxx.supabase.co:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Example student model
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    attendance = db.Column(db.Integer)

@app.route('/')
def home():
    return "Student Attendance DB is live 🎓"

@app.route('/add', methods=['POST'])
def add_student():
    data = request.get_json()
    new_student = Student(name=data['name'], attendance=data['attendance'])
    db.session.add(new_student)
    db.session.commit()
    return jsonify({"message": "Student added successfully!"})

@app.route('/students')
def get_students():
    students = Student.query.all()
    return jsonify([{"id": s.id, "name": s.name, "attendance": s.attendance} for s in students])

if __name__ == '__main__':
    app.run(debug=True)
