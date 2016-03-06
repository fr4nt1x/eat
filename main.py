from init import session
from models import Meal, Day
from ingredients import RockstarLime
from datetime import date

def getCurrentDay():
    if getLastDay() is None:
        session.add(Day(dateofconsum=date.today()))
        session.commit()
    return getLastDay()

def getLastDay():
    res = session.query(Day).filter_by(dateofconsum=date.today()).first()
    return(res)

 
def addMeal(day,name,kcal):
    session.add(Meal(day= day, name=name, kcal = kcal ))
    session.commit()



