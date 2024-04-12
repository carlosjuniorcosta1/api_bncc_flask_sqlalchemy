from flask_sqlalchemy import SQLAlchemy
from config.config import db 
from flask import Blueprint, request, jsonify
from models.bimester_now import BimesterNow

bimester_bp = Blueprint("bimester_bp", __name__)

@bimester_bp.route('/bimestres', methods=["GET"])
def get_bimester_control():
    all_bim = BimesterNow.query.all()
    all_bim_json = [x.to_json() for x in all_bim]
    return jsonify(data=all_bim_json)

@bimester_bp.route('/bimestre', methods=["POST"])
def add_bimester_control():
    bimester_data = request.get_json()
    subject_id = bimester_data.get('subject_id')
    bim_total_id = bimester_data.get('bim_total_id')
    bimester_id = bimester_data.get('bimester_id')
    group_id = bimester_data.get('group_id')
    q_new = BimesterNow.query.filter(BimesterNow.subject_id==subject_id, 
                                     BimesterNow.bimester_id == bimester_id,
                                     BimesterNow.group_id == group_id).first()
    if not q_new:
        new_bim = BimesterNow(subject_id=subject_id, bimester_id=bimester_id,
                          bim_total_id=bim_total_id, group_id=group_id)        
        db.session.add(new_bim)
        db.session.commit()
        new_bim_json = new_bim.to_json()
        return jsonify(data = new_bim_json), 200
    else:
        return jsonify(message="This bimester has already been created for this subject"), 400
    
    


