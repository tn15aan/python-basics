# Dictionary
# AKA --> hash or (confusingly) object in JS
# Works like a dictionary - has key and value pairs
    # The key is the word you look up
    # The value is the meaning / value of the word

# Syntax
# {}
# dict = {'key': 'value'}

# Defining a dictionary
my_dictionary = {'tissues': 'a disposable piece of absorbent paper, used especially as a handkerchief or for cleaning the skin.',
                 'baseball_bat': 'It is a bat of wood made to play baseball.'}

# Accessing or re-assigning is with the key inside the []
print(my_dictionary['baseball_bat'])
my_dictionary['baseball_bat'] = 'Really, you are looking up two seperate words'
print(my_dictionary['baseball_bat'])