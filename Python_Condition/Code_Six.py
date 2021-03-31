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


#Second method

if(numberOne > numberTwo and numberOne > numberThree):
    print("number One")
    print(numberOne)
elif(numberTwo > numberThree and numberTwo > numberOne):
    print("number Two")
    print(numberTwo)
elif(numberThree > numberOne and numberThree > numberTwo):
    print("number three")
    print(numberThree)
