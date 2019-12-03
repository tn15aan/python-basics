# Continuation for loops

dict_data = {
    1: {
        'name': 'Bronson',
        'money': 0.50
    },
    2: {
        'name': 'Janet',
        'money': 3.50
    },
    3: {
        'name': 'Bartolumeu',
        'money': 1.50
    },
    4: {
        'name': 'Vanessa',
        'money': 0.23
    }
}

# When you do a simple for loop on a dictionary
# You get the individual keys
# for key in dict_data:
#     print(key, '--->', dict_data[key]) # print the key name and print the values in key

# We want the name and how much they owe us
# After we apply the interest (4000%)

for key in dict_data:
    print(dict_data[key]['name'], 'owes us:', dict_data[key]['money']*4000/12+dict_data[key]['money'])

for values in dict_data.value():
    print(values)

print('Hello'[0])