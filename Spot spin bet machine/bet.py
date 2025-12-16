import random
import os
import time
import shutil
import ctypes
import sys

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

# ANSI / color helpers
RESET = "\033[0m"
BOLD = "\033[1m"
FG_RED = "\033[31m"
FG_GREEN = "\033[32m"
FG_YELLOW = "\033[33m"
FG_BLUE = "\033[34m"
FG_MAGENTA = "\033[35m"
FG_CYAN = "\033[36m"
FG_WHITE = "\033[37m"

SYMBOL_COLORS = {
    "A": FG_MAGENTA,
    "B": FG_CYAN,
    "C": FG_YELLOW,
    "D": FG_WHITE
}


def enable_windows_ansi():
    if os.name == "nt":
        kernel32 = ctypes.windll.kernel32
        mode = ctypes.c_uint()
        handle = kernel32.GetStdHandle(-11)  # STD_OUTPUT_HANDLE = -11
        if kernel32.GetConsoleMode(handle, ctypes.byref(mode)):
            kernel32.SetConsoleMode(handle, mode.value | 0x0004)  # ENABLE_VIRTUAL_TERMINAL_PROCESSING


enable_windows_ansi()


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def term_width():
    try:
        return shutil.get_terminal_size().columns
    except Exception:
        return 80


def center(text):
    width = term_width()
    lines = text.splitlines()
    return "\n".join(line.center(width) for line in lines)


def print_title():
    art = r"""
   _____        _       _    ____  _       _           
  / ____|      (_)     | |  |  _ \(_)     | |          
 | (___   _ __  _  __ _| |__| |_) |_  __ _| | ___  ___ 
  \___ \ | '_ \| |/ _` | '_ \  _ <| |/ _` | |/ _ \/ __|
  ____) || |_) | | (_| | | | | |_) | | (_| | |  __/\__ \
 |_____/ | .__/|_|\__, |_| |_|____/|_|\__,_|_|\___||___/
         | |       __/ |                                 
         |_|      |___/                                  
"""
    subtitle = "A simple slot machine — Good luck!"
    print(FG_GREEN + BOLD + center(art) + RESET)
    print(FG_CYAN + center(subtitle) + RESET)
    print(center("-" * min(60, term_width())))


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
    for symbol, count in symbols.items():
        all_symbols += [symbol] * count

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


def format_cell(symbol, highlight=False):
    color = SYMBOL_COLORS.get(symbol, FG_WHITE)
    style = BOLD if highlight else ""
    return f"{style}{color}{symbol}{RESET}"


def print_slot_machine(columns, winning_lines=None, header=""):
    if winning_lines is None:
        winning_lines = []
    width = term_width()
    if header:
        print(center(header))
    for row in range(len(columns[0])):
        row_elems = []
        highlight = (row + 1) in winning_lines
        for i, column in enumerate(columns):
            sym = column[row]
            cell = format_cell(sym, highlight)
            row_elems.append(f" {cell} ")
        line = " | ".join(row_elems)
        print(center(line))
    print(center("-" * min(60, width)))


def animate_spin(rows, cols, symbols, duration=1.2, steps=20):
    start = time.time()
    interval = max(0.01, duration / steps)
    end = start + duration
    while time.time() < end:
        # create a fake transient spin display
        columns = []
        for _ in range(cols):
            column = [random.choice(list(symbols.keys())) for _ in range(rows)]
            columns.append(column)
        clear_screen()
        print_title()
        print_slot_machine(columns, header=FG_YELLOW + "Spinning..." + RESET)
        time.sleep(interval)


def deposit():
    clear_screen()
    print_title()
    while True:
        amount = input(FG_CYAN + "What would you like to deposit? $ " + RESET)
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print(FG_RED + "Amount must be greater than zero." + RESET)
        else:
            print(FG_RED + "Please enter a valid number." + RESET)
    return amount


def get_number_of_lines():
    while True:
        lines = input(FG_CYAN + f"Enter number of lines to bet on (1-{max_lines}): " + RESET)
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= max_lines:
                break
            else:
                print(FG_RED + f"Please enter a number between 1 and {max_lines}." + RESET)
        else:
            print(FG_RED + "Please enter a valid number." + RESET)
    return lines


def get_bet():
    while True:
        bet = input(FG_CYAN + f"What would you like to bet on each line? (${min_bet}-${max_bet}): " + RESET)
        if bet.isdigit():
            bet = int(bet)
            if min_bet <= bet <= max_bet:
                break
            else:
                print(FG_RED + f"Bet must be between ${min_bet} - ${max_bet}." + RESET)
        else:
            print(FG_RED + "Please enter a number." + RESET)
    return bet


def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(FG_RED + f"You do not have enough to bet that amount. Current: ${balance}" + RESET)
        else:
            break

    print(FG_YELLOW + f"You are betting ${bet} on {lines} line(s). Total bet: ${total_bet}" + RESET)
    print()

    # Animate the spin
    animate_spin(rows, cols, symbols_count, duration=1.0, steps=12)

    # Final spin result
    columns = get_slot_machine_spin(rows, cols, symbols_count)
    winnings, winning_lines = check_winnings(columns, lines, bet, symbols_value)

    clear_screen()
    print_title()
    header = FG_GREEN + BOLD + "Result" + RESET
    print_slot_machine(columns, winning_lines, header=header)

    if winnings > 0:
        print(center(FG_GREEN + BOLD + f"Congrats! You won ${winnings} on line(s): {', '.join(map(str, winning_lines))}" + RESET))
    else:
        print(center(FG_RED + "No winning lines this spin. Better luck next time!" + RESET))

    print()
    input(FG_CYAN + "Press Enter to continue..." + RESET)
    return winnings - total_bet


def prompt_continue():
    ans = input(FG_CYAN + "Press Enter to spin again, (d)eposit, or (q)uit: " + RESET).strip().lower()
    return ans


def main():
    balance = deposit()
    while True:
        clear_screen()
        print_title()
        print(center(FG_YELLOW + f"Current balance: ${balance}" + RESET))
        ans = input(FG_CYAN + "Press Enter to spin (q to quit, d to deposit more): " + RESET).strip().lower()
        if ans == "q":
            break
        if ans == "d":
            balance += deposit()
            continue
        balance_change = spin(balance)
        balance += balance_change
        if balance <= 0:
            print(center(FG_RED + "You've run out of money. Game over." + RESET))
            break
        time.sleep(0.8)
    clear_screen()
    print_title()
    print(center(FG_MAGENTA + BOLD + f"You left with ${balance}" + RESET))
    print()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        clear_screen()
        print(center(FG_RED + "\nGame interrupted. Bye!" + RESET))
        sys.exit(0)
