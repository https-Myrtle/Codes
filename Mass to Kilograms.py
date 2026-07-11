#Author Myrtle
#Date 07/09/2026
'''
prompt obj mass in kg
mass * 9.8
if more than 500 n
    display too heavy
elif
    display too light
'''

mass = float(input('Enter the objects mass in kilograms: '))
weight = mass * 9.8
if weight > 500:
    print('Object Weight: ', round(weight, 2))
    print('The object is to heavy. It weighs more than 500.0 Newtons.')

elif weight < 100:
    print('Object Weight: ', round(weight, 2))
    print('The object is to light. It weighs less than 100.0 Newtons.')

else:
    print('Object Weight: ', round(weight, 2))
