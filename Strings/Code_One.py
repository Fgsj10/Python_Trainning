"""
Author = Francisco Gomes
"""

#Variables and input data user

wordFirst = str(input("First string please: "))
wordSecond = str(input("Second string please: "))


#Structure under strings

#Printing the strings
print("First string is: ", wordFirst)
print("Seconde string is: ", wordSecond)

#Calculating you content length

print("Length of first string is: ", len(wordFirst))
print("Length of second string is: ", len(wordSecond))

#Checking of two values is equals of length
if(len(wordFirst) == len(wordSecond)):
    print("Values and length is equals")
else:
    print("Values and length not equals")



