from flask import Blueprint, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from config.config import db
from models.aluno import Aluno
from datetime import datetime


aluno_filtro_bp = Blueprint('aluno_filtro_bp', __name__)

@aluno_filtro_bp.route('/alunos/filtrar', methods=["GET"])
def pesquisar_aluno():
    nome = request.args.get('nome')
    sobrenome = request.args.get('sobrenome')   
    data_nascimento = request.args.get('data_nascimento')
    data_cadastro = request.args.get('data_cadastro')
    id_turma = request.args.get('turma')
    nivel = request.args.get('nivel')
    status = request.args.get('status')

    if id_turma and nome:
        alunos_query = Aluno.query.filter(Aluno.id_turma == id_turma, Aluno.nome == nome).all()

    if id_turma and not nome:
        alunos_query = Aluno.query.filter_by(id_turma = id_turma).all()
    if nome and not sobrenome:  
        alunos_query = Aluno.query.filter_by(nome=nome).all()
    if nome and sobrenome:
        alunos_query = Aluno.query.filter(Aluno.nome == nome, Aluno.sobrenome == sobrenome)
    if sobrenome and not nome:
        alunos_query = Aluno.query.filter(Aluno.sobrenome == sobrenome)        
    if data_nascimento:
        alunos_query = Aluno.query.filter_by(data_nascimento=data_nascimento).all() 
    if nivel:
        alunos_query = Aluno.query.filter_by(nivel_ensino=nivel).all()
    if status:
        alunos_query = Aluno.query.filter_by(status_aluno=status).all() 
    if data_cadastro:
        alunos_query = Aluno.query.filter_by(data_cadastro=data_cadastro)
    alunos_js = [x.to_json() for x in alunos_query]
    
    return jsonify(message="Alunos solicitados", data=alunos_js)




