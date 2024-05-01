
import random

ROWS = 3
COLS = 3
symbol_count = {
    "a": 2,
    "b": 9,
    "c": 7,
    "d": 5,
    "f": 4,
}

def check_winning(columns, lines, bet, symbol_values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += symbol_values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines

def get_slot_machine(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()

def deposit():
    while True:
        amount = input("Please enter the amount you want to deposit: ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return amount

def no_of_lines():
    while True:
        no_of_lines = input("Please enter the number of lines you want to bet on (1-3): ")
        if no_of_lines.isdigit():
            no_of_lines = int(no_of_lines)
            if 0 < no_of_lines < 4:
                break
            else:
                print("Amount must be greater than 0 and less than 4.")
        else:
            print("Please enter a number.")
    return no_of_lines

def bet_get():
    while True:
        bet = input("Please enter your bet amount: ")
        if bet.isdigit():
            bet = int(bet)
            if bet > 0:
                break
            else:
                print("Bet amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return bet

def main():
    balance = deposit()
    while True:
        lines = no_of_lines()
        while True:
            bet = bet_get()
            total_bet = bet * lines
            if total_bet > balance:
                print(f"You don't have enough balance to bet. Your current balance is ${balance}.")
            else:
                break
        
        print(f"You are betting ${bet} on {lines} lines. Total bet is equal to ${total_bet}.")
        balance -= total_bet
        slots = get_slot_machine(ROWS, COLS, symbol_count)
        print_slot_machine(slots)
        winnings, lines_winnings = check_winning(slots, lines, bet, symbol_count)
        balance += winnings
        print(f"You have won ${winnings}.")
        if lines_winnings:
            print("You won on lines:", *lines_winnings)
        print(f"Your new balance is ${balance}.")
        
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break
        elif balance <= 0:
            print("You have run out of balance.")
            break

main()
