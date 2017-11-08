from init import session
from models import Meal, Day
from sqlalchemy import desc
from datetime import date,timedelta

def getCurrentDay():
    lastDay = getLastDay()
    oneDay = timedelta(days=1)
    if (lastDay!= None):
        while (lastDay.dateofconsum != date.today()):
            lastDay=Day(dateofconsum=lastDay.dateofconsum+oneDay)
            session.add(lastDay)
            print(lastDay.dateofconsum)
    else:
        lastDay=Day(dateofconsum=date.today())
        session.add(lastDay)
        print(lastDay.dateofconsum)
    session.commit()
    return getLastDay()

def getLastDay():
    res = session.query(Day).order_by(desc(Day.dateofconsum)).first()
    return res

 
def addMeal(day,name,kcal,price=None):
    session.add(Meal(day= day, name=name, kcal = kcal,price=price))
    session.commit()



