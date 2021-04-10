"""
Author = Francisco junior
"""

#Structure of received numbers

listNumbers = []
listSumNumbers = 0
listNumbersMultiplication = 1

#Repetition structure for input data

for x in range(0,5):
    number = int(input("Enter with a number: "))
    listNumbers.append(number)


#New structure for calculate sum of numbers

for x in listNumbers:
    listSumNumbers += x

#Structure for multiplication numbers

for x in listNumbers:
    listNumbersMultiplication *= x



#Printing sum of numbers
print("Sum of numbers is: %d " %(listSumNumbers))

print("Numbers multiplication is: %d " %(listNumbersMultiplication))



