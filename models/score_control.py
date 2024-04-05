from flask_sqlalchemy import SQLAlchemy
from config.config import db 
from sqlalchemy import ForeignKey


class ScoreControll(db.Model):
    __tablename__ = "score_controll_table"
    score_controll_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    score_id = db.Column(db.Integer, ForeignKey("scores_table.score_id"))
    score_now = db.Column(db.Float, default = 0.0)
    

    def __init__(self, score_id, score_now):
        self.score_id = score_id
        self.score_now = score_now

    def to_json(self):
        return {
            "score_controll_id": self.score_controll_id,
            "score_now": self.score_now
        }



    
    
    
