from init import session
from models import Meal, Day
from sqlalchemy import desc
from datetime import date,timedelta
import matplotlib.pyplot as plt
import numpy as np

kcalPerLb = 3500
LbinKg = 0.453592

def interpolate(weights):
    #add first and last entry just as constant
    if weights[0] == None:
        for w in weights:
            if w != None:
                weights[0] = w
                break
            
    if weights[-1] == None:
        for w in weights[::-1]:
            if w != None:
                weights[-1] = w
                break
    for i,w in enumerate(weights) :
        if w == None:
            for j,k in enumerate(weights[i:]):
                if k != None:
                    if i != 0 :
                        startweight = weights[i-1]
                    else:
                        startweight = 0
                    endweight = k
                    break
            if endweight == None:
                endweight = 0
                        
            delta = (endweight-startweight)/(j+1)
            #print(startweight,endweight)
            weights[i:j+i] = np.ones(j)*startweight + np.arange(1,j+1)*delta
    return weights
    
def get_days(startday):
    allDays = np.array(session.query(Day).order_by(Day.dateofconsum).all())[startday:]
    weights = np.array([x.weight for x in allDays])    
    kcal = np.array([sum([ m.kcal for m in x.meals]) for x in allDays])
    
   

    weights = interpolate(weights)
    weightdeltaLb = (weights[-2]-weights[0])/LbinKg
    MaintenanceKcal = (sum(kcal)-weightdeltaLb*kcalPerLb)/np.size(kcal)
    print("Maintenance Kcal :",MaintenanceKcal)
    x = np.arange(1,np.size(weights)+1)
    y1 = ((weights/max(weights)))
    plt.plot(x,y1)
    y2= kcal/max(kcal)
    plt.plot(x,y2)
    y3=np.ones(np.size(weights))*(MaintenanceKcal/max(kcal))
    plt.plot(x,y3)
   #print(np.trapz((y2-y3)*max(kcal),x))
    plt.show()

def get_price_per_day(startday):
    allDays = np.array(session.query(Day).order_by(Day.dateofconsum).all())[startday:]
    price = np.array([sum([z.price for z in x.meals if z.price!= None]) for x in allDays])    
    print(sum(price)/allDays.size)
#get_days(50)

get_price_per_day(235)
            

