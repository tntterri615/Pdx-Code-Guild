'''
get user input to do simple calculations
'''

# ask user for input they want to calculate
while True:
    operation = input('What is the operation you\'d like to perform?')

    if operation == 'done':
        print('Goodbye')
        break

    num1 = input('What is the first number?')
    num2 = input('What is the second number?')

    if operation == '+' or operation == '-' or operation == '*' or operation == '/':
        if operation == '+':
            print((float(num1) + float(num2)))
        elif operation == '-':
            print((float(num1) - float(num2)))
        elif operation == '/':
            print((float(num1) / float(num2)))
        elif operation == '*':
            print((float(num1) * float(num2)))
