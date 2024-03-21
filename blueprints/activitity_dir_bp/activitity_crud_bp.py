from flask_sqlalchemy import SQLAlchemy
from config.config import db 
from flask import request, jsonify, Blueprint
from models.activity import Activity

act_crud_bp = Blueprint("act_crud_bp", __name__)

@act_crud_bp.route('/atividades', methods= ['GET'])
def get_all_act():
    acts = Activity.query.all()
    if acts:
        acts_json = [x.to_json() for x in acts]
        return jsonify(message="All activities requested", data=acts_json), 200
    else:
        return jsonify(message="No activities found"), 404

@act_crud_bp.route('/atividades/<int:act_id>', methods=["GET"])
def get_act(act_id):
    act = Activity.query.get(act_id)
    if act:
        act_json = act.to_json()
        return jsonify(message="Requested activity"), 200
    else:
        return jsonify(message="Activity not found"), 404
    
@act_crud_bp.route('/atividade', methods=["POST"])
def add_act():
    data_act = request.get_json()
    act_id = data_act['act_id']
    act_date = data_act['act_date']
    act_description = data_act['act_description']
    total_act = data_act['total_act']
    act_status = data_act['act_status']
    group_id = data_act['group_id']
    subject_id = data_act['subject_id']
    bimester_id = data_act['bimester_id']
    mandatory_fields = ['act_id', 'act_date', 'act_description', 'total_act']
    missing_fields = [x for x in mandatory_fields if x not in data_act]
    if missing_fields:
        return jsonify(message=f" You have to provide the {', '.join(missing_fields)} field")
    new_act = Activity(act_id=act_id, act_date=act_date, act_description=act_description,
                       total_act=total_act, act_status=act_status, group_id=group_id,
                       subject_id=subject_id, bimester_id=bimester_id)
    if new_act:
        db.session.add(new_act)
        db.session.commit()
        new_act_json = new_act.to_json()
        return jsonify(message="New activity added", data=new_act_json), 200






    






