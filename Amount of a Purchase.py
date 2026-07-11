#Author Myrtle 
#Date 07/10/2026
'''
prompt purchase price and amount
sales tax 
county tax
total tax
sale total
'''
price = float(input('Enter purchase price: '))
state = price * 5 / 100
county = price * 2.5 / 100
total = state + county
saleT = price + total
print('Purchase Amount: ', round(price, 2))
print('State Tax: ', round(state, 2))
print('County Tax: ', round(county, 2))
print('Total Tax: ', round(total, 2))
print('Sale Total: ', round(saleT, 2))




