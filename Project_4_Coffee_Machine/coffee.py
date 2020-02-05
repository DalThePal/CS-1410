
class CoffeeMachine():
    def __init__(self):
        self._cashBox   = CashBox()
        self._selector  = Selector()
        
    def oneAction():
        print("TODO: oneAction")
        
    def totalCash():
        print("TODO: totalCash")
        
        
class CashBox():
    def __init__(self):
        self._credit        = 0
        self._totalReceived = 0
        
    def deposit(self, amount):
        print('TODO: deposit')
        
    def returnCoins(self):
        print("TODO: returnCoins")
    
    def haveYou(self, amount):
        print("TODO: haveYou, returns type bool")
        
    def deduct(self, amount):
        print("TODO: deduct")
        
    def total(self):
        print("TODO: total, returns type int")
        

class Selector():
    def __init__(self):
        self._cashBox   = CashBox()
        self._products  = []
        
    def select(self, choiceIndex):
        print("TODO: select")



class Product():
    def __init__(self):
        self._name      = ""
        self._price     = 0,
        self._recipe    = ["", "", ""]
        
    def getPrice():
        print("TODO: getPrice, returns type int")
        
    def make():
        print("TODO: make")


def main():
    
    
    
if __name__ == "__main__":
    main()