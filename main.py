"""
Created on the 19 April 2022
@Author Dwain Aiolupotea

BOWLING GAME
============

This bowling game source code is a 10pin bowling game prototype used to teach a variety of subjects.
The source code was developed for testing using unittest framework module.
"""

import unittest
import BowlingGame

class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        """
        First initial test to create a bowling game

        Methods:
        --------
        test_GutterGame(self)
            A function that tests gutter games with all zero scores. Assert to check the score equals to 0

        test_AllOnes(self)
             A Function that tests all one scores with a roll of 20 times. Assert to check the score equals to 20

        test_OneSpare(self)
            A Function that tests one spare roll. Assert to check the score equals to 16

        test_OneStrike(self)
            A function to test a strike. An Assert to check the score equals to 24

        test_PerfectGame(self)
            A function to test a perfect game with 10 rolls. Assert to check that the score equals to 300

        test_AllSpares(self)
            A function to test all spares. Assert to check that the score equals to 150

        rollMany(self, pins, rolls)
            A function to for many rolls.
        """

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

    def test_AllSpares(self):
        self.rollMany(5, 21)
        self.assertEqual(self.game.score(), 150)

    def rollMany(self, pins, rolls):
        for i in range(rolls):
            self.game.roll(pins)

if __name__ == '__main__':
    unittest.main()
