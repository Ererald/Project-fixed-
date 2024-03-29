import random

TOTAL_LINES = 5
MAX_BET = 100
MIN_BET = 0
LINE_SYMBOLS = {"Apple": 2, "Banana": 2, "Orange": 2, "Peach": 2, "Watermelon": 2, "Grape": 2, "Cherry": 2,
                "Pineapple": 2}

value_list = list(LINE_SYMBOLS.keys())


def deposit():
    while True:
        amount = input("Insert the amount that you would like to deposit €")
        if amount.isdigit():
            amount = int(amount)
            if amount > MAX_BET:
                print(f"Let's start by little at a time. Maximum amount allowed is €{MAX_BET}")
            elif amount == 69:
                print("Nice  (͡°͜ʖ͡°)")
                break
            elif amount > MIN_BET:
                break
            else:
                print(f"You can't win if you don't first bet! Minimum amount must be greater than €{MIN_BET}")
    return amount


def line_numbers():
    while True:
        lines = input(
            f"On how many columns would you like to try your luck? Please choose between 3 and {TOTAL_LINES} -> ")
        if lines.isdigit():
            lines = int(lines)
            if 3 <= lines <= TOTAL_LINES:
                break
            elif lines > TOTAL_LINES:
                print("Not so fast! Please bet on a valid number of columns")
            else:
                print("Please bet on a valid number of columns")
    return lines


def bet_amount(total_balance):
    while True:
        amount = input(f"Insert the amount that you would like to bet € ")
        if amount.isdigit():
            amount = int(amount)
            if 1 <= amount <= total_balance:
                break
            if amount == 0:
                print("You must bet something if you want to win! Please retry.")
            else:
                print(
                    f"You are currently missing €{amount - total_balance} to place that bet. Your inserted amount cannot exceed your current total balance of {total_balance}.")
    return amount


def confirm_data(total_balance, column, bet):
    while True:
        print(f"Deposit: €{total_balance}")
        print(f"Bet: €{bet}")
        print(f"Columns: {column}")
        print(f"Potential earnings: {bet * column}")
        user_input = input("Do you confirm? (yes/no): ").lower()
        if user_input == "yes":
            return True
        elif user_input == "no":
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


def symbol_in_column(value_list, column, bet):
    random_signs = random.sample(value_list, column)
    unique_symbols = set(random_signs)
    symbols_string = "|".join(unique_symbols)
    print(f"{'*CLING*' * 3} {symbols_string}")
    return unique_symbols


def win_conditions(symbols):
    symbol_list = list(symbols)
    for symbol in symbol_list:
        if symbol_list.count(symbol) >= 3:
            return True
    return False


def save_balance(total_balance):
    with open("balance.txt", "w") as file:
        file.write(str(total_balance))


def load_balance():
    try:
        with open("balance.txt", "r") as file:
            balance = int(file.read())
        return balance
    except FileNotFoundError:
        balance = deposit()
        save_balance(balance)
        return balance


def total_balance(load_balance):
    balance = load_balance()
    if balance == 0:
        user_input = input("Your balance is 0. Enter 'yes' to start a new game, or 'no' to quit: ").lower()
        if user_input == "yes":
            return deposit()
        elif user_input == "no":
            print("Thank you for playing. Goodbye!")
            return balance
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
            return balance
    return balance


def main():
    total_balance = load_balance()

    while True:
        if total_balance <= 0:
            user_input = input("Your balance is 0. Enter 'yes' to start a new game, or 'no' to quit: ").lower()
            if user_input == "yes":
                total_balance = deposit()  # Calling deposit() and update the balance
            elif user_input == "no":
                print("Thank you for playing. Goodbye!")
                return
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
                continue

        # Starting the main game loop
        user_input = input(f"Your current balance is €{total_balance}. Enter 'yes' to continue, or 'no' to quit: ").lower()
        if user_input == "no":
            print("Thank you for playing. Goodbye!")
            return
        elif user_input != "yes":
            print("Invalid input. Please enter 'yes' or 'no'.")
            continue

        column = line_numbers()
        bet = bet_amount(total_balance)
        if not confirm_data(total_balance, column, bet):
            continue

        symbols = symbol_in_column(value_list, column, bet)
        if win_conditions(symbols):
            print("Wow! You won!! Congratulations!")
            total_balance += bet
        else:
            print("Better luck next time! ")
            total_balance -= bet
        save_balance(total_balance)

if __name__ == "__main__":
    main()
