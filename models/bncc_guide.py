from flask_sqlalchemy import SQLAlchemy 
from config.config import db
from sqlalchemy import ForeignKey

class BnccGuide(db.Model):
    __tablename__ = "bncc_table"
    bncc_id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    cur_comp = db.Column(db.String(20))
    subject_id = db.Column(db.Integer, ForeignKey("subjects_table.subject_id"))
    k_obj = db.Column(db.Text)
    skill = db.Column(db.Text)
    description = db.Column(db.Text)
    es1 = db.Column(db.Boolean)
    es2 = db.Column(db.Boolean)
    es3 = db.Column(db.Boolean)
    es4 = db.Column(db.Boolean)
    es5 = db.Column(db.Boolean)
    es6 = db.Column(db.Boolean)
    es7 = db.Column(db.Boolean)
    es8 = db.Column(db.Boolean)
    es9 = db.Column(db.Boolean)

    def __init__(self, cur_comp,subject_id, skill, 
                 description, es1, es2,
                 es3, es4, es5, es6,
                 es7, es8, es9):
        self.cur_comp = cur_comp
        self.subject_id = subject_id
        self.skill = skill
        self.description = description
        self.es1 = es1
        self.es2 = es2
        self.es3 = es3
        self.es4 = es4
        self.es5 = es5
        self.es6 = es6
        self.es7 = es7
        self.es8 = es8
        self.es9 = es9

    def to_json(self):
            return {
            "bncc_id": self.bncc_id,
            "cur_comp": self.cur_comp,
            "subject_id": self.subject_id,
            "skill": self.skill,
            "description": self.description,
            "es1": self.es1,
            "es2": self.es2,
            "es3": self.es3,
            "es4": self.es4,
            "es5": self.es5,
            "es6": self.es6,
            "es7": self.es7,
            "es8": self.es8,
            "es9": self.es9 
            }
    def __repr__(self):
            return f"Component{self.cur_comp}, skill {self.skill}"
    

        