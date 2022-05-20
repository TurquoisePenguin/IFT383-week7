#!/usr/bin/python

# your class definition goes here
class Die(object):
        sides = 0

        #constructor
        def __init__(self, sides=6):
                self.sides = sides

        #returns a randomly rolled number
        def roll(self):
                import random
                return random.randint(1,self.sides)

        #returns a list of n rolls
        def rollMultiple(self, number):
                rolls = []
                for i in range(number):
                        rolls.append(self.roll())
                return rolls

        #getter sides
        def getSides(self):
                return self.sides

class Coin(Die):
        #constructor (always 2 sides)
        def __init__(self):
            self.sides = 2

        #returns "HEADS" if 1 and "TAILS" if 2
        def flip(self):
                temp = self.roll()
                if self.roll() == 1:
                        return "HEADS"
                else:
                        return "TAILS"

# testing code
# please do not edit
myCoin = Coin()
if myCoin.roll() > 0 and myCoin.roll() < 3:
    print("test 1 pass")
resFlip = myCoin.flip()
if resFlip == 'HEADS' or resFlip == "TAILS":
    print("test 2 pass")

