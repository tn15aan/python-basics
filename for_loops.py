# For loops
# For loops will iterate over an iterable and run a block of code

# Syntax
# for <placeholder> in <iteratable>:
        #doing stuff in the block
        #more things in a block
# }

# Note: the block of code exists after the : (colon)
# It is the lines of code that ARE INDENTED
# and it STOPs when the indentation stops

# Iterables are list, ranges and dictionaries... and also strings(why?)
import time
import random
wish_list = ('rc car', 'molten cheese', 'cheerleaders', 'White shirts',
             'sugar laces', 'reeces', 'pastel de nata')
# count = 1
# for item in wish_list:
#     print(count, '-', item)
#     print('Doing some thinking.. ')
#     time.sleep(1.2)
#     count += 1
#     print(random.randint(200, 207)) # using random library

# list_data = [[2, 4, 6, 8],[10, 12, 14, 16]]
list_data = [['rc car', 'cheerleaders', 'white shirts', 'audi r8'],
             ['sugar laces', 'cheese', 'pastel de nata', 'baklava']]

counter = 1
for data in list_data:
    print(data)
    for num in data:
        print(counter, '-', num)
        counter += 1



