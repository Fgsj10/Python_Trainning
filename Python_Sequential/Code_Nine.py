"""
Author: Francisco Gomes
"""


#Variables
temperatureFarenheit = float(input("Enter with temperature em Fº: "))


#Calculating and converting value
converterTemperature = 5 * ((temperatureFarenheit-32) / 9)


#Printing temperature converted
print("Temperature Fº -> Cº = %.2f " %(converterTemperature), "Cº")



