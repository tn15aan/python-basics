# Magic number game
# prompt the user for input
# generate a random number using a python library (should be between 1-10)
# check the the number against a magic number
# let the user know if he/she won or
    # if the guess was above or under

import random
random_num = random.randint(1, 10)
num = int

while random_num != num:
    num = input("Please input a number between 1 and 10: ")
    if num == random_num:
        print('OMG you won congratulations')
    elif num > random_num:
        print('Your number', num, 'is higher')
    else:
        print('Your number is lower')

