#Author Myrtle Abigail
#Date 07/06/2026

'''
input the number of sq ft in the tract

result = ft / 43560

display the size of the tract  #rounded by 2
'''

ft = input('Enter the number of square feet in the tract: ')
result = float(ft) / float(43560)
print('The size of that tract is ', round(result, 2), ' acres.')
