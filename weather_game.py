# Make a weather/clothing game
# IF statements
# Ask for user input and depending on the response advise on their attire.
#
# prompt user for input
# Evaluate each input and print the appropriate responses
# Follow these rules:
#
# when sunny >> respond with 'take your shorts!'
# stormy >> respond with 'take rain coat'
# rainy >> respond with 'Take your umbrella'
# rainy and stormy >> 'stay home'
# anything else respond with 'sorry, i didn't quite catch that'

attire1 = 'take your shorts!'
attire2 = 'take rain coat'
attire3 = 'Take your umbrella'
attire4 = 'stay home'


weather = input('How is the weather? Please choose between sunny, stormy, rainy')
if weather == 'sunny':
    print(attire1)
elif weather == 'stormy':
    print(attire2)
elif weather == 'rainy':
    print(attire3)
elif weather == 'rainy and stormy':
    print(attire4)
else:
    print("sorry, i didn't quite catch that")
