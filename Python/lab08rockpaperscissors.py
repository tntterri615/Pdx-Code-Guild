'''
rock paper scissors
'''

import random

user_choice = input("Let's play rock, paper, scissors. What do you choose?")

# define a list for computer to randomly choose from
computer_choices = ['rock', 'paper', 'scissors']
computer_choice = random.choice(computer_choices)

print('Computer chose ' + computer_choice)

# create a loop to compare user choice to computer choice to determine a winner
if user_choice == 'rock':
    if computer_choice == 'rock':
        print('Tie')
    elif computer_choice =='paper':
        print('You win')
    else:
        print('Computer wins')

elif user_choice == 'paper':
    if computer_choice == 'rock':
        print('You win')
    elif computer_choice == 'paper':
        print('Tie')
    else:
        print('Computer wins')
else:
    if computer_choice == 'rock':
        print('Computer wins')
    elif computer_choice == 'paper':
        print('You win')
    else:
        print('Tie')

