import random

MAX_LINES = 3
MAX_BET = 10000
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A":3,
    "B":3,
    "C":3,
    "D":4,
    "E":5,
    "F":6,
    "G":7,
    "H":8,
    "I":9,
    "J":3,
    "K":3,
    "L":3,
    "M":4,
    "N":5,
    "O":6,
    "P":7,
    "Q":8,
    "R":9,
    "S":3,
    "T":3,
    "U":3,
    "V":4,
    "W":5,
    "X":6,
    "Y":7,
    "Z":8
}

symbol_value = {
    "A":26,
    "B":25,
    "C":24,
    "D":23,
    "E":22,
    "F":21,
    "G":20,
    "H":19,
    "I":18,
    "J":17,
    "K":16,
    "L":15,
    "M":14,
    "N":13,
    "O":12,
    "P":11,
    "Q":10,
    "R":9,
    "S":8,
    "T":7,
    "U":6,
    "V":5,
    "W":4,
    "X":3,
    "Y":2,
    "Z":1
}

def get_win(columns, lines, bet, values):
    winnings = 0
    for line in range(lines):
        symbol = columns[0][line]
        win = True
        for column in columns:
            if column[line] != symbol:
                win = False
                break
        if win:
            winnings += values[symbol] * bet
    return winnings

def get_slot(rows, cols, symbols):
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
                print(column[row], end=" |♦| ")
            else:
                print(column[row], end="\n")

def deposit():
    while True:
        amount = input("\nHow much are you depositing? \n$")
        if amount.isdigit():
            amount = int(amount)
            if amount == 69:
                print(f"He-he-he.... 69\n")
                break
            if amount > 0:
                print(f"\n{amount} bucks, lil man, put that shit in my hand.\n")
                break
            else:
                print("Does Jay have to slap a hoe?\n")
        else:
            print("ENTER A NUMBER... Dick!\n")
    return amount

def get_num_of_lines():
    while True:
        lines = input("How many lines are you betting on, my guy? (1-" + str(MAX_LINES) + ") \n>")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("\n*AHEM*. I thought I was clear. HOW MANY LINES? 1 TO " + str(MAX_LINES) + ". Now...\n")
        else:
            print("\nFuck yourself!\n")
    return lines

def get_bet():
    while True:
        bet = input("\nHow much are you betting on each line? up to $" + str(MAX_BET) + " \n$")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print("\nHow many times do I have to teach you this lesson, old man?!?\n")
        else:
            print("\nENTER A NUMBER... Dick!\n")
    return bet

def main():
    initial_balance = deposit()
    current_balance = initial_balance

    while True:
        if current_balance <= 0:
            print("\nYou are out of money, sucks to suck... Byeeeeeee!")
            break
        
        print(f"\nBalance: ${current_balance}\n")
        
        lines = get_num_of_lines()
        
        while True:
            bet = get_bet()
            total_bet = bet * lines

            if total_bet > current_balance:
                print(f"\nBroke ass bitch! Your balance is ${current_balance}.\n")
            else:
                print(f"\n{total_bet} bucks, lil man, put that shit in my hand.\n")
                break

        print(f"\nTotal bet is ${total_bet}\n")
        current_balance -= total_bet
        print(f"\nBet ${total_bet}\nNew Balance ${current_balance}\n")

        slots = get_slot(ROWS, COLS, symbol_count)
        print_slot_machine(slots)
        winnings = get_win(slots, lines, bet, symbol_value)

        if winnings > 0:
            print(f"Congratulation! You won ${winnings}!\n")
        else:
            print("HA! NERRRRRD! YOU WON NOTHING!\n")

        current_balance += winnings
        print(f"New Balance: ${current_balance}\n")

        play_again = input("You playing again?\n (y/n)> ").strip().lower()
        if play_again != 'y':
            print(f"FINE! I didn't wanna play anyway! Just take your ${current_balance} and GO! GOODBYE!")
            break
main()
