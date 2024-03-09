from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import ForeignKey

from config.config import db 

class Aula(db.Model):
    __tablename__ = "tabela_aulas"
    id_aula = db.Column(db.Integer, primary_key = True, autoincrement=True)
    descricao_aula = db.Column(db.String(100))
    data_aula = db.Column(db.Date)
    habilidade_bncc = db.Column(db.Text)
    id_materia = db.Column(db.Integer, ForeignKey("tabela_materias.id_materia"))
    id_bimestre = db.Column(db.Integer, ForeignKey("tabela_bimestres.id_bimestre"))
    id_turma = db.Column(db.Integer, ForeignKey("tabela_turmas.id_turma"))
    materia = db.relationship("Materia", uselist=False )
    bimestre = db.relationship("Bimestre", uselist=False)
    turma = db.relationship("Turma", uselist=False )

    def __init__(self, descricao_aula, 
                 habilidade_bncc, id_materia, 
                 id_bimestre, id_turma):
        self.descricao_aula = descricao_aula
        self.data_aula = datetime.now().date()
        self.habilidade_bncc = habilidade_bncc
        self.id_materia = id_materia
        self.id_bimestre = id_bimestre
        self.id_turma = id_turma 

    def to_json(self):
        return {
            "id_aula": self.id_aula,
            "descricao_aula": self.descricao_aula,
            "data_aula": self.data_aula.strftime("%d/%m/%Y"),
            "habilidade_bncc": self.habilidade_bncc,
            "id_materia": self.id_materia,
            "id_bimestre": self.id_bimestre,
            "id_turma": self.id_turma
        }


