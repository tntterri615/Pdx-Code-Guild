

# def count_letter(char_to_find, word):
#     count = 0
#     for c in word:
#         print(c)
#         if c == char_to_find:
#             count += 1
#             print('\t'+str(count))
#         # if c is equal to char_to_find, increment count
#     return count
#
#
# print(count_letter('a', 'antidisestablishmentterianism'))
# printcount_letter('p', 'Pneumonoultramicroscopicsilicovolcanoconiosis')


'''
# Convert input strings to lowercase without any surrounding whitespace.

def lowercasenospace(word):
    word2 = word.lower()
    word3 = word2.strip()
    return word3

word = lowercasenospace("SUPER!")
print(word)
'''

# Write a function that tells whether a number is even or odd (hint, compare a/2 and a//2, or use a%2)

# def is_even(a):
#     z = a/2
#     if z == int:
#         print('True')
#     else:
#         print('False')
#
# a = is_even(3)


# Write a function using random.randint and subscription to get a random element of a list and return it.


# print(random_element(['apples', 'bananas', 'pears']))
# print(random_element(['a', 'b', 'c']))


# write a fn that returns the maximum of three parameters

# def maximum_of_three(a, b, c):
#     max = a
#     if b > max and b > c:
#         max = b
#     elif c > max:
#         max = c
#     return max

# print (maximum_of_three(5,7,11))


# print out the powers of 2 from 2^0 to 2^20

# def range_of_powers(number, high_power):
#     for i in range(high_power):
#         x = number**i
#         print(x)
#
# range_of_powers(3, 4)


# Write functions to find the minimum, maximum, mean, and (optionally) mode of a list of numbers.

# def minimum(nums):
#     min = nums[0]
#     for num in nums:
#         if num < min:
#             min = num
#     return(min)
#
# print(minimum([7, 4, 1, 8, 9]))
#
#
# def maximum(nums):
#     max = nums[0]
#     for num in nums:
#         if num > max:
#             max = num
#     return(max)
#
# print(maximum([2,9,3,6,14]))


# def mean(nums):
#     n = 0
#     for i in nums:
#         n += i
#     print(n / (len(nums)))
#
#
# print(mean([5, 0, 8, 3, 4, 1, 6]))

# reverse list

# def reverse_list(my_list):
#     for i in my_list:
#         return(my_list[::-1])

#
#
# #  print(my_list)
#
# print(reverse_list(['cookie', 'cake', 'candy']))


# Write a function to find all common elements between two lists.


# def common_elements(nums1, nums2):
#     output = []
#     for num in nums1:
#         if num in nums2:
#             output.append(num)
#     print(output)
#
#
# nums1 = [1,4,6,7,5]
# nums2 = [4,3,5,6,1]
#
# common_elements(nums1, nums2)


# move elements of list with values less than 10 to new list

# def extract_less_than_ten(nums):
#     output = []
#     for num in nums:
#         if num < 10:
#             output.append(num)
#     print(output)
#
# extract_less_than_ten([2,12,45,3,7,4])

# Write a function to combine two lists of equal length into one, alternating elements.

def combine(nums1, nums2):
    nums3 = []
    for i in range(len(nums1)):
        # append the element of nums1 at i to nums3
        nums3.append(nums1[i])
    # append the element of nums2 at i to nums3
        nums3.append(nums2[i])
    return nums3

x = combine(['a','b','c'],[1,2,3])
print(x)






