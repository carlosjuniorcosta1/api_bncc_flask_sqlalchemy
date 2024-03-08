from config.config import db

class Materia(db.Model):
    __tablename__ = "tabela_materias"
    id_materia = db.Column(db.Integer, primary_key=True, autoincrement=True)
    materia = db.Column(db.String(40))

    def __init__(self, materia):
        self.materia = materia 

    def to_json(self):
        return  {
            "id_materia": self.id_materia,
            "materia": self.materia
            }
    
        
    
        

