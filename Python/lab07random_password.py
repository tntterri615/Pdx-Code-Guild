''' random password generator
'''

import string
import random

n = int(input('How long do you want the password to be: '))

i = 0
output = ""

while i < n:
    output += random.choice(string.ascii_lowercase)
    i += 1

print(output)