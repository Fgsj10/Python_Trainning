"""
Author: Francisco Gomes
"""

#Data Received of user input

numberOne = float(input("Enter with first number: "))
numberTwo = float(input("Enter with second number: "))

#Operations
print("1 - Number pair or odd? ")
print("2 - Number positive or negative? ")
print("3 - number integer or decimal? ")

#Input of operation user selected
operation = int(input("User, please select one operation: "))


if(operation == 1):
    if(numberOne % 2 == 0):
        print("number one is pair")
    elif(numberOne % 2 == 1):
        print("number one is odd")
    if(numberTwo % 2 == 1):
        print("Number two is odd")
    else:
        print("number two is pair")

if(operation == 2):
    if(numberOne < 0):
        print("number one negative")
    elif(numberOne > 0):
        print("number one positive")
    if(numberTwo < 0):
        print("number two is negative")
    else:
        print("number two is positive")