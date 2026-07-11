#Author Myrtle 
#Date 07/04/2026
'''
Converting miles driven to gallon used
input enter miles driven
input gallons of uel used
MPG = miles driven / gallon
display the result of usafes of miles used per gallon.
'''
miles = input('Enter the miles driven:')
gallon = input('Enter the gallons of fuel used:')
result = float(miles) / float(gallon)
print('You used ', round(result, 2), 'miles per gallon. ')
