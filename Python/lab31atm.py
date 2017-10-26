'''
atm lab
'''


class Atm:
    transaction_list = []

    def __init__(self, balance = 0, interest_rate = 0.1):
        self.balance = balance
        self.interest_rate = interest_rate

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        self.transaction_list.append(f'You deposited ${amount}')
        return self.balance

    def check_withdrawl(self, amount):
        return (self.balance - amount) > 0

    def withdraw(self, amount):
        self.balance -= amount
        self.transaction_list.append(f'You withdrew ${amount}')
        return self.balance

    def calc_interest(self, interest):
        self.balance *= interest
        return self.balance

    def print_transactions(self):
        for i in self.transaction_list:
            print(i)

account = Atm(0, 0)
while True:
    command = input('What would you like to do (deposit, withdraw, check balance, history)? ').strip()

    if command == 'deposit':
        deposit_amount = input('Enter amount to deposit: ')
        account.deposit(int(deposit_amount))

    elif command == 'withdraw':
        withdraw_amount = input('Enter amount to withdraw: ')
        account.withdraw(int(withdraw_amount))

    elif command == 'check balance':
        print(account.check_balance())

    elif command == 'history':
        account.print_transactions()

