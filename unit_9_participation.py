"""
Name: Unit 9 Participation Activity: Dice
Author: Jordan Betz
Description: Class based dice rolling program
Date: 3/11/2026
"""
from random import randint

class Die():
    def __init__(self, faceCount: int):
        self.faceCount = faceCount
        
    def roll_die(self):
        return randint(1,self.faceCount)
    
if __name__ == "__main__":
    die_1: Die = Die(6)
    print(f"You rolled a {die_1.roll_die()} on a {die_1.faceCount} sided die")
    die_2: Die = Die(100)
    print(f"You rolled a {die_2.roll_die()} on a {die_2.faceCount} sided die")