import unittest
from dice.NormalDice import NormalDice

class TestNormalDice(unittest.TestCase):
    def testNormalDiceInstance(self):
        dice=NormalDice()
        self.assertIsInstance(dice.RollDice(), int)
 
if __name__ == '__main__':
    unittest.main()
