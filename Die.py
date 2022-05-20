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


# testing code
# please do not edit
myd = Die(6)
md = myd.rollMultiple(1000)
if type(myd.roll()) is int:
    print("test 1 pass")
if len(md) == 1000:
    print("test 2 pass")
if max(md) == 6:
    print("test 3 pass")
if min(md) == 1:
    print("test 4 pass")
if myd.getSides() == 6:
    print("test 5 pass")
