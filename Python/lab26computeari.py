# compute ari from text file

import math
punctuation = ";,.?!'\"-()*:[]$#"
other_punctuation = '":;#*()[]\'/$#,-\n'
word_count = {}
ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

with open('leviathan.txt', 'r') as f:
    contents = f.read()
    contents = contents.replace('?', '.')  # split into sentences by changing all punctuation to '.'
    contents = contents.replace('!', '.')
    contents = contents.lower()
    for punctuation in other_punctuation:
        contents = contents.replace(punctuation, '')     # remove punctuation and split into sentences
    sentences = contents.split('.')
    # print(sentences)
    words = contents.split(' ')           # split into words
    # print(words)
    # print(len(words))
    # print(len(sentences))

    letters = ''.join(words)
    # print(len(letters))

    ari = 4.71*((len(letters))/(len(words))) + 0.5*((len(words))/(len(sentences))) - 21.43
    if ari > 14:
        ari = 14
    # print(ari)

    print(f'''
    -----------------------------------------------------------------------------
    The ARI for leviathan.txt is {ari},
    This corresponds to a {ari_scale[ari]["grade_level"]} level of difficulty,
    That is suitable for the average person {ari_scale[ari]["ages"]} years old
    -----------------------------------------------------------------------------''')


