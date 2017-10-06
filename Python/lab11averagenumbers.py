'''
average numbers
'''

'''
nums = [5, 0, 8, 3, 4, 1, 6]
n = 0

# get a running total from the list, nums
for i in nums:
    n += i

print(n)

# get average of list
print(n / (len(nums)))
'''

nums = []
x = input('Enter a number or reply "done":')

while x != 'done':
    nums.append(int(x))
    x = input('Enter a number or reply "done":')

n = 0
# figure out how to calculate and display the average
for i in nums:
    n += i


print(n / (len(nums)))
