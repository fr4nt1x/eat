

class Ingredient():
    def __init__(self,name,amount,kcalPerCG,GperOne):
        #amount describes standard unit, for rice and stuff its 100g, amount = 1 times kcalPerUnit gives the kcal in one standard unit
        self.name = name
        self.amount= amount
        self.kcalPerOne = kcalPerCG*(GperOne/100.0)
        self.GperOne = GperOne
        
    def getKcal(self):
        return self.kcalPerOne*self.amount


class RockstarLime(Ingredient):
    def __init__(self,amount):
        Ingredient.__init__(self,"RockstarLime",amount=float(amount),kcalPerCG=59, GperOne = 500)

class RockstarGuava(Ingredient):
    def __init__(self,amount):
        Ingredient.__init__(self,"RockstarGuava",amount=float(amount),kcalPerCG=67, GperOne = 500)
        
class RockstarRed(Ingredient):
    def __init__(self,amount):
        Ingredient.__init__(self,"RockstarRed",amount=float(amount),kcalPerCG=64, GperOne = 500)
class WildRice(Ingredient):
    def __init__(self,amount):
        Ingredient.__init__(self, "WildRice", amount=float(amount),kcalPerCG=344,GperOne = 100)

class WheatBread(Ingredient):
    def __init__(self,amount):
        Ingredient.__init__(self, "WheatBread", amount=float(amount),kcalPerCG=241,GperOne = 40)

class PeanutButterCrunchy(Ingredient):
    #one is a enoguh on a slice of bread
    def __init__(self,amount):
        Ingredient.__init__(self, "PeanutButterCrunchy", amount=float(amount),kcalPerCG=616,GperOne = 20)

        
class PhiladelphiaClassic(Ingredient):
    #one is a enoguh on a slice of bread
    def __init__(self,amount):
        Ingredient.__init__(self, "PhiladelphiaClassic", amount=float(amount),kcalPerCG=235,GperOne = 20)

class FolEpiFine(Ingredient):
    #one is a enoguh on a slice of bread
    def __init__(self,amount):
        Ingredient.__init__(self, "FolEpiFine", amount=float(amount),kcalPerCG=361,GperOne = 25)

class Almonds(Ingredient):
    #one handfull
    def __init__(self,amount):
        Ingredient.__init__(self, "Almonds", amount=float(amount),kcalPerCG=611,GperOne=20)

class RedLenses(Ingredient):
    def __init__(self,amount):
        Ingredient.__init__(self, "RedLenses", amount=float(amount),kcalPerCG=352,GperOne=120)

class Peas(Ingredient):
    def __init__(self,amount):
        Ingredient.__init__(self, "Peas", amount=float(amount),kcalPerCG=68,GperOne=100)

class PapricaRed(Ingredient):
    def __init__(self,amount):
        Ingredient.__init__(self, "PapricaRed", amount=float(amount),kcalPerCG=35,GperOne=200)

class Onion(Ingredient):
    def __init__(self,amount):
        Ingredient.__init__(self, "Onion", amount=float(amount),kcalPerCG=28,GperOne=40)

class Carot(Ingredient):
    def __init__(self,amount):
        Ingredient.__init__(self, "Carot", amount=float(amount),kcalPerCG=26,GperOne=100)

class Banana(Ingredient):
    def __init__(self,amount):
        Ingredient.__init__(self, "Banana", amount=float(amount),kcalPerCG=90,GperOne=100)

class LindChocolateChili(Ingredient):
    def __init__(self,amount):
        Ingredient.__init__(self, "LindChocolateChili", amount=float(amount),kcalPerCG=538,GperOne=20)   

class FlaxSeed(Ingredient):
    def __init__(self,amount):
        Ingredient.__init__(self, "FlaxSeed", amount=float(amount),kcalPerCG=471,GperOne=20)
        
class QuarkLow(Ingredient):
    def __init__(self,amount):
        Ingredient.__init__(self, "QuarkLow", amount=float(amount),kcalPerCG=66,GperOne=500)
        
class CherryJuice(Ingredient):
    def __init__(self,amount):
        Ingredient.__init__(self, "CherryJuice", amount=float(amount),kcalPerCG=59,GperOne=200)

  
class MilkRice(Ingredient):
    def __init__(self,amount):
        Ingredient.__init__(self, "MilkRice", amount=float(amount),kcalPerCG=357,GperOne=100)
        
class Milk(Ingredient):
    def __init__(self,amount):
        Ingredient.__init__(self, "Milk", amount=float(amount),kcalPerCG=47,GperOne=200)
        
class Raisins(Ingredient):
    def __init__(self,amount):
        Ingredient.__init__(self, "Raisins", amount=float(amount),kcalPerCG=299 ,GperOne=50)
        
class Butter(Ingredient):
    def __init__(self,amount):
        Ingredient.__init__(self, "Butter", amount=float(amount),kcalPerCG=745,GperOne=20)
        
class Plums(Ingredient):
    def __init__(self,amount):
        Ingredient.__init__(self, "Plums", amount=float(amount),kcalPerCG=80,GperOne=500)
        
class Sugar(Ingredient):
    def __init__(self,amount):
        Ingredient.__init__(self, "Sugar", amount=float(amount),kcalPerCG=405,GperOne=20)
        
class Egg(Ingredient):
    def __init__(self,amount):
        Ingredient.__init__(self, "Egg", amount=float(amount),kcalPerCG=137,GperOne=50)
        
class Pretzel(Ingredient):
    def __init__(self,amount):
        Ingredient.__init__(self, "Pretzel", amount=float(amount),kcalPerCG=217,GperOne=60)

class PretzelRing(Ingredient):
    def __init__(self,amount):
        Ingredient.__init__(self, "PretzelRing", amount=float(amount),kcalPerCG=350,GperOne=100)

class Turkey(Ingredient):
    def __init__(self,amount):
        Ingredient.__init__(self, "Turkey", amount=float(amount),kcalPerCG=97,GperOne=100)
        
class Porree(Ingredient):
    def __init__(self,amount):
        Ingredient.__init__(self, "Porree", amount=float(amount),kcalPerCG=26,GperOne=50)

class ChinaNoodles(Ingredient):
    def __init__(self,amount):
        Ingredient.__init__(self, "ChinaNoodles", amount=float(amount),kcalPerCG=359,GperOne=70)

class Beer(Ingredient):
    def __init__(self,amount):
        Ingredient.__init__(self, "Beer", amount=float(amount),kcalPerCG=49,GperOne=500)
        
class Quinoa(Ingredient):
    def __init__(self,amount):
        Ingredient.__init__(self, "Quinoa", amount=float(amount),kcalPerCG=365 ,GperOne=80)
        
class Prinzenrolle(Ingredient):
    def __init__(self,amount):
        Ingredient.__init__(self, "Prinzenrolle", amount=float(amount),kcalPerCG=492 ,GperOne=24)

class Pasta(Ingredient):
    def __init__(self,amount):
        Ingredient.__init__(self, "Pasta", amount=float(amount),kcalPerCG=359 ,GperOne=100)

class Gulasch(Ingredient):
    def __init__(self,amount):
        Ingredient.__init__(self, "Gulasch", amount=float(amount),kcalPerCG=150 ,GperOne=100)
        
IngredientList = {"RockstarLime":RockstarLime,"WildRice":WildRice,"WheatBread":WheatBread,
                  "PeanutButterCrunchy":PeanutButterCrunchy,"PhiladelphiaClassic":PhiladelphiaClassic,"FolEpiFine":FolEpiFine,
                  "Almonds":Almonds,"RedLenses":RedLenses,"Peas":Peas,
                  "PapricaRed":PapricaRed,"Onion":Onion,"Carot":Carot,
                  "Banana":Banana,"LindChocolateChili":LindChocolateChili,"FlaxSeed":FlaxSeed,
                  "QuarkLow":QuarkLow,"CherryJuice":CherryJuice,"MilkRice":MilkRice,
                  "Milk":Milk,"Raisins":Raisins,"Butter":Butter,
                  "Plums":Plums,"Sugar":Sugar,"Egg":Egg,
                  "Pretzel":Pretzel,"PretzelRing":PretzelRing,"Turkey":Turkey,
                  "Porree":Porree,"ChinaNoodles":ChinaNoodles,"RockstarRed":RockstarRed,
                  "Beer":Beer,"Quinoa":Quinoa,"RockstarGuava":RockstarGuava,"Prinzenrolle":Prinzenrolle,
                  "Gulasch":Gulasch,"Pasta":Pasta}
