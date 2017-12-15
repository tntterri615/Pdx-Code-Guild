# mismatched socks

import random
sock_count = {}
sock_types = ['ankle', 'crew', 'calf', 'thigh']
sock_colors = ['black', 'white', 'blue']

i = 0
sock_pile = []
while i < 100:                                       # generate 100 random socks
    sock = random.choice(sock_types)
    color = random.choice(sock_colors)
    sock_pile.append((sock, color))
    i += 1
# print(f'types: {sock_pile}')

for sock in sock_pile:                         # count number of socks per type
    if sock not in sock_count:
        sock_count[sock] = 1
    else:
        sock_count[sock] += 1

print(f'sock count: {sock_count}')

pairs = {}
singles = {}
for sock in sock_count:                                # do math to get number of pairs
    pairs[sock] = sock_count[sock]//2
    singles[sock] = sock_count[sock]%2

print(f'pairs: {pairs}')
print(f'singles: {singles}')



