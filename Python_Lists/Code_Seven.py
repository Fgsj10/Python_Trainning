"""
Author = Francisco Junior
"""

#Creating lists of structure for adding values
listAge = []
listHeight = []

#Structure repetition for add values in lists
for x in range(0,5):
    age = int(input("Enter with you age = "))
    listAge.append(age)
    height = float(input("Enter with you height: "))
    listHeight.append(height)

#Printing lists with values ordened
print("List of ages is: ", listAge)
print("List of Height is: ", listHeight)


#Printing lists of values inversed
print(listAge[::-1])
print(listHeight[::-1])


