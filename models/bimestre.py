from config.config import db 

class Bimestre(db.Model):
    __tablename__ = "tabela_bimestres"
    id_bimestre = db.Column(db.Integer, primary_key = True, autoincrement=True)
    bimestre = db.Column(db.String(10))

    def __init__(self, bimestre):        
        self.bimestre = bimestre
    
    def to_json(self):
        return     {
        "id_bimestre": self.id_bimestre,
        "bimestre": self.bimestre

    }
    
    

        
