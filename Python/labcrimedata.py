'''
crime data
'''

with open('crime_incident_data_2011.csv.txt', 'r') as file:
    contents = file.read().split('\n') # this creates a list
    key = contents.pop(0)   # remove first index to create key
    key = key.split(',')
    print(key)
    print(contents[0])          # shows key was removed from list
    crimes = []

    for line in contents:
        line = line.split('","')
        print(line)
        temp = ''
        line.pop()
        print(line)
    #     crime = {}
    #     for i in range(len(line)):
    #         crime[key[i]] = line[i]
    #     crimes.append(crime)
    # print(crimes)

