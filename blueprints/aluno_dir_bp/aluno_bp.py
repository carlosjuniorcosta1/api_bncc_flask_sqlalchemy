from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint, jsonify, request
from models.aluno import Aluno

aluno_bp = Blueprint("aluno_bp", __name__)


@aluno_bp.route('/alunos', methods=["GET"])
def listar_alunos():
    alunos = Aluno.query.all()
    return jsonify(data= Aluno.to_json_list(alunos), message="Lista de alunos")

@aluno_bp.route('/aluno', methods=["GET"])
def listar_aluno():
    id_aluno = request.args.get('id')
    aluno = Aluno.query.filter_by(id_aluno=id_aluno).first()
    aluno_js = aluno.to_json()
    return jsonify(data=aluno_js, message="Aluno solicitado")



    
        


