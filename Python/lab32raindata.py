'''
rain data
'''

import datetime
import math
import matplotlib.pyplot as plt

with open('collins_view.rain.txt', 'r') as f:
    contents = f.read().split("\n")
    rain_data = []
    for i in range(11, len(contents) - 1):
        temp = contents[i].split()
        temp[0] = datetime.datetime.strptime(temp[0], '%d-%b-%Y')
        for j in range(1, len(temp)):
            if temp[j] != '-':
                temp[j] = int(temp[j])
        if len(temp) > 0:
            rain_data.append(temp)

    most_rain_day = rain_data[0]                              # get rainiest day
    for i in range(len(rain_data)):
        if rain_data[i][1] == '-':
            continue
        if most_rain_day[1] < rain_data[i][1]:
            most_rain_day = rain_data[i]
    print(f'Rain accumulation on rainiest day: {most_rain_day}')

    # get average
    total = 0
    broken_rain_gauge = 0                                   # this is data with dashes
    count = 0
    rain_data_day = rain_data[0][1]
    for i in range(len(rain_data) - 1):
        if rain_data[i][1] == '-':
            broken_rain_gauge += 1
            continue
        count += 1
        total += rain_data[i][1]
    # print(broken_rain_gauge)
    # mean = total / (len(rain_data) - broken_rain_gauge)
    mean = total / count
    print(f'Mean: {mean}')

    total = 0                                                 # get variance
    for i in range(len(rain_data) - 1):
        if rain_data[i][1] == '-':
            continue
        diff = rain_data[i][1] - mean
        total += diff * diff
        variance = total / ((len(rain_data) - 1)-broken_rain_gauge)

    print(f'Variance: {variance}')
    print(f'Std deviation: {math.sqrt(variance)}')

    # rainiest year

    list_of_years = []                               # create a list of all years in data
    yearly_rain_total = []
    counts = []
    for data_row in rain_data:
        year = data_row[0].year
        if year not in list_of_years:
            list_of_years.append(year)
            yearly_rain_total.append(0)
            counts.append(0)
    list_of_years.sort()
    # print(list_of_years)

    for i in range(len(rain_data)):                           # add rain data to corresponding year
        if rain_data[i][1] == '-':
            continue
        year = rain_data[i][0].year
        j = list_of_years.index(year)
        yearly_rain_total[j] += rain_data[i][1]
        counts[j] += 1

    print(f'Years with rain data: {list_of_years}')
    # print(yearly_rain_total)
    # print(counts)

    avg = []
    for i in range(len(list_of_years)):
        if counts[i] == 0:
            avg.append(0)
        else:
            avg.append(yearly_rain_total[i] / counts[i])

    print(f'The rainiest year was {list_of_years[avg.index(max(avg))]}')

    x_values = list_of_years
    y_values = avg

    # x_values = []
    # y_values = []
    # for i in range(len(rain_data)):                 # loops over indices
    #     if rain_data[i][0].year == 2012:            # lots of data, only printing one year to be able to read graph
    #         x_values.append(rain_data[i][0])
    #         y_values.append(rain_data[i][1])

    # for data_row in rain_data:                    # loops over elements
    #     if data_row[0].year == 2012:
    #         x_values.append(data_row[0])
    #         y_values.append(data_row[1])

    plt.plot(x_values, y_values)
    plt.show()
