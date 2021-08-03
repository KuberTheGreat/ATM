class ATM:
    def __init__(self, accountNumber, pin):
        self.accountNumber = accountNumber
        self.pin = pin

        print('Your account number: ', accountNumber)
        print('Your account number: ', pin)

def withdraw(amount):
    print('You withdrew ₹', amount)

def deposit(amount):
    print('You deposited ₹', amount)

accountNumber = input('Enter 16 digit account number: ')
pin = int(input('Enter 4 digit account pin: '))

info = ATM(accountNumber, pin)

print('1.Withdraw')
print('2.Deposit')

option = int(input('What would you like to do: '))

if option == 1:
    amount = int(input('How much would you like to withdraw: '))
    sum = withdraw(amount)
elif option == 2:
    amount = int(input('How much would you like to deposit: '))
    sum = deposit(amount)