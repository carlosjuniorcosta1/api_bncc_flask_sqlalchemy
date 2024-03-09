from flask_sqlalchemy import SQLAlchemy
from config.config import db 
from sqlalchemy import ForeignKey

frequencia_alunos = db.Table("frequencia_alunos", 
                     db.Column("id_frequencia", db.Integer, 
                               ForeignKey("tabela_frequencias.id_frequencia")),
                    db.Column("id_aluno", db.Integer, ForeignKey("tabela_alunos.id_aluno"))           
                             )


class Frequencia(db.Model):
    __tablename__ = "tabela_frequencias"
    id_frequencia = db.Column(db.Integer, primary_key=True, autoincrement=True)
    presente = db.Column(db.Boolean)
    id_aula = db.Column(db.Integer, ForeignKey("tabela_aulas.id_aula"))
    id_aluno = db.Column(db.Integer, ForeignKey("tabela_alunos.id_aluno"))
    alunos = db.relationship("Aluno", secondary=frequencia_alunos, backref="frequencias", lazy="dynamic")
    
    def __init__(self, presente, id_aula, id_aluno):
        self.presente = presente
        self.id_aluno = id_aluno
        self.id_aula = id_aula

    def to_json(self):
        return {
            "id_frequencia": self.id_frequencia,
            "presente": self.presente,
            "id_aula": self.id_aula,
            "id_aluno": self.id_aluno
        }
        