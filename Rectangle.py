#!/usr/bin/python
class Rectangle(object):
    # complete the class definition as described
	length = 0
	width = 0

	#constructor
	def __init__(self, length, width):
		if type(length) is int:
			self.length = length
		if type(width) is int:
			self.width = width

	#Returns length
	def getLength(self):
		return self.length

	#returns width
	def getWidth(self):
		return self.width

	#returns the area
	def getArea(self):
		return (self.length*self.width)

	#returns True if object is square
	def isSquare(self):
		return (self.length == self.width)

	#Overload "=="
	def __eq__(self, other):
		if self.length == other.getLength() and self.width == other.getWidth():
			return True
		elif self.length == other.getWidth() and self.width == other.getLength():
			return True
		else:
			return False

# This code tests the functionality of your Rectangle class
if __name__ == '__main__':
    rect1 = Rectangle(10,10)
    rect2 = Rectangle(10,10)
    rect3 = Rectangle(10,15)
    if rect1 == rect2:
        print("Test 1 pass")
    if rect1.isSquare():
        print("Test 2 pass")
    if rect3 == rect1:
        print("Test 3 FAIL")
    else:
        print("Test 3 pass")
