"""
Author = Francisco Junior
"""

#Creating class

class Rectangle():
    "Structure of rectangle"

    def __init__(self, base, height):
        self.setBase(base)
        self.setHeight(height)

    def setBase(self, base):
        self.setBase = base

    def getBase(self):
        return self.base

    #Now for height

    def setHeight(self, height):
        self.height = height

    def getHeight(self):
        return self.height

    def calculateArea(self):
        return self.base * self.height

    def perimeterRectangle(self):
        return 2 * self.base + 2 * self.height


#Testing the class

base = int(input("Enter with base: "))
height = int(input("Enter with height: "))
rectangle = Rectangle(base,height)

print("You area is: ",rectangle.calculateArea())


