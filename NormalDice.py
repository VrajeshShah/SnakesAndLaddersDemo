from IDice import IDice


import random
class NormalDice(IDice):

    def __init__(self):
        self.diceSides=[*range(1,7,1)]

    def RollDice(self):
        random.shuffle(self.diceSides)
        return self.diceSides[0]