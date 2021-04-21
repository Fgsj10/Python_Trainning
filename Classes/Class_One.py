"""
Author = Francisco Junior
"""

class Ball():
    "Printing color of ball"
    def changeColor(self, color):
        self.color = color

    def printingColor(self):
        print(self.color)




#Testing class
ball = Ball()
ball.changeColor("Blue")
ball.printingColor()
