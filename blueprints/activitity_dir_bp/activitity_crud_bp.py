from flask_sqlalchemy import SQLAlchemy
from config.config import db 
from flask import request, jsonify, Blueprint
from models.activity import Activity
from models.student import Student
from datetime import datetime 

act_crud_bp = Blueprint("act_crud_bp", __name__)

@act_crud_bp.route('/atividades', methods= ['GET'])
def get_all_act():
    acts = Activity.query.all()
    if acts:
        acts_json = [x.to_json() for x in acts]
        return jsonify(message="All activities requested", data=acts_json), 200
    else:
        return jsonify(message="No activities found"), 404


@act_crud_bp.route('/atividade/<int:act_id>', methods=["GET"])
def get_act(act_id):
    act = Activity.query.get(act_id)
    if act:
        act_json = act.to_json()
        group_id = act_json['group_id']
        students = Student.query.filter_by(group_id=group_id).with_entities(Student.student_id, Student.full_name).all()
        students_data = [{'student_id': x.student_id, 'name': x.full_name} for x in students]
        act_json['students'] = students_data
        return jsonify(message="teste", data= act_json), 200


@act_crud_bp.route('/atividade', methods=["POST"])
def add_act():
    data_act = request.get_json()
    act_id = data_act.get('act_id')
    act_date = data_act.get('act_date')
    act_date_form = datetime.strptime(act_date, "%d/%m/%Y")
    act_description = data_act.get('act_description')
    total_act = data_act.get('total_act')
    act_status = data_act.get('act_status')
    group_id = data_act.get('group_id')
    subject_id = data_act.get('subject_id')
    bimester_id = data_act.get('bimester_id')
    mandatory_fields = ['act_description', 'total_act']
    missing_fields = [x for x in mandatory_fields if x not in data_act]
    if missing_fields:
        return jsonify(message=f" You have to provide the {', '.join(missing_fields)} field"), 400
    new_act = Activity(act_date=act_date_form.strftime("%Y/%m/%d"), act_description=act_description,
                       total_act=total_act, act_status=act_status, group_id=group_id,
                       subject_id=subject_id, bimester_id=bimester_id)
    if new_act:
        db.session.add(new_act)
        db.session.commit()
        new_act_json = new_act.to_json()
        return jsonify(message="New activity added", data=new_act_json), 201
    
@act_crud_bp.route('/atividade', methods=["PUT"])
def update_act():
    data_act = request.get_json()
    act_id = data_act.get('act_id')
    if "act_id" not in data_act:
        return jsonify(message="You need to provide and act_id to update an activity"), 400
    else:
        updated_act = Activity.query.get(act_id)
    if updated_act:
        for key, value in data_act.items():
            if key != "act_id" and key != "act_date":
                setattr(updated_act, key, value)
    if "act_date" in data_act:
        act_date = data_act.get('act_date')
        act_date_form = datetime.strptime(act_date, "%d/%m/%Y")
        updated_act.act_date = act_date_form.strftime("%Y/%m/%d")    
    db.session.commit()
    return jsonify(message="Actitivy updated", data=updated_act.to_json()), 200

@act_crud_bp.route('/atividade', methods=["DELETE"])
def delete_act():
    data_act = request.get_json()
    if "act_id" not in data_act:
        return jsonify(message="You have to provide an act_id to delete an activity")
    else:
        act_id = data_act.get('act_id')    
    act_to_delete = Activity.query.get(act_id)    
    if not act_to_delete:
        return jsonify(message="Activity not found"), 404
    else:
        act_to_delete_json = act_to_delete.to_json()
        db.session.delete(act_to_delete)
        db.session.commit()
        return jsonify(message="Activity deleted", data=act_to_delete_json), 200
    
    
    
    
              