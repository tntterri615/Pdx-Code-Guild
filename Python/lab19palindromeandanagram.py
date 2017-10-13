# write a fn to check if words are anagrams

def anagram(word1, word2):
    word1 = (word1).lower()
    word2 = (word2).lower()
    word1 = (word1).replace(' ', '')
    word2 = (word2).replace(' ', '')
    print(word1, word2)
        # turn words into lists
    word1 = sorted(list(word1))
    word2 = sorted(list(word2))

    return (word1 == word2)

print(anagram('anagram', 'nag a ram'))


# write a fn to check if a word is a palindrome

# def check_palindrome(word):
#     for i in range(len(word)//2):
#         # j = len(word) - i - 1
#         # print(word[i])
#         # print(word[j])
#         if (word[i]) != (word[-i - 1]):
#             return False
#
#     return True
#
#
# print(check_palindrome("raceoar"))


