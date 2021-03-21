import random
number = random.randint(1,99)
guess = int(input('write your number:'))
while number != guess :
    if number > guess:
        print ('guess higher')
    else:
        print ('guess lower')
    guess = int(input('write your number:'))
print('you won!')
