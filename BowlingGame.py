"""
Created on the 19 April 2022
@Author Dwain Aiolupotea
"""


class BowlingGame:

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
