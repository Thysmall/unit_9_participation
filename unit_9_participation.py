"""
Name: Unit 9 Participation Activity: Dice
Author: Jordan Betz
Description: Class based dice rolling program
Date: 3/11/2026
Classes: 
    Die: Used to create and roll a die with a provided number of sides
        Attributes: 
            sides (int): Number of sides on the die
        Methods: 
            roll_die(): Prints the roll of a die with provided sides
"""
from random import randint

class Die(object):
    """Used to create and roll a die with a provided number of sides
    
    Attributes:
        sides (int): specified number of sides on die 
    """
    def __init__(self, sides: int):
        """Constructor for die

        Args:
            sides (int): specified number of sides on die
        """
        self.sides: int = sides
        
    def roll_die(self):
        """Rolls die using own sides value as max and prints result
        """
        roll: int = randint(1,self.sides)
        print(f"You rolled a {roll} on a {self.sides} sided die")
        
    
if __name__ == "__main__":
    die_1: Die = Die(6)
    die_2: Die = Die(10)
    die_3: Die = Die(20)
    dice: list[Die] = [die_1, die_2, die_3]
    for die in dice:
        for _ in range(10):
            die.roll_die()
    