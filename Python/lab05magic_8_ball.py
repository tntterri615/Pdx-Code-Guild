# ask magic 8 ball questions until you are 'done'

import random


results = ['As I see it, yes', 'Reply hazy try again', 'Most likely', 'Outlook good', 'Ask again later', 'Very doubtful']


while True:
    question = input('What is your question?')
    result = random.choice(results)

    if question == 'done':
        break

    print(result)
