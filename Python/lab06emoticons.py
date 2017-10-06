import random

eyes = [';', ':']
noses = ['^', '-']
mouths = [')', '(', '/']




for i in range(7):

    eye = random.choice(eyes)
    nose = random.choice(noses)
    mouth = random.choice(mouths)
    print(eye + nose + mouth)



