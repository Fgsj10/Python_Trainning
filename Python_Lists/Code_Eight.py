"""
Author = Francisco Junior
"""



#Variables and received input data user
valuesList = []
listDoublesNumbers = []


#Structure for adding values in list

for x in range(0,10):
    number = int(input("Enter with a number: "))
    valuesList.append(number)



#Printing list of numbers

print("List of numbers is: ", valuesList)


#Calculating numbers of doubles

for x in valuesList:
    numberDouble = (x ** 2)
    listDoublesNumbers.append(numberDouble)

print("List of numbers double is: ",listDoublesNumbers)

sumNumbers = 0


#Sum of numbers in list
for x in listDoublesNumbers:
    sumNumbers += x


#Printing numbers of list
print("List numbers sum of double: ",sumNumbers)


