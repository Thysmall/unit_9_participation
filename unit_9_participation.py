"""
Name: Unit 9 Participation Activity: Dice
Author: Jordan Betz
Description: Class based dice rolling program
Date: 3/11/2026
"""
from random import randint

class Die():
    def __init__(self, sides: int):
        self.sides = sides
        
    def roll_die(self):
        roll: int = randint(1,self.sides)
        print(f"You rolled a {roll} on a {die_1.sides} sided die")
        
    
if __name__ == "__main__":
    die_1: Die = Die(6)
    die_2: Die = Die(10)
    die_3: Die = Die(20)
    