"""
Author = Francisco junior
"""

#First variable for user data input

note = float(input("Enter with note: "))

#checking value required
while (note < 0 or note > 10):
    print("Note invalid, try again")
    print("note required > 0 and < 10")
    note = float(input("Enter with note again: "))

#Printing note final

print("You Final note is: %.2f" %(note))