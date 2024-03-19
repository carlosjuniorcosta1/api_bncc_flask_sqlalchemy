from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import ForeignKey
from config.config import db 

class Lecture(db.Model):
    __tablename__ = "lectures_table"
    lecture_id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    lecture_description = db.Column(db.String(100))
    lecture_date = db.Column(db.Date)
    bncc_skill = db.Column(db.Text)
    subject_id = db.Column(db.Integer, ForeignKey("subjects_table.subject_id"))
    bimester_id = db.Column(db.Integer, ForeignKey("bimesters_table.bimester_id"))
    group_id = db.Column(db.Integer, ForeignKey("groups_table.group_id"))
    bncc_id = db.Column(db.Integer, ForeignKey("bncc_table.bncc_id"))
    materia = db.relationship("Subject", uselist=False )
    bimester = db.relationship("Bimester", uselist=False)
    group = db.relationship("Group", uselist=False ) 
    skill = db.relationship('BnccGuide', lazy='joined')

    def __init__(self, lecture_description, 
                 bncc_skill, subject_id, 
                 bimester_id, group_id):
        self.lecture_description = lecture_description
        self.lecture_date = datetime.now().date()
        self.bncc_skill = bncc_skill
        self.subject_id = subject_id
        self.bimester_id = bimester_id
        self.group_id = group_id 

    def to_json(self):
        return {
            "lecture_id": self.lecture_id,
            "lecture_description": self.lecture_description,
            "lecture_date": self.lecture_date.strftime("%d/%m/%Y"),
            "bncc_skill": self.bncc_skill,
            "subject_id": self.subject_id,
            "bimester_id": self.bimester_id,
            "group_id": self.group_id
        }


