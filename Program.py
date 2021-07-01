# from dice.CrookedDice import CrookedDice
from SnakesAndLaddersBoard import SnakesAndLaddersBoard


# a=CrookedDice()
# for i in range(10):
#     print(a.RollDice())
# gameData=JsonOperations.JsonToObject("data/Game1.json")
# print(gameData)

board=SnakesAndLaddersBoard("data/Game1.json")
board.PrintBoard()