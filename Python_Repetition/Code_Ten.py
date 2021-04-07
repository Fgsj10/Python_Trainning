"""
Author = Francisco Junior
"""

#Variables and user received input data

number = int(input("Enter with number: "))

#Structure repetition for calculate values

for x in range(0,11):
    print("%d X %d = %d" %(number, x, number*x))
