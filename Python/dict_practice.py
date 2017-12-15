




inventory = {'apples': 4, 'pears':10, 'pineapple': 3}
for key in inventory:
    print(key + ' ' + str(inventory[key]))


inventory['apples'] += 1

print(inventory)


inventory['banana'] = 1
print(inventory)


for item in inventory:
    print(item, end=' ')
    print(inventory[item])


