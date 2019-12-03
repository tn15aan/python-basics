# If functions
# Control flow
# While loops also part of control flow

# Syntax
# if <condition>:
    # block of code
# elif <condition>:
    # block of code
# else:
    # block of code

age = int(input('How old are you?'))
if age < 21 and age > 18:
    print('You can vote but you cannot drink')
elif age > 18 and age < 65:
    print('You can vote')
elif age > 16:
    print('You can drive in the US')
else:
    print('You are too young')

# Most specific has to be on top
# conditions are built with operators and logical operators
# Once something is True, the block runs and the program exits the function