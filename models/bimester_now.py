from flask_sqlalchemy import SQLAlchemy
from config.config import db
from sqlalchemy import ForeignKey

class BimesterNow(db.Model):
    __tablename__ = "bim_now_table"
    bim_now_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    subject_id = db.Column(db.Integer, ForeignKey("subjects_table.subject_id"))
    bim_total_id =  db.Column(db.Integer, ForeignKey("bim_total_table.bim_total_id"))
    bimester_id = db.Column(db.Integer, ForeignKey("bimesters_table.bimester_id"))
    group_id = db.Column(db.Integer, ForeignKey('groups_table.group_id'))
    bim_now_sum = db.Column(db.Float, default = 0.0)

    def __init__(self, subject_id, bimester_id, bim_total_id, group_id):
        self.subject_id = subject_id
        self.bimester_id = bimester_id
        self.bim_total_id = bim_total_id
        self.group_id = group_id

    def to_json(self):
        return {
            "bim_now_id": self.bim_now_id,
            "group_id": self.group_id, 
            "bim_total_id": self.bim_total_id,
            "bim_now_sum": self.bim_now_sum,
            "bimester_id": self.bimester_id,
            "subject_id": self.subject_id
        }



    




