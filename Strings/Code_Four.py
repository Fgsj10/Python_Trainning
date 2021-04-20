"""
Author = Francisco Gomes
"""

#User data input and variables

print("Validating number cellphone")

number = str(input("Enter with a number: "))

phoneFormated = number.replace("-", "")

#Checking of number cellphone is validate

if(len(phoneFormated) == 7):
    print("Cellphone with 7 digits, adding number 3 in front")
    #Printing cellphone not formated
    print("Cellphone not formated is: 3%s " %(phoneFormated))
    #Printing cellphone with formated
    print("Cellphone with formated is: 3%s " %(number))

