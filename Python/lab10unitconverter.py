'''
convert feet to meters
'''


x = int(input('What distance do you want to convert?'))
y = input('What are the input units?')
z = input('What are the output units?')


if y == 'ft':
    output = x * 0.3048
elif y == 'km':
    output = x * 1000
elif y == 'mi':
    output = x * 1609.34
elif y == 'yd':
    output = x * 0.9144
elif y == 'in':
    output = x * 0.0254


if z == 'ft':
    output /= 0.3048
elif z == 'km':
    output /= 1000
elif z == 'mi':
    output /= 1609.34
elif z == 'yd':
    output /= 0.9144
elif z == 'in':
    output /= 0.0254


print(f'{x} {y} is {output} {z}')
