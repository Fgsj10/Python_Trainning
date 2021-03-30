"""
Author: Francisco Gomes
"""

#Received data of user input
weightFish = int(input("Enter with fish weight: "))

#Calculating tax of weight fish
if(weightFish > 50):
    excessFishWeigh = weightFish - 50
    taxFishWeight = (excessFishWeigh * 4)

#Printing value of tax fish weight

print("Tax of payment of excess weight is: R$ %.2f " %(taxFishWeight))

