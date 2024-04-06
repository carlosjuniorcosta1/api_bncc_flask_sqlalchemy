from flask_sqlalchemy import SQLAlchemy
from config.config import db 
from models.lecture import Lecture
from models.bncc_guide import BnccGuide
from flask import Blueprint, jsonify, request

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
    bncc_id = data_lec.get("bncc_id")
    bncc_ref = BnccGuide.query.get(bncc_id)
    print(bncc_ref)
    new_lec = Lecture(lecture_description=lec_desc, lecture_date= lec_date ,
                      subject_id=subject_id, bimester_id=bimester_id,
                        group_id=group_id, bncc_id=bncc_id)
    
    db.session.add(new_lec)
    new_lec_json = new_lec.to_json()
    return jsonify(message="Lecture added", data=new_lec_json), 201
    