# Write a program that decrypts a message encoded with ROT13 on each charachter starting with 'a', and displays it to the user in the terminal.


alphabet = 'abcdefghijklmnopqrstuvwxyz !.?'
# rot13 =  'nopqrstuvwxyzabcdefghijklm !.?'

text = 'hello'

encrypted = '' # string builder pattern
rotation = int(input("Rotation amount: "))
for char in text:
    # find the index of char in alphabet using 'find'
    index = alphabet.find(char)  # find index for character
    index += rotation

    if index > 25:
        index -= 26

    encrypted += alphabet[index]
print(encrypted)


