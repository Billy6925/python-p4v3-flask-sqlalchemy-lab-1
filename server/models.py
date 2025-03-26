from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData,Integer,Column,Float,String
from sqlalchemy_serializer import SerializerMixin

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

# Add models here
class Earthquake(db.Model,SerializerMixin):
    __tablename__ = 'earthquakes'
    id = Column(Integer(), primary_key =True)
    magnitude =Column(Float())
    location = Column(String())
    year =Column(Integer())

    def __init__(self,magnitude=0.0,location="",year=0):
        self.magnitude = magnitude
        self.location = location
        self.year = year

    def __repr__(self):
        return f'Earthquake {self.id}, {self.magnitude}, {self.location}, {self.year}'

