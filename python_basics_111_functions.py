# Functions

# A function is like a machine.
# It needs to be turned on (called) and it does things


# Good practices
# They should be small and only do one job
        # Avoid stringy code
        # Testable code
        # Maintainable code
        # Readable

# Do not print inside a function - unless it explicity is supposed to print
# In function you return
# Call the function inside a print(function_name)
# DRY (Don't repeat yourself)
# Seperation of concerns
    # Define functions in one file
    # Call them in another
    # There is more to this

# Functions work this way:
    # 1) Define a function
    # 2) Call the function

# Syntax
# def <name>(arg, arg2, arg3):
    # Block
    # return something if you wish

def say_hello():
    return 'HElloooo'

def say_hello_user_bracket(f_name='filipe', l_name = 'paiva'):
    return 'hello ' + f_name.capitalize() + ' ' + l_name.capitalize()
print(say_hello_user_bracket('bob'))

def say_hello_user(f_name, l_name):
    return 'hello ' + f_name.capitalize() + ' ' + l_name.capitalize()

print(say_hello_user('thomas', 'nguyen'))
