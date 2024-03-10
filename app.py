from flask import Flask, jsonify
from config.config import Config, db
from blueprints.aluno_dir_bp.aluno_crud_bp import aluno_bp
from blueprints.aluno_dir_bp.aluno_filtros_bp import aluno_filtro_bp
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from models.aluno import Aluno
from models.bimestre import Bimestre
from models.materia import Materia
from models.nota import Nota 
from models.turma import Turma 
from models.aula import Aula
from models.frequencia import Frequencia
from models.atividade import Atividade 


app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
app.register_blueprint(aluno_bp)
app.register_blueprint(aluno_filtro_bp)
Migrate(app, db)

if __name__ == "__main__": 
    app.run()






