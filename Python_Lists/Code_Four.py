"""
Author = Francisco Gomes
"""

#Variables and lists for input data received user

listLetters = [] #list empty of full letters
listConsonant = [] #list empty for letters consonant


#Structure repetition for input letters

for x in range(0,10):
    letter = str(input("Enter with a you letter: "))
    if(letter != "a" and letter != "e" and letter != "i" and letter != "o" and letter != "u"):
        listConsonant.append(letter)



#Printing lists of letters and consonant

print("List of letters consonant = ", listConsonant)





