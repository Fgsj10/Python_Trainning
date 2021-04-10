"""
Author = Francisco Junior
"""

#Lists of numbers

listNumbers = []
listNumberPair = []
listNumberOdd = []



#Structure repetition for input data received
for x in range(0,20):
    number = int(input("Enter with a number: "))
    listNumbers.append(number)

#Printing first list with all numbers
print("List final numbers is: ",listNumbers)

#Searching and adding numbers in list pair or odd

for x in listNumbers:
    if (x % 2 == 0):
        listNumberPair.append(x)
    else:
        listNumberOdd.append(x)

#Printing lists of numbers pair and Odd
print("List of numbers pair is: ", listNumberPair)

print("List of numbers odd is: ", listNumberOdd)










