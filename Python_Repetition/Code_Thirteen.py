"""
Author = Francisco Junior
"""

#Variables and user received input data

number = int(input("Enter with a number: "))


#Structure of calculate numbers valid and rule business
while (number < 0 or number > 1000):
    print("Number invalid, try again")
    number = int(input("Enter with a new number: "))

#Printing number final
print("Number final between 0 and 1000 is: %d " %(number))


