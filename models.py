from sqlalchemy import Column, ForeignKey, Integer, String, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Day(Base):
    __tablename__ = 'day'
    id = Column(Integer, primary_key=True)
    dateofconsum = Column(Date,index=True)
    meals = relationship("Meal", backref="day")
    weight = Column(Float,index=True)
    
class Meal(Base):
    __tablename__ = 'meal'
    # Here we define columns for the table meal
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    kcal = Column(Integer,index= True)
    day_id = Column(Integer, ForeignKey('day.id'))
    price = Column(Float,index=True)


