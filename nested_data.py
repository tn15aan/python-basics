# Nested Data in lists and dictionaries

mix_list = ['strings', 98, ['more string', [1, 2, 'important']]]

print(type(mix_list[2]))

internal_list = mix_list[2]

print('Getting the word important')
print(mix_list[2][1][2]) #get a value in a list in a list
print('////')
print(internal_list) # print the internal list
print(internal_list[1][2]) #get the word important as the list is in index 1, and important is in 2
                            # in internal list

embedded_dict = {
    'status': 'operational',
    'key1': ['car keys', 'boat keys', 'mansion keys', 'dog house keys'],
    'staff': {
        'Julio Cesar': {
            'name': 'Julio',
            'last_name': 'Cesar',
            'birth_date': 1979,
            'football club': 'Flamengo'
        },
        'Julia Venus': {
            'name': 'Julia',
            'last_name': 'Venus',
            'birth_date': 1969,
            'football club': 'CubaFC'
        }
    }
}

#Print:
## The boat keys and dog house keys
## Inside the key 'staff', print the dictionary with the key 'Julio Cesar'
# From the dictionary with the key Julia Venus, print:
## the last name. the birthdate and the football club
key_list = embedded_dict['key1']
print(key_list[1])
print(key_list[3])

print(embedded_dict['staff']['Julia Venus']['last_name'])
print(embedded_dict['staff']['Julia Venus']['birth_date'])