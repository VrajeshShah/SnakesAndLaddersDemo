# from dice.CrookedDice import CrookedDice
from dice.CrookedDice import CrookedDice
from SnakesAndLaddersBoard import SnakesAndLaddersBoard
from dice.NormalDice import NormalDice
from random import randint


crookedDice=CrookedDice()
normalDice=NormalDice()

board=SnakesAndLaddersBoard("data/Game1.json")

while(1):
    instructions="""

        1. Play a Move.
        2. Print the Board.
        3. Quit.

    """
    print(instructions)
    n=int(input())
    if n==1:
        randomValue=randint(1,2)
        if randomValue==1:
            board.Play(crookedDice)
        else:
            board.Play(normalDice)
    elif n==2:
        board.PrintBoard()
    elif n==3:
        break
    else:
        continue
