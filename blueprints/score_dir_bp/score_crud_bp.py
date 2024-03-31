from flask import request, jsonify, Blueprint
from config.config import db 
from flask_sqlalchemy import SQLAlchemy 
from models.score import Score
from models.student import Student
from models.activity import Activity

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
    scores = Score.query.filter(act_id==act_id).all()
    if not scores:
        return jsonify(message="No scores for this activity"), 400
    scores_json = [x.to_json() for x in scores]
    return jsonify(data=scores_json, message= "Scores for this activity"), 200
    
@score_crud_bp.route('/nota', methods=["POST"])
def add_score():
    data_score = request.get_json()
    act_id = data_score.get('act_id')
    score = data_score.get('score')
    student_id = data_score.get('student_id')
    mandatory_fields = ["act_id", "score", "student_id"]
    activity = Activity.query.get(act_id)
    if not activity:
        return jsonify("No activities were found with this act_id"), 404
    group_id = activity.group_id
    list_students = Student.query.filter_by(group_id=group_id).with_entities(Student.student_id).all()
    list_students_ids = [x[0] for x in list_students]
    if student_id not in list_students_ids:
        return jsonify(f"Invalid student_id {student_id}. This student has not been registered in the group"), 400
    total_act = activity.total_act    
    if score < total_act:
        new_score = Score(act_id=act_id, student_id=student_id, score=score)
    db.session.add(new_score)
    new_score_json = new_score.to_json()
    return  jsonify(message="Trying", data= new_score_json), 201






    

    




        




