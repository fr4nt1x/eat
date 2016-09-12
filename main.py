from init import session
from models import Meal, Day
from sqlalchemy import desc
from datetime import date,timedelta

def getCurrentDay():
    lastDay = getLastDay()
    oneDay = timedelta(days=1)
    
    while (lastDay.dateofconsum != date.today()):
        lastDay=Day(dateofconsum=lastDay.dateofconsum+oneDay)
        session.add(lastDay)
        print(lastDay.dateofconsum)
        
    session.commit()
    return getLastDay()

def getLastDay():
    res = session.query(Day).order_by(desc(Day.dateofconsum)).first()
    return res

 
def addMeal(day,name,kcal):
    session.add(Meal(day= day, name=name, kcal = kcal ))
    session.commit()



