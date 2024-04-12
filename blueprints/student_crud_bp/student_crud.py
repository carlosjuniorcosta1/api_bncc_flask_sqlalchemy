from flask import Blueprint, jsonify, request
from models.student import Student
from config.config import db 
from datetime import datetime 

student_bp = Blueprint("student_bp", __name__)

@student_bp.route('/alunos', methods=["GET"])
def get_all_students():
    students = Student.query.all()
    students_js =  [x.to_json() for x in students]
    return jsonify(data= students_js, message="List of students")

@student_bp.route('/aluno/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = Student.query.get(student_id)
    student_js = student.to_json()
    return jsonify(data=student_js, message="Requested student")

@student_bp.route('/aluno', methods=["GET", "PUT"])
def update_student():
    updated_data = request.get_json()
    student_id = updated_data['student_id']
    student = Student.query.filter_by(student_id=student_id).first()
    for key, value in updated_data.items():
        if key != "student_id":
            setattr(student, key, value)
    db.session.commit()
    return jsonify(message= f"Student {Student.to_json()} updated")

@student_bp.route('/aluno', methods=["POST"])
def add_student():
    student_data = request.get_json()
    name = student_data['name']
    surname = student_data['surname']
    date_birth = student_data['date_birth']
    group_id = student_data['group_id']
    new_student = Student(name=name, surname=surname, 
                        date_birth=date_birth,
                       group_id=group_id)
    db.session.add(new_student)
    db.session.commit()
    return jsonify(message=f"Student {new_student} adicionado", data=new_student.to_json())

    
@student_bp.route('/alunos/filtrar', methods=["GET"])
def search_student():
    name = request.args.get('name')
    surname = request.args.get('surname')   
    date_birth = request.args.get('date_birth')
    date_registration = request.args.get('date_registration')
    group_id = request.args.get('group_id')
    level = request.args.get('level')
    status = request.args.get('student_status')
    if group_id and name:
        alunos_query = Student.query.filter(Student.group_id == group_id, Student.name.ilike(f"%{name}%"))

    if group_id and not name:
        alunos_query = Student.query.filter(Student.group_id == group_id)    

    if name and not surname:  
        alunos_query = Student.query.filter(Student.name.ilike(f"%{name}%"))
    if name and surname:
        alunos_query = Student.query.filter(Student.name.ilike(f"%{name}%"), Student.surname.ilike(f"%{surname}"))
    if surname and not name:
        alunos_query = Student.query.filter(Student.name.ilike(f"%{surname}%"))        
    if date_birth:
        alunos_query = Student.query.filter_by(date_birth=date_birth)
    if level:
        alunos_query = Student.query.filter(Student.level.ilike(f"%{level}%"))
    if status:
        alunos_query = Student.query.filter(Student.status_aluno==status)
    if date_registration:
        alunos_query = Student.query.filter(Student.date_registration==date_registration)
    alunos_result = alunos_query.all()
    alunos_js = [x.to_json() for x in alunos_result]
    
    return jsonify(message="Students requested", data=alunos_js)
















    
        


