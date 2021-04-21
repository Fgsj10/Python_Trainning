"""
Author = Francisco Gomes
"""

class Squat():
    "printing values of side"
    def __init__(self, side):
        self.setSide(side)

    def setSide(self, side):
        self.side = side

    def getSide(self):
        return self.side

    def calculateArea(self):
        return self.side * self.side


#Testing and values of class

squat = Squat(5)
#Printing area calculate of squat
print(squat.calculateArea())


squat.setSide(10)
print(squat.calculateArea())
