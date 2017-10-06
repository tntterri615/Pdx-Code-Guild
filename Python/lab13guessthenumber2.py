'''
have the user guess a random number (1-10) chosen by the computer
'''

from random import randint


comp_choice = randint(1, 10)


#create a REPL to check the user input against the computer choice
i = 0
while True:
    i += 1
    user_choice = input('Let\'s play a game. Guess what number from 1-10 the computer is thinking of: ')
    user_choice = int(user_choice)
    if comp_choice == user_choice:
        print('You won!')
        break
    else:
        if user_choice > comp_choice:
            print('Wrong! Too high, try again.')
        else:
            print('Wrong! Too low, try again.')



print('Guesses: '+str(i))