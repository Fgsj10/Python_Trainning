"""
Aauthor = Francisco junior
"""

#Variables and input data user

listA = []
listB = []
listC = []

#Adding values in list A, B and C

for x in range(0,10):
    numberA = int(input("Enter with value in list A: "))
    listA.append(numberA)


for x in range(0,10):
    numberB = int(input("Enter with value in list B: "))
    listB.append(numberB)

#Printing lists with values
print("Values in list A: ", listA)

print("Values in list B: ", listB)


#Adding numbers in list in sort intercaled
for x in listA,listB:
    listC.append(x)

print("Values of in list C: ", listC)







