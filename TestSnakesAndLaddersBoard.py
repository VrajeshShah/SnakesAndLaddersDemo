from SnakesAndLaddersBoard import SnakesAndLaddersBoard
import unittest

class TestSnakesAndLaddersBoard(unittest.TestCase):    
    def testDiceGraterThenNormalLimit(self):
        self.board=SnakesAndLaddersBoard("data/Game1.json")
        self.board.playerPosition=95
        self.board.PlayGame(6)
        self.assertEqual(self.board.playerPosition, self.board.playerPosition)

    def testDiceEqualToNormalLimit(self):
        self.board=SnakesAndLaddersBoard("data/Game1.json")
        self.board.playerPosition=94
        self.board.PlayGame(6)
        self.assertEqual(self.board.playerPosition, 100)
    
    def testSnakeWorking(self):
        self.board=SnakesAndLaddersBoard("data/Game1.json")
        self.board.playerPosition=13
        self.board.PlayGame(1)
        self.assertEqual(self.board.playerPosition, 7)

    def testLadderWorking(self):
        self.board=SnakesAndLaddersBoard("data/Game1.json")
        self.board.playerPosition=5
        self.board.PlayGame(1)
        self.assertEqual(self.board.playerPosition,33)

    def testNormalWorking(self):
        self.board=SnakesAndLaddersBoard("data/Game1.json")
        self.board.playerPosition=4
        self.board.PlayGame(1)
        self.assertEqual(self.board.playerPosition,5)
        
 

if __name__ == '__main__':
    unittest.main()