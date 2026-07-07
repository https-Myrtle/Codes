#Author Myrtle Argote
#Date 07/07/2026

'''
Celsius to Fahrenheit

input enter a celsius temeprature

formula = 9/5 * C + 32

display C = to formula #round it by 2 decimal places

'''
celcius = float(input('Enter a Celsius temperature: '))

formula = float(9/5) * float(celcius) + float(32)

print(round(celcius, 2), 'C = ', round(formula, 2), 'F')
