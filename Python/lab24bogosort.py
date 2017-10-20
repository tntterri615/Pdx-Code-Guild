# bogo sort

import random

def random_list(n):
    list = []
    for i in range(n):
        # create a list of random numbers
        list.append(random.randint(0, 100))
    return list

def shuffle(nums):
    shuffled_list = []
    for i in range(len(nums)):
        # create a random index and shuffle
        index = random.randint(0, len(nums) - 1)
        j = nums.pop(index)
        shuffled_list.append(j)
    return shuffled_list

num_list = random_list(200)

# now, shuffle numbers
print(num_list)
# print(shuffle(num_list))

# now, are the numbers in the list sorted?

def is_sorted(nums):
    for i in range(len(nums)):
        # check if the first index is greater than the second index and loop through to compare all indices
        if num_list.index(i) > num_list.index(i + 1):
            return False
    return True

num_list = random_list(200)
print(is_sorted(num_list))
