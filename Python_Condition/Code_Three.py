"""
Author: Francisco Gomes
"""


#creating variables and data user input received

letter = str(input("Enter with value F-Female or M-Male: "))

#Converting letter for minuscule

converterLetter = letter.lower();

#printing letter minuscule
print("A letter is: %s" %(converterLetter))

if(converterLetter == "f"):
    print("Female")
elif (converterLetter == "m"):
    print("Male")
else:
    print("Gender invalid")