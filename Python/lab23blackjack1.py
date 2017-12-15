# give basic blackjack advice


def card_value(card):
    if card == 'jack' or card == 'queen' or card == 'king':
        return 10
    elif card == 'ace':
            return 1
    else:
        return int(card)


first_card = input('What is your first card? ')
second_card = input('What is your second card? ')
third_card = input('What is your third card? ')


first_value = card_value(first_card)
second_value = card_value(second_card)
third_value = card_value(third_card)

card_total = first_value + second_value + third_value

print(card_total)

if card_total < 17:
    print('Hit')
elif card_total >= 17:
    print('Stay')
elif card_total > 21:
    print('Already busted')



