"""
Author = Francisco junior
"""

#Variables and user data input

name = str(input("Enter with a name: "))
while(len(name) <= 3):
    print("Name invalid, with must 3 caracteres")
    name = str(input("Enter with you name: "))

print("------------------------------------------------------")


age = int(input("Enter with a age: "))
while (age < 0 or age > 150):
    print("Age invalid, try again")
    age = int(input("Enter with you age: "))

print("------------------------------------------------------")

salary = float(input("Enter with a salary: "))
while(salary < 0):
    print("Salary is invalid, try again")
    salary = float(input("Enter with you salary: "))

print("------------------------------------------------------")

gender = str(input("Enter with you gender: "))

#converter letter
genderMinuscule = gender.lower()

while(genderMinuscule != "m" and genderMinuscule != "f"):
    print("Gender invalid")
    gender = str(input("Enter with you gender, again: "))
    genderMinuscule = gender.lower()

print("------------------------------------------------------")


stateCivil = str(input("Enter with you state civil: "))
stateCivilConverter = stateCivil.lower()
while (stateCivilConverter != "s" and stateCivilConverter != "c" and stateCivilConverter != "v" and stateCivilConverter != "d"):
    print("State civil invalid")
    stateCivil = str(input("Enter with you again state civil: "))
    stateCivilConverter = stateCivil.lower()




