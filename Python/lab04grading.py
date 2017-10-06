'''
grading
'''

grade = int(input('Enter your grade.'))

if grade > 90:
    print('You got an A.')
elif grade > 80:
    print('You got a B.')
elif grade > 70:
    print('You got a C.')
elif grade > 60:
    print('You got a D.')
else:
    print('You got an F.')

if grade > 70:
    print('You passed.')
else:
    print('You failed.')

