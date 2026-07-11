#Author Myrtle
#Date 07/03/2026
'''
input cars speed is
input the time
distance = speed * time
Display car travelled then round it ny 2
'''
speed = input('Enter the cars speed: ')
time = input('Enter the time: ')
distance = float(speed) * float(time)
print('The car travelled ', round(distance, 2))
