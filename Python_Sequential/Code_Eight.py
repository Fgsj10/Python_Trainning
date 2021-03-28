"""
Author: Francisco Gomes
"""

#Variable received value of user input

valueHourWorker = float(input("Enter with value of hour labour: $ "))
hoursWorkMonth = int(input("Enter with hours worked in month: "))

#Calculating salary brute in month
salaryBrute = (valueHourWorker * hoursWorkMonth)

#Printing values final

print("You salary brute is: $ %.2f " %(salaryBrute))

