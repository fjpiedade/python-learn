import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1


def deposit():
    while True:
        amount = input("Please, what is your amount? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Please most be great than 0.")
        else:
            print("Please enter a Number.")
    return amount


def get_number_of_lines():
    while True:
        lines = input(f"Please, Enter the number of Lines (1 - {MAX_LINES})? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f"Please, Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a Number.")
    return lines


def get_bet():
    while True:
        amount = input(f"Please, What would you like to bet? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print("Please Enter valid number of lines.")
        else:
            print("Please enter a Number.")
    return amount


def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: {balance}")

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    print(balance, lines, bet)


main()
