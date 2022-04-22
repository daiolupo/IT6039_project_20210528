"""
Created on the 19 April 2022
@Author Dwain Aiolupotea
"""

import unittest
import BowlingGame

class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        self.game = BowlingGame.BowlingGame()

    def test_GutterGame(self):
        for i in range(0, 20):
            self.game.roll(0)
        self.assertEqual(self.game.score(), 0)

    def test_AllOnes(self):
        self.rollMany(1, 20)
        self.assertEqual(self.game.score(), 20)

    def test_OneSpare(self):
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(3)
        self.rollMany(0, 17)
        self.assertEqual(self.game.score(), 16)

    def test_OneStrike(self):
        self.game.roll(10)
        self.game.roll(4)
        self.game.roll(3)
        self.rollMany(0, 16)
        self.assertEqual(self.game.score(), 24)

    def test_PerfectGame(self):
        self.rollMany(10, 12)
        self.assertEqual(self.game.score(), 300)

    def test_OneSpare(self):
        self.rollMany(5, 21)
        self.assertEqual(self.game.score(), 150)

    def rollMany(self, pins, rolls):
        for i in range(rolls):
            self.game.roll(pins)

if __name__ == '__main__':
    unittest.main()
