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

## Useful method(dependant on a specific data type) for strings
