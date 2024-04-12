from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from datetime import datetime
from config.config import db 

class Student(db.Model):
    __tablename__ = "students_table"    
    student_id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    name = db.Column(db.String(50), nullable = False)
    surname = db.Column(db.String(200), nullable = False)
    full_name = db.Column(db.Text, nullable = False)
    level = db.Column(db.Text, nullable = False)
    date_birth = db.Column(db.Date, nullable = False)
    date_registration = db.Column(db.Date, nullable = False)
    student_status = db.Column(db.Boolean, nullable=False)
    group_id = db.Column(db.Integer, ForeignKey("groups_table.group_id") )
    group = db.relationship('Group', backref="students", uselist=False)

    def __init__(self, name, surname, date_birth, group_id):
        self.name = name 
        self.surname = surname
        self.full_name = self.name + " " + self.surname # preenche auto
        self.level = self.preenche_nivel() # preenche auto
        self.date_birth = self.preenche_date_birth(date_birth) #digitar data brasileira
        self.date_registration = datetime.now().date() # preenche auto
        self.student_status = True 
        self.group_id = group_id

    
    def preenche_date_birth(self, data_str):
        day, month, year = map(int, data_str.split('/'))
        return datetime(year, month, day).date()

    def to_json(self):
        return {
            'student_id': self.student_id,
            'name': self.name,
            'surname': self.surname,
            'full_name': self.full_name,
            'level': self.level,
            'date_birth': self.date_birth.strftime('%d/%m/%Y'),
            'date_registration': self.date_registration.strftime("%d/%m/%Y"),
            'student_status': self.student_status,
            "group_id": self.group_id
        }

        

    
        




