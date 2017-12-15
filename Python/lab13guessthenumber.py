'''
have the user guess a random number (1-10) chosen by the computer
'''
from random import randint

comp_choice = randint(1, 10)

#create a REPL to check the user input against the computer choice
i = 0
user_choice = 0
while i < 10 and user_choice != comp_choice:
    user_choice = int(input('Guess what number from 1-10 the computer is thinking of: '))
    if comp_choice == user_choice:
        print('You won!')
    else:
        print('Wrong! Try again!')
    i += 1

if i >= 10:
    print('You lose!')
