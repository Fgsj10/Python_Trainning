"""
Author: Francisco Gomes
"""

#Variables and received number
numberOne = int(input("Enter with number one: "))
numberTwo = int(input("Enter with number two: "))
numberThree = float(input("Enter with a number three: "))

#Operations and mathematical

firstOperation = (numberOne * 2) * (numberTwo / 2)

secondOperation = (numberOne * 3) + (numberThree)

thirdOperation = (numberThree ** 3)

#Printing values
print("First operation is: %.2f " %(firstOperation))

print("Second operation is: %.2f " %(secondOperation))

print("Third operation is: %.2f " %(thirdOperation))
