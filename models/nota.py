from flask_sqlalchemy import SQLAlchemy
from config.config import db 
from sqlalchemy import ForeignKey


class Nota(db.Model):
    __tablename__ = "tabela_notas"
    id_nota = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nota = db.Column(db.Float)
    id_atividade = db.Column(db.Integer, ForeignKey("tabela_atividades.id_atividade"))
    id_aluno = db.Column(db.Integer, ForeignKey("tabela_alunos.id_aluno"))

    def __init__(self, nota, id_atividade, id_aluno):
        self.nota = nota 
        self.id_atividade = id_atividade
        self.id_aluno = id_aluno

    def to_json(self):
        return {
            "id_nota": self.id_nota,
            "nota": self.nota,
            "id_atividade": self.id_atividade,
            "id_aluno": self.id_aluno
        }
        