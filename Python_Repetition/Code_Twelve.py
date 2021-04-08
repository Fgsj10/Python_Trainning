"""
Author = Francisco Junior
"""

#Variables and received user data input

countPair = 0
countOdd = 0

for x in range(0,10):
    number = int(input("Enter with a number: "))
    if(number % 2 == 0):
        countPair += 1
    else:
        countOdd += 1

print("Amount numbers pair is: %d " %(countPair))
print("Amount numbers odd is: %d " %(countOdd))




