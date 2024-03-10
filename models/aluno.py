from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from datetime import datetime
from config.config import db 

class Aluno(db.Model):
    __tablename__ = "tabela_alunos"    
    id_aluno = db.Column(db.Integer, primary_key=True, autoincrement = True)
    nome = db.Column(db.String(50), nullable = False)
    sobrenome = db.Column(db.String(200), nullable = False)
    nome_completo = db.Column(db.Text, nullable = False)
    ano = db.Column(db.String(20), nullable = False)
    nivel_ensino = db.Column(db.Text, nullable = False)
    data_nascimento = db.Column(db.Date, nullable = False)
    data_cadastro = db.Column(db.Date, nullable = False)
    status_aluno = db.Column(db.Boolean, nullable=False)
    id_turma = db.Column(db.Integer, ForeignKey("tabela_turmas.id_turma") )
    turma = db.relationship('Turma', backref="alunos", uselist=False)

    def __init__(self, nome, sobrenome, ano, data_nascimento, id_turma):
        self.nome = nome 
        self.sobrenome = sobrenome
        self.nome_completo = self.nome + " " + self.sobrenome # preenche auto
        self.ano = ano
        self.nivel_ensino = self.preenche_nivel() # preenche auto
        self.data_nascimento = self.preenche_data_nascimento(data_nascimento) #digitar data brasileira
        self.data_cadastro = datetime.now().date() # preenche auto
        self.status_aluno = True 
        self.id_turma = id_turma

    def preenche_nivel(self):
        if self.ano.endswith('_ef'):
            nivel_auto = "ef"
            return nivel_auto
        elif self.ano.endswith('_em'):
            nivel_auto = "em"
            return nivel_auto
    
    def preenche_data_nascimento(self, data_str):
        dia, mes, ano = map(int, data_str.split('/'))
        return datetime(ano, mes, dia).date()

    def to_json(self):
        return {
            'id_aluno': self.id_aluno,
            'nome': self.nome,
            'sobrenome': self.sobrenome,
            'nome_completo': self.nome_completo,
            'ano': self.ano,
            'nivel_ensino': self.nivel_ensino,
            'data_nascimento': self.data_nascimento.strftime('%d/%m/%Y'),
            'data_cadastro': self.data_cadastro.strftime("%d/%m/%Y"),
            'status_aluno': self.status_aluno,
            "id_turma": self.id_turma
        }
    @staticmethod
    def to_json_list(alunos):
        alunos_json = []
        for aluno in alunos:
            alunos_json.append(aluno.to_json())
        return alunos_json
        

    
        




