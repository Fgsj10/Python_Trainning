"""
Author: Francisco Gomes
"""


#Received data user input
salary = float(input("Enter with you salary, please: "))

#Checking of increase money in salary

if(salary <= 280):
    print("You salary have increase of 20%")
    newIncrease = (salary * 0.20)
    print("You value of increase is: R$ %.2f" %(newIncrease))
    newSalary = (salary + (newIncrease))
    print("You final salary is: R$ %.2f " %(newSalary));
elif(salary > 280 and salary <= 700):
    print("You salary have increase of 15%")
    newIncrease = (salary * 0.15)
    print("You value of increase is: R$ %.2f" %(newIncrease))
    newSalary = (salary + (newIncrease))
    print("you final salary is: R$ %.2f" %(newSalary))
elif(salary > 700 and salary <= 1500):
    print("You salary have increase of 10%")
    newIncrease = (salary * 0.10)
    print("You value of increase is: R$ %.2f" %(newIncrease))
    newSalary = (salary + (newIncrease))
    print("You salary final is: R$ %.2f " %(newSalary))
elif(salary > 1500):
    print("You salary have increase of 5%")
    newIncrease = (salary * 0.05)
    print("You value of increase is: R$ %.2f" %(newIncrease))
    newSalary = (salary + newIncrease)
    print("You salary final is: R$ %.2f " %(newSalary))




