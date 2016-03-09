from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Baseincr = declarative_base()


class Ingredients(Baseincr):
    __tablename__ = 'day'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    kcalPerOne = Column(Float)
    GperOne = Column(Float,index= True)
    


