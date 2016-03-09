
from sqlalchemy import create_engine
import models_ing
from models_ing import Ingredients


engine = create_engine('sqlite:///db\inc.db')
models_ing.Baseincr.metadata.create_all(engine)
