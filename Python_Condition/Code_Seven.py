"""
Author: Francisco Gomes
"""


#Variables and received data user input

numberOne = float(input("Number one: "))
numberTwo = float(input("Number Two: "))
numberThree = float(input("Number Three: "))


#Method of checking bigger and small numbers

biggerNumber = max(numberOne, numberTwo, numberThree)
smallerNumber = min(numberOne, numberTwo, numberThree)

#Printing values with first method
print("Bigger number is: %.2f " %(biggerNumber))
print("Smaller number is: %.2f " %(smallerNumber))


#Checking value with second conditions
if(numberOne > numberTwo and numberOne > numberThree and numberTwo > numberThree):
    print("Bigger number is number one : ", numberOne)
    print("Smaller number is number three : ", numberThree)
elif(numberOne > numberTwo and numberOne > numberThree and numberThree > numberTwo):
    print("Bigger number is number one : ", numberOne)
    print("Smaller number is number two : ", numberTwo)
elif(numberTwo > numberThree and numberTwo > numberOne and numberOne > numberThree):
    print("Bigger number is number two : ", numberTwo)
    print("Smaller number is number three : ", numberThree)
elif(numberTwo > numberThree and numberTwo > numberOne and numberThree > numberOne):
    print("Bigger number is two : ", numberTwo)
    print("Smaller number is one : ", numberOne)
elif(numberThree > numberOne and numberThree > numberTwo and numberOne > numberTwo):
    print("Bigger number is number three : ", numberThree)
    print("Smaller number is number two : ", numberTwo)
elif(numberThree > numberOne and numberThree > numberTwo and numberTwo > numberOne):
    print("Bigger number is number three : ", numberThree)
    print("Smaller number is number one : ", numberOne)






