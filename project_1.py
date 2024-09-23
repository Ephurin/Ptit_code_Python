def deposit():
    while True:
        amount = input('What would you want to deposit? $')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else: print('The amount of deposit must be positive.')
        else:
            print('Please enter a number.')

    return amount
def main():
    balance = deposit()