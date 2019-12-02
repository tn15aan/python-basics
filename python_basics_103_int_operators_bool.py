# Numerical types
# Numerical types are: integers, floats, composites
    # big int and complex number

# Declaring an int
num1 = 20
print(type(num1))

num2 = 20.0
print(type(num2))

# Operators # +, -, *, %, / Numerical operators take priority over logical however use brackets?
result1 = 10 + 12 # Adding
result2 = 10 - 2 # Subtracting
result3 = 10 * 30 # Multiplying
result4 = 20 % 3 # Checking the remainder
result5 = 20 / 2 # Dividing
print(result1, result2, result3, result4, result5)

# Logical operators
# one = is assignment
num_a = 10
num_b = 10
num_c = 13

# Bigger than --> returns a boolean (bool)
print(num_b > num_c)
print(num_c > num_a)
# Smaller than
print(num_b < num_c)

#Bigger/smaller than or equals
print(num_a >= num_b)
print(num_b <= num_c)
print((num_a + num_c) > num_b)

# Check if the same data type matters
print('10' == 10)
print(num_b == num_a)
print(num_a == num_c)

# Boolean - true or false
print(type(True))
print(type(False))
bool_true = True
bool_false = False

print(bool_true == bool_false)
print(bool_true != bool_false) #not equals to

# Logical <and>
# Syntax
# (<condition> and <condition>) --> bool
    # Requires the two sides to be true to return true
print(True and True) # The two sides and True
print(True and False) # only one side is True --> becomes False

# Logical <or>
# Syntax
# (<condition> and <condition>) --> bool
    # Requires only one side to be true to result in true
print(True or True) # The two sides and True
print(True or False) # One side is True --> results in True