from flask import request, jsonify, Blueprint
from config.config import db 
from flask_sqlalchemy import SQLAlchemy 
from models.score import Score
from models.student import Student
from models.activity import Activity
from models.score_control import ScoreControll
from models.bimester_total import BimesterTotal

score_crud_bp = Blueprint("score_crud_bp", __name__)
@score_crud_bp.route('/notas', methods=["GET"])
def get_all_scores():
    scores = Score.query.all()
    if not scores:
        return jsonify(message="No scores registered yet"), 400
    scores_json = [x.to_json() for x in scores]
    return jsonify(data=scores_json, message="Requested scores"), 200

@score_crud_bp.route('/notas/<int:act_id>', methods=["GET"])
def get_act_score(act_id):
    scores = Score.query.filter(Score.act_id==act_id).all()
    if not scores:
        return jsonify(message="No scores for this activity"), 400
    scores_json = [x.to_json() for x in scores]
    return jsonify(data=scores_json, message= "Scores for this activity"), 200
    
@score_crud_bp.route('/nota', methods=["POST", "PUT"])
def add_score():
    data_score = request.get_json()
    act_id = data_score.get('act_id')
    score = data_score.get('score')
    student_id = data_score.get('student_id')
    activity = Activity.query.get(act_id)
    if not activity:
        return jsonify("No activities were found with this act_id"), 404
    group_id = activity.group_id
    bim_id = activity.bim_total_id
    list_students = Student.query.filter(Student.group_id==group_id).with_entities(Student.student_id).all()
    list_students_ids = [x[0] for x in list_students]
    if student_id not in list_students_ids:
        return jsonify(f"Invalid student_id {student_id}. This student has not been registered in this group"), 404
    total_act = activity.total_act 
    existent_score_reg = Score.query.filter(Score.act_id == act_id, Score.student_id == student_id).first()
    if not existent_score_reg:   
        if score <= total_act:
            new_score = Score(act_id=act_id, student_id=student_id, score=score)
            db.session.add(new_score)
            db.session.commit()
            new_score_id = new_score.score_id
            new_score_controll = ScoreControll(score_id=new_score_id, score_now=score)
            db.session.add(new_score_controll)
            db.session.commit()
            new_score_json = new_score.to_json()
            return jsonify(message="New score added", data=new_score_json), 201
    else:
        total_bim = BimesterTotal.query.filter(BimesterTotal.bim_total_id == bim_id).with_entities(BimesterTotal.total_bim).first()
        total_bim_value = total_bim[0]
        print(total_bim_value)
        score_id_up = existent_score_reg.score_id
        score_up = ScoreControll.query.filter(ScoreControll.score_id == score_id_up).first()
        if score_up.score_now + score <= total_bim_value:
            score_up.score_now += score
        elif score_up.score_now + score > total_bim_value:
            return jsonify(message=f"Invalid score. There is still {total_bim_value - score_up.score_now + score} remaining"), 400       
        db.session.commit()
        existent_score_reg_json = existent_score_reg.to_json()
        return  jsonify(message="Score added and updated", data= existent_score_reg_json), 201
    
@score_crud_bp.route("/nota", methods=["DELETE"])
def delete_score():
    data_score = request.get_json()
    score_id = data_score.get('score_id')
    if not score_id:
        return jsonify("You need to provide an score id in order to delete a score"), 400
    if score_id:
        score_obj = ScoreControll.query.get(score_id)
        if not score_obj:
            return jsonify("Score_id not found"), 404
        else:
            score_obj_2 = Score.query.get(score_id)
            db.session.delete(score_obj)
            db.session.delete(score_obj_2)
            return jsonify("Score deleted"), 200







    










    

    




        




