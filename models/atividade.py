from flask_sqlalchemy import SQLAlchemy
from config.config import db
from datetime import datetime
from sqlalchemy import ForeignKey

class Atividade(db.Model):
    __tablename__ = "tabela_atividades"
    id_atividade = db.Column(db.Integer, primary_key=True, autoincrement=True)
    data_atividade = db.Column(db.Date, default= datetime.now().date())
    descricao_atv = db.Column(db.String(100))
    valor_atv = db.Column(db.Float)
    status_atv = db.Column(db.Boolean, default=False)
    id_turma = db.Column(db.Integer, ForeignKey("tabela_turmas.id_turma"))
    id_materia = db.Column(db.Integer, ForeignKey("tabela_materias.id_materia"))
    id_bimestre = db.Column(db.Integer, ForeignKey("tabela_bimestres.id_bimestre"))
    
    def __init__(self, descricao_atv, valor_atv, id_turma, id_materia, id_bimestre):
        self.descricao_atv = descricao_atv
        self.valor_atv = valor_atv
        self.id_turma = id_turma
        self.id_materia = id_materia
        self.id_bimestre = id_bimestre

    def to_json(self):
        return {
            "id_atividade": self.id_atividade,
            "data_atividade": self.data_atividade,
            "descricao_atv": self.descricao_atv,
            "valor_atv": self.valor_atv,
            "status_atv": self.status_atv, 
            "id_turma": self.id_turma,
            "id_materia": self.id_materia,
            "id_bimestre": self.id_bimestre
        }




