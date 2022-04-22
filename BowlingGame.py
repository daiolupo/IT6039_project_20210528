"""
Created on the 19 April 2022
@Author Dwain Aiolupotea

BOWLING GAME
============

This bowling game source code is a 10pin bowling game prototype used to teach a variety of subjects.
This is the back end code of the program. There is no GUI and no system for receiving input data from files or a database.
After the backend has been developed and tested, the GUI and database will be developed.
"""


class BowlingGame:
    """
    Class created to track score of a bowling game

    Attributes:
    -----------
    rolls : [int]
        A Constructor that defines an array to store each roll for a frame

    Methods:
    --------
    roll(pins)
        A function that adds each roll to the rolls array

    score()
        Define the results. A function that calculates the score and returns a result

    is_strike(rollindex)
        A function that checks if there was a strike. If the score is equal to ten then it's a strike.

    is_spare(rollindex),
    strike_score(rollindex),
    strike_score(rollindex),
    spare_score(rollindex),
    frame_score(rollindex)
        A group of helper methods for checking. if there is a strike or if there is a spare. A method for Strike score, Spare score and frame score.
    """

    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        self.rolls.append(pins)

    def score(self):
        result = 0
        rollindex = 0
        for frameIndex in range(10):
            if self.is_strike(rollindex):
                result += self.strike_score(rollindex)
                rollindex += 1
            elif self.is_spare(rollindex):
                result += self.spare_score(rollindex)
                rollindex += 2
            else:
                result += self.frame_score(rollindex)
                rollindex += 2
        return result

    def is_strike(self, rollindex):
        return self.rolls[rollindex] == 10

    def is_spare(self, rollindex):
        return self.rolls[rollindex] + self.rolls[rollindex + 1] == 10

    def strike_score(self, rollindex):
        return 10 + self.rolls[rollindex + 1] + self.rolls[rollindex + 2]

    def spare_score(self, rollindex):
        return 10 + self.rolls[rollindex + 2]

    def frame_score(self, rollindex):
        return self.rolls[rollindex] + self.rolls[rollindex + 1]