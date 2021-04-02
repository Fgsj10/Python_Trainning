"""
Author = Francisco junior
"""

#Received data user input
name = str(input("Enter with you name: "))
password = str(input("Enter with you password: "))

while (name == password):
    print("Name or password invalid")
    print("Name is required different of password")
    name = str(input("Again please name : "))
    password = str(input("Again please password: "))

#Printing name and password

print("You name user is: ", name)
print("You password is: ", password)





