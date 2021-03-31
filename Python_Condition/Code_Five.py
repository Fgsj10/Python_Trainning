"""
Author: Francisco Gomes
"""


#creating variables and data user input received

noteOne = float(input("Enter with first note: "))
noteTwo = float(input("Enter with second note: "))

#Calculating average
average = (noteOne + noteTwo) / 2;

print("You average is partial %.2f " %(average))

#Checking values of average
if(average == 10.0):
    print("Aproved with distinction")
    print("Average is %.2f " %(average))
elif(average < 7.0 and average > 0):
    print("Reproved")
    print("Average is: %.2f " %(average))
elif(average >= 7 and average < 9.9):
    print("Aproved")
    print("Average is: %.2f " %(average))
else:
    print("Average is invalid")
    print("Average  < 0")



