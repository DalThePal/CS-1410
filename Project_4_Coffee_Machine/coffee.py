VALID_AMOUNTS = [5, 10, 25, 50]


class CoffeeMachine():
    def __init__(self):
        self._cashBox   = CashBox()
        self._selector  = Selector(self._cashBox)
        
    def oneAction(self):
        print("______________________________________")
        print("    PRODUCT LIST: all 35 cents, except bouillon (25 cents)")
        print("    1=black, 2=white, 3=sweet, 4=white & sweet, 5=bouillon")
        print("    Sample commands: insert 25, select 1")
        command = input(">>> Your command: ")
        command = command.split(" ")
        
        if command[0] == "select":
            selection = None
            if not len(command) > 1:
                print("INPUT ERROR >>>")
                print("You didn't select anything.")
            else:
                selection = int(command[1])
                
                if selection in range(1, 6):
                    self._selector.select(selection)
                else:
                    print("INPUT ERROR >>>")
                    print(f"{selection} is not a product.")
            
        elif command[0] == "insert":
            amount = None
            if not len(command) > 1:
                print("INPUT ERROR >>>")
                print("You didn't insert anything.")
            else:
                amount = int(command[1])
              
                if amount in VALID_AMOUNTS:
                    self._cashBox.deposit(amount)
                else:
                    print("INPUT ERROR >>>")
                    print("We only take half-dollars, quarters, dimes, and nickels.")
                    print("Coin(s) returned")            
            
        elif command[0] == "cancel":
            self._cashBox.returnCoins()
            
        elif command[0] == "quit":
            return False
            
        else:
            print("Invalid command")
            
        return True
        
    def totalCash(self):
        return self._cashBox.total()
    
               
class CashBox():
    def __init__(self):
        self._credit        = 0
        self._totalReceived = 0
        
    def deposit(self, amount):
        self._credit += amount
        self._totalReceived += amount
        print(f"Depositing ${amount/100:.2f}.  You have ${self._credit/100:.2f} credit.")
        
    def returnCoins(self):
        print(f"Returning ${self._credit/100:.2f}.")
    
    def haveYou(self, amount):
        return amount <= self._credit
        
    def deduct(self, amount):
        self._totalReceived += amount
        self._credit -= amount
        self.returnCoins()
        
    def total(self):
        return self._totalReceived
        

class Selector():
    def __init__(self, cashBox):
        self._cashBox   = cashBox
        self._products  = {
            1: Product("black", 35, ["cup", "coffee", "water"]),
            2: Product("white", 35, ["cup", "coffee", "creamer", "water"]),
            3: Product("sweet", 35, ["cup", "coffee", "sugar", "water"]),
            4: Product("white & sweet", 35, ["cup", "coffee", "sugar", "creamer", "water"]),
            5: Product("bouillon", 25, ["cup", "bouillonPowder", "water"])
        }
        
    def select(self, choiceIndex):
        product = self._products[choiceIndex]
        price = product.getPrice()
        have = self._cashBox.haveYou(price)
        
        if have:
            product.make()
            self._cashBox.deduct(price)
        else:
            print("Sorry. Not enough money deposited.")


class Product():
    def __init__(self, name, price, recipe):
        self._name      = name
        self._price     = price
        self._recipe    = recipe
        
    def getPrice(self):
        return self._price
        
    def make(self):
        for item in self._recipe:
            print(f"\tDispensing {item}")


def main():
    m = CoffeeMachine()
    while m.oneAction():
        pass
    total = m.totalCash()
    print(f"Total Cash: ${total/100:.2f}")
    
    
if __name__ == "__main__":
    main()