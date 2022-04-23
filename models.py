from colorsys import hsv_to_rgb
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class StudentModel(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.column(db.String())
    last_name = db.column(db.String())
    email = db.column(db.String())
    password = db.column(db.String())
    gender = db.column(db.String())
    hobbies = db.column(db.String())
    country = db.column(db.String(80))

    def __init__(self,first_name,last_name,email,password,gender,hobbies,country):
        self.first_name=first_name
        self.last_name=last_name
        self.email=email
        self.password=password
        self.gender=gender
        self.hobbies=hobbies
        self.country=country

    def __repr__(self):
        return f"{self.first_name}:{self.last_name}"