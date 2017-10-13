# pick 6, play lottery

import random

user_expenses = 0
user_winnings = 0

print('Let\'s play the lottery')



winning_nums = []
for i in range(6):
    winning_nums.append(random.randint(1, 99))

for w in range(1000):
    ticket = []
    for i in range(6):
        ticket.append(random.randint(1, 99))



    user_expenses += 2

    common_nums = 0
    for num in ticket:
        if num in winning_nums:
            common_nums += 1

    if common_nums == 1:
        print('You win $4')
        user_winnings += 4
    elif common_nums == 2:
        print('You win $7')
        user_winnings += 7
    elif common_nums == 3:
        print('You win $100')
        user_winnings += 100
    elif common_nums == 4:
        print('You win $50,000')
        user_winnings += 50000
    elif common_nums == 5:
        print('You win $1,000,000')
        user_winnings += 1000000
    elif common_nums == 6:
        print('You win $25,000,000')
        common_nums += 25000000
    else:
        print('No matches')


print(winning_nums)
print(user_winnings - user_expenses)
ROI = ((user_winnings - user_expenses)/user_expenses)
print(ROI)
