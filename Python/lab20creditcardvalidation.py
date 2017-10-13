# write fn to determine if cc# is valid (as a boolean)

def check_credit_card(card):
    check_digit = card.pop()
    # print(check_digit)
    # print(card) # list w/o check digit
    card.reverse()
    # print(card)
    # double every other element AND sub 9 fr/nums > 9
    for i in range(0, len(card), 2):
        card[i] *= 2
        if card[i] > 9:
            card[i] -= 9
    return sum(card) % 10 == check_digit


card = list(input('enter your cc: '))
# convert the string into a list
for i in range(len(card)):
    card[i] = int(card[i])
print(check_credit_card(card))


