from flask_sqlalchemy import SQLAlchemy
from config.config import db


class Group(db.Model):
    __tablename__ = "groups_table"
    group_id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    group = db.Column(db.Integer)
    
    def __init__(self, group):
        self.group = group 

    def to_json(self):
        return {
        "group_id": self.group_id,
        "group": self.group

        }


