"""
Author: Francisco Gomes
"""

#Creating variables and received user input
hoursWorkValue = float(input("Enter with value for hour work: "))
hoursLabourMonth = int(input("Enter with amount hours in month: "))

#Calculating values and operations discount under salary

#Salary brute
salaryBrute = (hoursWorkValue * hoursLabourMonth)

#Printing salary brute
print("Your salary brute is: R$ %.2f " %(salaryBrute))

#IR
ir = (salaryBrute * 0.11)

#INSS
inss = (salaryBrute * 0.08)

#Sindicate
sindicate = (salaryBrute * 0.05)

#Printing discounts
print("Discount IR = R$ %.2f " %(ir))
print("Discount INSS = R$ %.2f " %(inss))
print("Discount Sindicate = R$ %.2f " %(sindicate))

#Calculating salary liquid
salaryLiquid = (salaryBrute - (ir + inss + sindicate))

#printing salary liquid
print("Your salary liquid is: R$ %.2f " %(salaryLiquid))

