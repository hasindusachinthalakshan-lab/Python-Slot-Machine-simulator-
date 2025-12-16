import random
max_lines = 3
max_bet = 100
min_bet = 1 

rows = 3
cols = 3

symbols_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbols_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbols_count in symbols.items():
        for _ in range(symbols_count):
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
            if i != len(columns) -1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()


def deposit():
    while True:
        amount = input("What would you like to deposit?: $")
        if amount.isdigit():
            amount = int(amount)
            if amount >0:
                break
            else:
                print("Amount must be greater than zero.")
        else:
            print("Please enter a valid number.")
    return amount


def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{max_lines}): ")
        if lines.isdigit():
            lines = int (lines)
            if 1 <= lines <= max_lines:
                break
            else:
                print(f"Please enter a number between 1 and {max_lines}.")
        else:
            print("Please enter a valid number.")
    return lines


def get_bet():
    while True:
        bet = input("What would you like to bet on each line? : $")
        if bet.isdigit():
            bet = int(bet)
            if min_bet <= bet <= max_bet:
                break
            else:
                print(f"Bet must be between ${min_bet} - ${max_bet}.")
        else:
            print("Please enter a number.")
    return bet



def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines.Total bet is equal to : ${total_bet}")
    print()

    columns = get_slot_machine_spin(rows, cols, symbols_count)
    print_slot_machine(columns)
    winnings, winning_lines = check_winnings(columns, lines, bet, symbols_value)
    print()
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)

    return winnings - total_bet

    
def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to spin (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)
    print(f"You left with ${balance}")


main()