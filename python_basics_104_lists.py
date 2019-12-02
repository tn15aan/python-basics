# List in Python
# Ordered by index
## AKA arrays or (confusingly) as objects in JavaScript

# Syntax
# Declare lists using []
    # Seperate objects using ,

# var_list_name = [ 0 , 1 , 2 , 3] - the index values

crazy_x_landlords = ['Sr. Julio', 'Jane', 'Alfred', 'Marksons']
print(crazy_x_landlords)
print(type(crazy_x_landlords))

# How to access record number 3 in the list
print(crazy_x_landlords[2])

# Accessing other locations
print(crazy_x_landlords[0])
print(crazy_x_landlords[-1])

# New list of places to live
places_to_live = ['California', 'Rio de Janeiro', 'Melbourne', 'Manchester', 'Singapore']
print(places_to_live[3])

# Reassigning an index
places_to_live[3] = 'Hawaii'
print(places_to_live[3])

# Method .append(object)
print(len(places_to_live))
places_to_live.append('LA')
print(len(places_to_live))

# .insert(index, object)
places_to_live.insert(0, 'Lisboa')
print(places_to_live)

# .pop(index)
# Removes from list at specific index
places_to_live.pop(3)
print(places_to_live)

# List slicing
    # Used to manage lists

# Prints from stated index to end of list
print(places_to_live[3:])
# Prints from index to the start of the list (not inclusive of the index)
print(places_to_live[:3])

# Prints from specific index to second specified index (not inclusive)
print(places_to_live[1:3])

# Skip slicing
list_exp = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
print(list_exp)
print(list_exp[0:12:2]) # Starting index, finishing index, how many to increment
print(list_exp[::-1]) # Decrement

# Tuples
# Immutable lists
# Syntax
    # Defined using (object, object)

mortal_enemies = ('Mario', 'Sailormoon', 'MOON CAKE', 'Jerry', 'Berry')
print(type(mortal_enemies))

# If you try to reassign it will break (will not work) e.g.
# mortal_enemies[0] = 'Goku'
print(mortal_enemies)

# Example of creating amazing list for end of the world survival
list_of_kit = []
item_1 = input('What is your first item to keep?')
list_of_kit.append(item_1)
item_2 = input('What is your second item to keep?')
list_of_kit.append(item_2)
item_3 = input('What is your third item to keep?')
list_of_kit.append(item_3)

print('Hey there partner you have a nice list!')
print(list_of_kit)