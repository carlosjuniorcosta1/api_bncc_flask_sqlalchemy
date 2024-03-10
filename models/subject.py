from config.config import db

class Subject(db.Model):
    __tablename__ = "subjects_table"
    subject_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    subject = db.Column(db.String(40))

    def __init__(self, subject):
        self.subject = subject 

    def to_json(self):
        return  {
            "subject_id": self.subject_id,
            "subject": self.subject
            }
    
    
        
    
        

