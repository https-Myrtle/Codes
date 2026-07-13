#Author Myrtle
#Date 07/12/2026
'''
Primary color is red, blue, and yellow
input both primary color
display error if not primary color
if red and blue display purple
if red and yellow display orange
if blue and yellow display green
'''
pri_1 = input('Enter the first primary color in lower case: ')
pri_2 = input('Enter the second primary color in lower case: ')
color = ('red', 'blue', 'yellow')
if pri_1 not in color:
    print('Error: The first color you entered is invalid.')
if pri_2 not in color:
     print('Error: The second color you entered is invalid.') 
if pri_1 == 'red' and pri_2 == 'blue':
    print('purple')
if pri_1 == 'red' and pri_2 == 'yellow':
    print('orange')
if pri_1 == 'blue' and pri_2 == 'yellow':
    print('green')



