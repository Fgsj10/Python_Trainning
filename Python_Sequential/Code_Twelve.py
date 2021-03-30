"""
Author: Francisco Gomes
"""


#Creating variables
height = float(input("Enter with you height: "))

#Calculating weight ideal
weightIdealMan = (72.7 * height) - 58
weightIdealWomen = (62.1 * height) - 44.7

#Printing values of weight ideal

print("Weight ideal for man is: %.2f " %(weightIdealMan), "kg")
print("Weight ideal for women is: %.2f " %(weightIdealWomen), "kg")


