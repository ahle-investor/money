from datetime import datetime

class 

class Saving:
    def __init__(self, amount, interest):
        self.amount   = amount
        self.interest = interest
    def open(self, start):
        self.start = start

    def getInterest(self):
        pass


class Asset:
    pass




livretA = Saving(22000, 0.03)
livretA.open(datetime.now())
print(livretA)
