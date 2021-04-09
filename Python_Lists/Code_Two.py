"""
Author = Francisco Junior
"""

#Received data user input
listNumbers = []

#Structure repetition for add number in list
for x in range(0,10):
    number = int(input("Enter with a number: "))
    listNumbers.append(number)

print("List original is: ", listNumbers)

#Reverting numbers in list
listNumbers.reverse()

print("List inverse of numbers is: ", listNumbers)



