# build a program to manage a list of contacts
'''
[
0:   {'name': 'Cameron', 'favorite color': 'blue', 'favorite fruit': 'blackberry'},
1:   {'name': 'Cameon', 'favorite color': 'blue', 'favorite fruit': 'blackberry'},
2:   {'name': 'Camen', 'favorite color': 'blue', 'favorite fruit': 'blackberry'},
3:   {'name': 'Caeron', 'favorite color': 'blue', 'favorite fruit': 'blackberry'},
4:   {'name': 'Ceron', 'favorite color': 'blue', 'favorite fruit': 'blackberry'},
]

[0, 1, 2, 3, 4]

list[3].values()
{'name': 'Caeron', 'favorite color': 'blue', 'favorite fruit': 'blackberry'}.values()
['Caeron', 'blue', 'blackberry']
'''
# version 1
with open('contacts.csv', 'r') as file:
    contents = file.read().split('\n') # this creates a list
    #print(lines)
    key = contents.pop(0)   # remove first index to create key
    # print(key)
    key = key.split(',')
    # print(key)
    # print(contents)          # shows key was removed from list
    contacts = []

    for line in contents:
        line = line.split(',')
        contact = {}
        for i in range(len(line)):
            contact[key[i]] = line[i]
        contacts.append(contact)
    print(contacts)


# define functions for version 2
def print_contact(contact):
    print("")
    for key, value in contact.items():
        print(f"{key}: {value}")
    print("")

'''Finds a contact in the list and returns its index'''
def contact_index(contacts, search_text):
    for i in range(len(contacts)):
        if search_text.lower() == contacts[i]['name'].lower():
            return i

# Version 3, reverse of version 1
def save(contacts):
    lines = []
    keys = list(contacts[0].keys())
    lines.append(",".join(keys))

    for contact in contacts:
        values = list(contact.values())
        lines.append(",".join(values))

    with open('contacts.csv', 'w') as file:
        file.write("\n".join(lines))

# version 2

while True:
    command = input('What would you like to do to the dictionary? ')
    if command in ['done', 'exit', 'quit']:
        save_or_not = input('Do you want to save? y/n: ')
        if save_or_not == 'y':
            save(contacts)
        break
    elif command == 'create':
        contact = {}
        contact[key[0]] = input('Enter the name: ')
        contact[key[1]] = input('Enter their favorite fruit: ')
        contact[key[2]] = input('Enter their favorite color: ')
        print_contact(contact)
        contacts.append(contact)
    elif command == 'retrieve':
        retrieve_name = input('Enter contact name: ')
        index = contact_index(contacts, retrieve_name)
        if index:
            print_contact(contacts[index])
        else:
            print('Name not in contacts. ')

    elif command == 'update':
        update_name = input('Enter contact name: ')
        index = contact_index(contacts, update_name)
        update_info = input ('Choose fruit or color to update: ')
        update_var = input('What is the updated favorite? ')

        if update_info == 'fruit':
            contacts[index].update({'favorite fruit': update_var})
        else:
            contacts[index].update({'favorite color': update_var})

    elif command == 'delete':
        delete_name = input('Enter contact name to be deleted: ')
        index = contact_index(contacts, delete_name)
        contacts.pop(index)

    elif command == 'list':
        for contact in contacts:
            print(contact)

    else:
        print('Command not recognized')

