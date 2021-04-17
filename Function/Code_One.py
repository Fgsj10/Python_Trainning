"""
Author = Francisco Junior
"""

#Creating function

def printingNumber(lines):
    for x in range(1,lines+1):
        for i in range(1, x+1):
            print (i),
        print()



#Creating variable and input data user
numberLines = int(input("Enter with a number lines: "))

#Printing line numbers
printingNumber(numberLines)



