from flask_sqlalchemy import SQLAlchemy
from config.config import db 
from sqlalchemy import ForeignKey


class Score(db.Model):
    __tablename__ = "scores_table"
    score_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    score = db.Column(db.Float)
    act_id = db.Column(db.Integer, ForeignKey("activities_table.act_id"))
    student_id = db.Column(db.Integer, ForeignKey("students_table.student_id"))

    def __init__(self, score, act_id, student_id):
        self.score = score 
        self.act_id = act_id
        self.student_id = student_id

    def to_json(self):
        return {
            "score_id": self.score_id,
            "score": self.score,
            "act_id": self.act_id,
            "student_id": self.student_id
        }
        