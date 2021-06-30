from dice.IDice import IDice
import random
class CrookedDice(IDice):

    def __init__(self):
        self.diceSides=[*range(1,7,2)]

    def RollDice(self):
        random.shuffle(self.diceSides)
        return self.diceSides[0]