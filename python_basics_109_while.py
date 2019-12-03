# While loops

# Syntax
# while <condition>:
    # block of code
    # block of code
    #Condition
        # Break

# num = 0
# while num < 10:
#     print('still less than 10')
#     num += 1

wish_list = ('rc car', 'molten cheese', 'cheerleaders', 'White shirts',
             'sugar laces', 'reeces', 'pastel de nata')

# # Using to substitute the for loop
# print(len(wish_list))
# index_length = len(wish_list)-1
# counter = 0 #index is at 0 that's why we -1 beforehand
# while counter <= index_length:
#     print(wish_list[counter])
#     counter += 1

# Generate a random number
while True:
    # Generate a random number
    num = 14
    # Ask for user input
    user_guess = int(input('What number do you think I am thinking of?'))
    # Evaluate input and respond appropriately
    if num == user_guess:
        print('Holy cow! You guessed it')
    elif user_guess > num:
        print('lower... bit lower')
    elif user_guess == 0:
        break
    elif user_guess < num:
        print('higher... bit higher')






