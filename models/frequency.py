from flask_sqlalchemy import SQLAlchemy
from config.config import db 
from sqlalchemy import ForeignKey

frequency_students = db.Table("students_frequency", 
                     db.Column("frequency_id", db.Integer, 
                               ForeignKey("frequencies_table.frequency_id")),
                    db.Column("student_id", db.Integer, ForeignKey("students_table.student_id"))           
                             )


class Frequency(db.Model):
    __tablename__ = "frequencies_table"
    frequency_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    present = db.Column(db.Boolean)
    lecture_id = db.Column(db.Integer, ForeignKey("lectures_table.lecture_id"))
    student_id = db.Column(db.Integer, ForeignKey("students_table.student_id"))
    students = db.relationship("Student", secondary=frequency_students, backref="frequencies", lazy="dynamic")
    
    def __init__(self, present, lecture_id, student_id):
        self.present = present
        self.student_id = student_id
        self.lecture_id = lecture_id

    def to_json(self):
        return {
            "frequency_id": self.frequency_id,
            "present": self.present,
            "lecture_id": self.lecture_id,
            "student_id": self.student_id
        }
        