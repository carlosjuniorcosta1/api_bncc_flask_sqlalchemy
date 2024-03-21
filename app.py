from flask import Flask, jsonify
from config.config import Config, db
from blueprints.student_dir_bp.student_crud import student_bp
from blueprints.student_dir_bp.student_filters import student_filters_bp
from blueprints.activitity_dir_bp.activitity_crud_bp import act_crud_bp
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


app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
app.register_blueprint(student_bp)
app.register_blueprint(student_filters_bp)
app.register_blueprint(act_crud_bp)
Migrate(app, db)

if __name__ == "__main__":
   
 
    app.run()






