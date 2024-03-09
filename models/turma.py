from flask_sqlalchemy import SQLAlchemy
from config.config import db


class Turma(db.Model):
    __tablename__ = "tabela_turmas"
    id_turma = db.Column(db.Integer, primary_key = True, autoincrement=True)
    turma = db.Column(db.Integer)

    def __init__(self, turma):
        self.turma = turma 

    def to_json(self):
        return {
        "id_nota": self.id_turma,
        "nota": self.turma

        }


