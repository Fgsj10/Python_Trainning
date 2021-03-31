"""
Author: Francisco Gomes
"""


#creating variables and data user input received
letter = str(input("Digit one letter: "))

#Converter letter for minuscule
converterLetter = letter.lower()

#checking letter if consonant or vogal
if(converterLetter == "a" or converterLetter == "e" or converterLetter == "i" or converterLetter == "o" or converterLetter == "u"):
    print("Letter is vogal")
    print(converterLetter)
else:
    print("Letter is consonant")
    print(converterLetter)