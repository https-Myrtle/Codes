#Autor Myrtle Argote
#Date 07/08/2026
'''
length x Width
INPUT L1, W1, L2, W2
result_1 = L1 * W1
result_2 = L2 * W2
IF result_1 > result_2 THEN
    DISPLAY result_1, result_2
    DISPLAY "Area A is greater than Area B."
ELSE IF result_1 < result_2 THEN
    DISPLAY result_1, result_2
    DISPLAY "Area B is greater than Area A."
ELSE
    DISPLAY result_1, result_2
    DISPLAY "Area A is equal to Area B."
'''
value_1 = input('L1: ')
value_2 = input('W1: ')
value_3 = input('L2: ')
value_4 = input('W2: ')

result_1 = float(value_1) * float(value_2) #L1 x W1
result_2 = float(value_3) * float(value_4) #L2 x W2

if result_1 > result_2:
    print('Area A: ', round(result_1, 2))
    print('Area B: ', round(result_2, 2))
    print('Area A is greater than Area B.')

elif result_1 < result_2:
    print('Area A: ', round(result_1, 2))
    print('Area B: ', round(result_2, 2))
    print('Area B is greater than Area A.')

else:
    print('Area A: ', round(result_1, 2))
    print('Area B: ', round(result_2, 2))
    print('Area A is equal to Area B.')
