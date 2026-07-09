import random
random.seed(101) #do not remove

value = 0

while True:
    number = random.randint(0, 10)
    value += 1
    print('Number', value,'was', number)
    
    if number == 7:
        print('Lucky 7!')
    if number == 0:
        break

