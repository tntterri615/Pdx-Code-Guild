'''
making change out of a dollar amount
'''

# get input(dollar amount) from user
x = int(input("Let's convert your money from dollars into change. How much money do you have, without using the decimal point?"))

# determine how many quarters can be used
quarters = float(x//25)

# get remainder
q_remainder = x%25

# determine how many dimes can be used
dimes = float(q_remainder//10)
d_remainder = q_remainder%10

# determine how many nickles can be used
nickles = float(d_remainder//5)
n_remainder = d_remainder%5

#determine how many pennies can be used
pennies = n_remainder



print(f'{quarters} quarters, {dimes} dimes, {nickles} nickles, {pennies} pennies')


y = float(input("Now enter a dollar amount with the decimal point:"))

amount_in_pennies = y * 100

print(f'You have {amount_in_pennies} pennies.')