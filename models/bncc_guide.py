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
    first_el_school = db.Column(db.Boolean)
    second_el_school = db.Column(db.Boolean)
    third_el_school = db.Column(db.Boolean)
    fourth_el_school = db.Column(db.Boolean)
    fifth_el_school = db.Column(db.Boolean)
    sixth_el_school = db.Column(db.Boolean)
    seventh_el_school = db.Column(db.Boolean)
    eighth_el_school = db.Column(db.Boolean)
    nineth_el_school = db.Column(db.Boolean)

    def __init__(self, cur_comp, subject_id, skill, description, first_el_school, second_el_school,
                 third_el_school, fourth_el_school, fifth_el_school, sixth_el_school,
                 seventh_el_school, eighth_el_school, nineth_el_school):
        self.cur_comp = cur_comp
        self.subject_id = subject_id
        self.skill = skill
        self.description = description
        self.first_el_school = first_el_school
        self.second_el_school = second_el_school
        self.third_el_school = third_el_school
        self.fourth_el_school = fourth_el_school
        self.fifth_el_school = fifth_el_school
        self.sixth_el_school = sixth_el_school
        self.seventh_el_school = seventh_el_school
        self.eighth = eighth_el_school
        self.nineth = nineth_el_school

    def to_json(self):
            return {
            "bncc_id": self.bncc_id,
            "cur_comp": self.cur_comp,
            "subject_id": self.subject_id,
            "skill": self.skill,
            "description": self.description,
            "first_el_school": self.first_el_school,
            "second_el_school": self.second_el_school,
            "third_el_school": self.third_el_school,
            "fourth_el_school": self.fourth_el_school,
            "fifth_el_school": self.fifth_el_school,
            "sixth_el_school": self.sixth_el_school,
            "seventh_el_school": self.seventh_el_school,
            "eighth": self.eighth_el_school,
            "nineth": self.nineth_el_school 
            }
    def __repr__(self):
            return f"Component{self.cur_comp}, skill {self.skill}"
    

        