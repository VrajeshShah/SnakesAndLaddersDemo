import unittest
from dice.CrookedDice import CrookedDice

class TestCrookedDice(unittest.TestCase):

    def test_crookedDiceInstance(self):
        dice=CrookedDice()
        self.assertIsInstance(dice.RollDice(), int)
    
    def test_crookedDiceValue(self):
        dice=CrookedDice()
        diceValue=dice.RollDice()
        self.assertEqual(diceValue%2, 1)

if __name__ == '__main__':
    unittest.main()