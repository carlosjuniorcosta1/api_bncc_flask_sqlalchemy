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

@bncc_guide_bp.route("/habilidade/<int:bncc_id>")
def get_skill(bncc_id):
    skill = BnccGuide.query.get(bncc_id)
    if not skill:
        return jsonify(message="Skill not found"), 404
    else:
        skill_json = skill.to_json()
        return jsonify(message="Skill requested", data=skill_json), 200

