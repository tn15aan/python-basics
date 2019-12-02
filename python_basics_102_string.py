# Strings

## Define string - using '' and ""
my_string = "I'm an amazing string"
my_string2 = 'I am'
my_name = 'Thomas Nguyen'

print(my_string)
print(type(my_string))
print(my_string2)
print(type(my_string2))

# Concatenation - Joining of two string
print('This is an example of concatenation ' + my_string)
print('these are examples of strings', my_string2, my_string)

concatenate = my_string2 + ' ' + my_name
print(concatenate)

# Interpolation - Piece of code into a string
age = 21
name = "Julia"

# This is where we need to interpolate
print('Welcome <person>, you are <age_years> old')
print('Welcome <person>, you were born in the year <date_birth>')

# This is us actually interpolating values
print(f'Welcome {name}, you are {age} old')
print(f'Welcome {name}, you were born in the year {2019 - age}')

#print('Welcome {0}, you were born on the year {1}'.format.name, age)
## Useful method(dependant on a specific data type) for strings
example_string = "HELLoo   "
print(example_string)
print(example_string.strip()) # Remove trailing white spaces
print(example_string.count('L')) # Counts the number of characters on string
print(example_string.lower())
print(example_string.upper())
print(example_string.strip().capitalize()) # Chaining methods - Remove white trails and capitalize

# Learning and using .split()
text_to_split = 'this is some example text in our file'
results_split = text_to_split.split(' ') # space and comma
print(results_split)
results_split2 = text_to_split.split('i')
print(results_split2)

# Casting and int
str_string = '1990'
print(type(str_string))

# str to int casting
int_number = int(str_string)
print(type(int_number))

# int to str
new_str = str(int_number)
print(type(new_str))

# Standard built in function len()
print(len(example_string)) #Not dependent on the object which is a string (len is in front) whereas .lower is dependent requires the string to do something

