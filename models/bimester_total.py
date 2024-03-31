from flask_sqlalchemy import SQLAlchemy
from config.config import db 

class BimesterTotal(db.Model):
    __tablename__ = "bim_total_table"
    bim_total_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    total_bim = db.Column(db.Float)

    def __init__(self, total_bim):
        self.total_bim = total_bim

    def to_json(self):
        return {
            "bim_total_id": self.bim_total_id,
            "total_bim": self.total_bim,
        }
    def __repr__(self):
        return f"bim_total_id = {self.bim_total_id} total_bim = {self.total_bim}"
        
        
