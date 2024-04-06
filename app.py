from flask import Flask, jsonify
from config.config import Config, db
from blueprints.student_crud_bp.student_crud import student_bp
from blueprints.activitity_dir_bp.activitity_crud_bp import act_crud_bp
from blueprints.score_dir_bp.score_crud_bp import score_crud_bp
from blueprints.lecture_dir_bp.lecture_bp import lecture_bp
from blueprints.bncc_guide_bp.bncc_guide_bp import bncc_guide_bp
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from models.student import Student
from models.bimester import Bimester
from models.subject import Subject
from models.score import Score
from models.group import Group
from models.lecture import Lecture
from models.frequency import Frequency
from models.activity import Activity
from models.bncc_guide import BnccGuide
from models.bimester_total import BimesterTotal
from models.bimester_now import BimesterNow
from models.score_control import ScoreControll


app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(student_bp)
app.register_blueprint(act_crud_bp)
app.register_blueprint(score_crud_bp)
app.register_blueprint(lecture_bp)
app.register_blueprint(bncc_guide_bp)
db.init_app(app)

Migrate(app, db)

if __name__ == "__main__":        

    app.run(debug=True)






