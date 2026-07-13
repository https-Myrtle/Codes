#Author Myrtle
#Date 07/13/2026
'''
INPUT food
tip = food * 0.18
tax = food * 0.07
total = food + tip + tax
DISPLAY tip, tax, total
'''
food = float(input('Enter the charge for food: '))
tip = food * 18 / 100
tax = food * 7 / 100
total = tip + tax + food
print('Tip: $', round(tip, 2))
print('tax: $', round(tax, 2))
print('Total: $', round(total, 2))
