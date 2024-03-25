from flask import request, jsonify, Blueprint
from config.config import db 
from flask_sqlalchemy import SQLAlchemy 
from models.score import Score
from models.student import Student
from models.activity import Activity, scores


score_crud_bp = Blueprint("score_crud_bp", __name__)

@score_crud_bp.route('/notas', methods=["GET"])
def get_all_scores():
    scores = Score.query.all()
    if not scores:
        return jsonify(message="No scores registered yet"), 400
    scores_json = [x.to_json() for x in scores]
    return jsonify(data=scores_json, message="Requested scores"), 200

#using table Scores
@score_crud_bp.route('/nota', methods=["GET", "POST"])
def add_score():
    data_score = request.get_json()
    if not "act_id" in data_score:
        return jsonify(message="You need to provide and act_id to insert the students scores"), 400
    act_id = data_score.get('act_id')
    activity = Activity.query.get(act_id)
    group_id = activity.group_id
    students_data = Student.query.filter_by(group_id=group_id).with_entities(Student.student_id, Student.full_name).all()
    students_json = [{'student_id': x.student_id, 'full_name': x.full_name, 'score': 0} for x in students_data]
    scores_to_add = []
    for x in students_json:
        new_score = Score(act_id=act_id, score=0, student_id=x['student_id'])
        scores_to_add.append(new_score)
    db.session.add_all(scores_to_add)
    db.session.commit()

    return jsonify(message="Score initialized successfully", data=students_json), 201

#using intermediate table scores
@score_crud_bp.route('/notaalunos', methods=["GET", "POST"])
def add_new_score():
    data_score = request.get_json()
    if "act_id" not in data_score:
        return jsonify(message="You need to provide an act_id (activity id) in order to add a score for a student"), 400
    act_id = data_score.get('act_id')

    activity = Activity.query.get(act_id)
    group_id = activity.group_id
    student_ids = Student.query.filter_by(group_id=group_id).with_entities(Student.student_id).all()
    student_ids = [x for (x,) in student_ids]
    for x in range(len(student_ids)):
        new_score = scores.insert().values(act_id=act_id, student_id=x+1, score=0)
        db.session.execute(new_score)
    db.session.commit()
    

    return jsonify(message="trying"), 201