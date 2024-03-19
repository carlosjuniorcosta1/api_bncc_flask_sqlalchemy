from flask_sqlalchemy import SQLAlchemy
from config.config import db
from datetime import datetime
from sqlalchemy import ForeignKey

class Activity(db.Model):
    __tablename__ = "activities_table"
    act_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    act_date = db.Column(db.Date)
    act_description = db.Column(db.String(100))
    score_atv = db.Column(db.Float)
    act_status = db.Column(db.Boolean, default=False)
    group_id = db.Column(db.Integer, ForeignKey("groups_table.group_id"))
    subject_id = db.Column(db.Integer, ForeignKey("subjects_table.subject_id"))
    bimester_id = db.Column(db.Integer, ForeignKey("bimesters_table.bimester_id"))
    group = db.relationship("Group", uselist=False)
    subject = db.relationship("Subject", uselist=False)
    bimester = db.relationship("Bimester", uselist=False)     
    
    def __init__(self, act_description, score_atv, group_id, subject_id, bimester_id):
        self.act_description = act_description
        self.score_atv = score_atv
        self.group_id = group_id
        self.subject_id = subject_id
        self.bimester_id = bimester_id

    def to_json(self):
        return {
            "act_id": self.act_id,
            "act_date": self.act_date,
            "act_description": self.act_description,
            "score_atv": self.score_atv,
            "act_status": self.act_status, 
            "group_id": self.group_id,
            "subject_id": self.subject_id,
            "bimester_id": self.bimester_id
        }




