from flask_sqlalchemy import SQLAlchemy
from config.config import db 
from models.lecture import Lecture
from models.bncc_guide import BnccGuide
from models.group import Group
from flask import Blueprint, jsonify, request
import json 

lecture_bp = Blueprint("lecture_bp", __name__)

@lecture_bp.route("/aulas", methods=["GET"])
def get_all_lectures():
    all_lec = Lecture.query.all()
    all_lec_json = [x.to_json() for x in all_lec]
    return jsonify(message="All lectures", data=all_lec_json), 200

@lecture_bp.route("/aula/<int:lecture_id>", methods=["GET"])
def get_lecture(lecture_id):
    lec = Lecture.query.get(lecture_id)
    if lec:
        lec_json = lec.to_json()
        return jsonify(message="Lecture requested", data=lec_json)
    else:
        return jsonify(message="Lecture not found"), 404

@lecture_bp.route("/aula", methods=["POST"])
def add_lecture():
    data_lec = request.get_json()
    lec_desc = data_lec.get("lecture_description")
    lec_date = data_lec.get('lecture_date')
    subject_id = data_lec.get('subject_id')
    bimester_id = data_lec.get("bimester_id")
    group_id = data_lec.get("group_id")
    bncc_id = data_lec.get('bncc_id')    
    
    new_lec = Lecture(lecture_description=lec_desc, lecture_date= lec_date ,
                      subject_id=subject_id, bimester_id=bimester_id,
                        group_id=group_id, bncc_id=bncc_id)    
    db.session.add(new_lec)
    db.session.commit()
    new_lec_json = new_lec.to_json()
    return jsonify(message="Lecture added", data=new_lec_json), 201

@lecture_bp.route('/aula', methods=["DELETE"])
def delete_lecture():
    data_lec = request.get_json()
    lecture_id = data_lec.get('lecture_id')
    if not lecture_id:
        return jsonify(message="You need to provide a lecture_id in order to delete a lecture"), 400
    else:
        lec_query = Lecture.query.get(lecture_id)
    if not lec_query:
        return jsonify(message="Lecture not found"), 404
    else:
        lec_query_json = lec_query.to_json()
        db.session.delete(lec_query)
        return jsonify(message="Lecture deleted successfully", data=lec_query_json), 200
    
    
    



