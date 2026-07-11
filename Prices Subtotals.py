#author Myrtle 
#07/03/2026
'''
input prices 1 - 5
subtotal is prices of 1 - 5
sales tax is subtotal * 0.07
result is subtotal + subtotal
print answer
Everything is supposed to be rounded it into 2 decimals
'''
value_1 = input('Enter the price of item #1: ')
value_2 = input('Enter the price of item #2: ')
value_3 = input('Enter the price of item #3: ')
value_4 = input('Enter the price of item #4: ')
value_5 = input('Enter the price of item #5: ')

subtotal = float(value_1) + float(value_2) + float(value_3) + float(value_4) + float(value_5)
print('Subtotal:', round(subtotal, 2))

sales_tax = float(subtotal) * 7 / 100
print('Sales Tax:', round(sales_tax, 2))

result = float(subtotal) + float(sales_tax)

print('Total:', result)
