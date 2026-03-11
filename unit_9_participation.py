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