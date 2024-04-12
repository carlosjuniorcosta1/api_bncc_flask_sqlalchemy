from flask_sqlalchemy import SQLAlchemy
from config.config import db 
from flask import Blueprint, request, jsonify
from models.bncc_guide import BnccGuide

bncc_guide_bp = Blueprint("bncc_guide_bp", __name__)

@bncc_guide_bp.route("/habilidades")
def get_all_skills():
    all_skills = BnccGuide.query.all()
    all_skills_json = [x.to_json() for x in all_skills]
    return jsonify(message="All skills", data=all_skills_json)

@bncc_guide_bp.route("/habilidade/<int:bncc_id>", methods=["GET"])
def get_skill(bncc_id):
    skill = BnccGuide.query.get(bncc_id)
    if not skill:
        return jsonify(message="Skill not found"), 404
    else:
        skill_json = skill.to_json()
        return jsonify(message="Skill requested", data=skill_json), 200

@bncc_guide_bp.route('/habilidades/filtrar', methods=["GET"])
def get_skill_filter():
    subject = request.args.get('subject')
    es = request.args.get('grade')
    if es == "1":
        skill_query = BnccGuide.query.filter(BnccGuide.es1 == True, BnccGuide.cur_comp == subject)
    elif es == "2":
        skill_query = BnccGuide.query.filter(BnccGuide.es2 == True, BnccGuide.cur_comp == subject)
    elif es == "3":
        skill_query = BnccGuide.query.filter(BnccGuide.es3 == True, BnccGuide.cur_comp == subject)
    elif es == "4":
        skill_query = BnccGuide.query.filter(BnccGuide.es4 == True, BnccGuide.cur_comp == subject)
    elif es == "5":
        skill_query = BnccGuide.query.filter(BnccGuide.es5 == True, BnccGuide.cur_comp == subject)
    elif es == "6":
        skill_query = BnccGuide.query.filter(BnccGuide.es6 == True, BnccGuide.cur_comp == subject)
    elif es == "7":
        skill_query = BnccGuide.query.filter(BnccGuide.es7 == True, BnccGuide.cur_comp == subject)        
    elif es == "8":
        skill_query = BnccGuide.query.filter(BnccGuide.es8 == True, BnccGuide.cur_comp == subject)
    elif es == "9":
        skill_query = BnccGuide.query.filter(BnccGuide.es9 == True, BnccGuide.cur_comp == subject)
    skill_query_all = skill_query.all()
    skill_query_json = [x.to_json() for x in skill_query_all]
    return jsonify(message="Requested skills", data=skill_query_json), 200
    













