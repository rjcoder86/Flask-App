from flask import Blueprint, jsonify, request
from .models import Student
from .db import db

main = Blueprint('main', __name__)

@main.route('/')
def hello_world():
    return '<h1>Hello world </h1>'


@main.route("/students", methods=["GET"])
def get_students():
    students = Student.query.all()
    students_data = [{"id": student.id, "name": student.name, "standard": student.standard} for student in students]
    return jsonify(students_data)


@main.route("/add_student", methods=["POST"])
def create_student():
    data = request.get_json()
    name = data.get('name')
    standard = data.get('standard')

    if not name or not standard :
        return jsonify({"error":"Name and standard required"}) , 400
    
    new_student = Student(name=name, standard=standard)

    db.session.add(new_student)
    db.session.commit()

    return jsonify({
        "id": new_student.id,
        "name": new_student.name,
        "standard": new_student.standard
    }), 201













