from config.config import db 

class Bimester(db.Model):
    __tablename__ = "bimesters_table"
    bimester_id = db.Column(db.Integer, primary_key = True, autoincrement=True)
    bimester = db.Column(db.String(10))

    def __init__(self, bimester):        
        self.bimester = bimester
    
    def to_json(self):
        return     {
        "bimester_id": self.bimester_id,
        "bimester": self.bimester

    }
    
    

        
