# unicode count words

punctuation = ";,.?!'\"-()*:[]$#"
other_punctuation = '":;#*()[]\'/$#,-\n'
word_count = {}

# Version 1
# with open('leviathan.txt', 'r') as f:
#     contents = f.read()
#     contents = contents.lower()
#     for char in punctuation:
#         contents = contents.replace(char, "")
#     contents = contents.split()
#
# for word in contents: # for key in dict
#     if word not in word_count:
#         word_count[word] = 1
#     else:
#         word_count[word] += 1
#
# print(word_count)
#
# words = list(word_count.items()) # list of tuples
# words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
# for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
#     print(words[i])


# Version 2
with open('leviathan.txt', 'r') as f:
    contents = f.read()
    contents = contents.replace('?', '.')  # split into sentences by changing all punctuation to '.'
    contents = contents.replace('!', '.')
    contents = contents.lower()
    for punctuation in other_punctuation:
        contents = contents.replace(punctuation, '')
    sentences = contents.split('.')
    words = contents.split(' ')
    print(len(words))
    print(len(sentences))
    # for word in words:
    #     print(word)
    #print(sentences)
    for i in range(len(words)-1):  # for key in dict
        if words[i].strip() == '' or words[i+1].strip() == '':
            continue
        pair = words[i] + ' ' + words[i + 1]
        if pair not in word_count:
            word_count[pair] = 1
        else:
            word_count[pair] += 1
    words = list(word_count.items()) # list of tuples
    words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
    for i in range(min(20, len(words))):  # print the top 20 words, or all of them, whichever is smaller
        print(words[i])

# Version 3
# Nick walked me through the concept of how this would work; create a dictionary inside a dictionary
# pair_counts = {
#     'to': {
#         'from': 3,
#         'there': 5,
#     },
#     'there': {
#         'and': 4,
#         'word': 5
#     }
# }
#
# word1 = 'to'
# word2 = 'from'
#
# if word1 not in pair_counts:
#     pair_counts[word1] = {}
#
# if word2 not in pair_counts[word1]:
#     pair_counts[word1][word2] = 1
# else:
#     pair_counts[word1][word2] += 1
