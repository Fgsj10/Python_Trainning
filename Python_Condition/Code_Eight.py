"""
Author: Francisco Gomes
"""

#Received data of user input
shift = str(input("Enter with you shift work: "))

#Converter content of shift for minuscule
converterShift = shift.lower();

#Checking what shift you labour

if(converterShift == "m"):
    print("You shift is Morning")
elif(converterShift == "a"):
    print("You shift is afternoon")
elif(converterShift == "n"):
    print("You shift is night")
else:
    print("You shift is invalid")



