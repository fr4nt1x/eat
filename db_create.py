
from sqlalchemy import create_engine
import models
from models import Day,Meal


engine = create_engine('sqlite:///db\eatit.db')

models.Base.metadata.create_all(engine)
