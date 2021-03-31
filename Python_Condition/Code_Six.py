"""
Author: Francisco Gomes
"""


#creating variables and data user input received
numberOne = float(input("Number one: "))
numberTwo = float(input("Number two: "))
numberThree = float(input("Number three: "))

#With function
firstBiggerNumber = max(numberOne, numberTwo, numberThree)

#printing bigger number
print("Bigger number is: %.2f " %(firstBiggerNumber))

