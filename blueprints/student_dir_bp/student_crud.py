from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint, jsonify, request
from models.student import Student
from config.config import db 
from datetime import datetime 

student_bp = Blueprint("student_bp", __name__)

student_bp.route('/alunos', methods=["GET"])
def listar_Students():
    Students = Student.query.all()
    Students_lista_js =  Student.to_json_list(Students)
    return jsonify(data= Students_lista_js, message="Lista de Students")

student_bp.route('/aluno/<int:student_id>', methods=['GET'])
def listar_Student_url(student_id):
    Student = Student.query.get(student_id)
    Student_js = Student.to_json()
    return jsonify(data=Student_js, message="Student pela url")

student_bp.route('/aluno', methods=["GET", "PUT"])
def atualizar_Student():
    updated_data = request.get_json()
    student_id = updated_data['student_id']
    student = Student.query.filter_by(student_id=student_id).first()
    for key, value in updated_data.items():
        if key != "student_id":
            setattr(student, key, value)
    db.session.commit()
    return jsonify(message= f"Student {Student.to_json()} atualizado")

student_bp.route('/aluno', methods=["POST"])
def cria_Student():
    student_data = request.get_json()
    name = student_data['name']
    surname = student_data['surname']
    grade = student_data['grade']
    date_birth = student_data['date_birth']
    group_id = student_data['group_id']
    new_student = Student(name=name, surname=surname, 
                       grade=grade, date_birth=date_birth,
                       group_id=group_id)
    db.session.add(new_student)
    db.session.commit()
    return jsonify(message=f"Student {new_student} adicionado", data=new_student.to_json())

    












    
        


