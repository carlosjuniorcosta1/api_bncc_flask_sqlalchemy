from flask_sqlalchemy import SQLAlchemy
from config.config import db 
from flask import request, jsonify, Blueprint
from models.activity import Activity
from models.student import Student
from datetime import datetime
from models.bimester_total import BimesterTotal
from models.bimester_now import BimesterNow

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
    if not act:
        return jsonify(message="No activity found with this id"), 404
    if act:
        act_json = act.to_json()      
        return jsonify(message="teste", data= act_json), 200

@act_crud_bp.route('/atividade', methods=["POST", "PUT"])
def add_act():
    data_act = request.get_json()
    act_date = data_act.get('act_date')
    act_date_form = datetime.strptime(act_date, "%d/%m/%Y")
    act_description = data_act.get('act_description')
    total_act = data_act.get('total_act')
    act_status = data_act.get('act_status')
    group_id = data_act.get('group_id')
    subject_id = data_act.get('subject_id')
    bimester_id = data_act.get('bimester_id')
    bim_total_id = data_act.get('bim_total_id')
    bim_now_id = data_act.get('bim_now_id')
    limit_bimester = BimesterTotal.query.filter(BimesterTotal.bim_total_id==bim_total_id)\
        .with_entities(BimesterTotal.total_bim).first()[0]
    bimester_now_obj = BimesterNow.query.filter(BimesterNow.bim_now_id==bim_now_id).first()
    total_sum_now = bimester_now_obj.bim_now_sum
    test_limit_bimester = total_act + total_sum_now
    if test_limit_bimester >= limit_bimester:
        return jsonify(message=f"Invalid value for total_act. You can distribute {limit_bimester} in this bimester and you have {limit_bimester - total_sum_now} remaining"), 400
    new_act = Activity(act_date=act_date_form.strftime("%Y/%m/%d"), 
                       act_description=act_description,
                       total_act=total_act, act_status=act_status,
                         group_id=group_id,
                       subject_id=subject_id, bimester_id=bimester_id,
                         bim_total_id=bim_total_id, bim_now_id=bim_now_id)    
    db.session.add(new_act)     
    bimester_now_obj.bim_now_sum += total_act
    db.session.commit()     
    return jsonify(message="New activity added", data=new_act.to_json()), 201
    
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
    
    
    
    
              