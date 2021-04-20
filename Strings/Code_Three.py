"""
Author = Francisco Gomes
"""

#Variables and data user input

name = str(input("Name: "))

#Printing name sorted
print("Name is: ", name)

#Printing in format vertical
for x in name:
    print(x[::1])
