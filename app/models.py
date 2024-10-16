from .db import db

class Student(db.Model):
    id: int
    name: str
    standard: str
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50) ,nullable=False)
    standard = db.Column(db.String(50), nullable=False)

