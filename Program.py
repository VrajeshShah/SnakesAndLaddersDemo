# from dice.CrookedDice import CrookedDice
from dice.CrookedDice import CrookedDice
from SnakesAndLaddersBoard import SnakesAndLaddersBoard
from dice.NormalDice import NormalDice
from random import randint
import CustomLogger
logger=CustomLogger.GetLogger()
try:

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
except Exception as ex:
    print("Something Wrong Happened!!Please Check The Logs!!")
    logger.critical(ex)
