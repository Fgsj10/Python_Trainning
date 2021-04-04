"""
Author = Francisco Junior
"""

#variables for received data input user
maior = 0
for x in range(0,5):
    number = float(input("Enter with number: "))
    if(number > maior):
        maior = number
        print("Bigger number is: %d" % (maior))

print("Bigger number is: %d" %(maior))