from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint, jsonify, request
from models.aluno import Aluno
from config.config import db 
from datetime import datetime 
aluno_bp = Blueprint("aluno_bp", __name__)

@aluno_bp.route('/alunos', methods=["GET"])
def listar_alunos():
    alunos = Aluno.query.all()
    alunos_lista_js =  Aluno.to_json_list(alunos)
    return jsonify(data= alunos_lista_js, message="Lista de alunos")

@aluno_bp.route('/aluno/<int:id_aluno>', methods=['GET'])
def listar_aluno_url(id_aluno):
    aluno = Aluno.query.get(id_aluno)
    aluno_js = aluno.to_json()
    return jsonify(data=aluno_js, message="Aluno pela url")

@aluno_bp.route('/aluno', methods=["GET", "PUT"])
def atualizar_aluno():
    dados_atualizados = request.get_json()
    id_aluno = dados_atualizados['id_aluno']
    aluno = Aluno.query.filter_by(id_aluno=id_aluno).first()
    for chave, valor in dados_atualizados.items():
        if chave != "id_aluno":
            setattr(aluno, chave, valor)
    db.session.commit()
    return jsonify(message= f"aluno {aluno.to_json()} atualizado")

@aluno_bp.route('/aluno', methods=["POST"])
def cria_aluno():
    dados_aluno = request.get_json()
    nome = dados_aluno['nome']
    sobrenome = dados_aluno['sobrenome']
    ano = dados_aluno['ano']
    data_nascimento = dados_aluno['data_nascimento']
    id_turma = dados_aluno['id_turma']
    novo_aluno = Aluno(nome=nome, sobrenome=sobrenome, 
                       ano=ano, data_nascimento=data_nascimento,
                       id_turma=id_turma)
    db.session.add(novo_aluno)
    db.session.commit()
    return jsonify(message=f"Aluno {novo_aluno} adicionado", data=novo_aluno.to_json())

    












    
        


