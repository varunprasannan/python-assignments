account_balance = 100000


def deposit(number):
    global account_balance
    account_balance += number
    print("You have deposited Rs.{} and your total available balance is {}".format(number, account_balance))


def withdraw(number):
    global account_balance
    if(account_balance < number):
        print("You can't withdraw Rs.{} as your available balance is insufficient".format(number))
    else:
        account_balance -= number
        print("You have withdrawn Rs.{} and your total available balance is {}".format(number, account_balance))

