import random

#Global variables
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

SLOT_ROWS = 3
SLOT_COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8,
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}

#Checks the spin for matching letters in each row
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
            winning_lines.append(line +1)#adds which lines the player won on
    
    return winnings, winning_lines

#Gets a new slot spin and saves it in a nested list
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]#this makes sure that we make a copy instead of a reference
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)
    
    return columns

#prints the slot spin and transposes the nested list/matix
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="\n")

#requests a money deposit from the player
def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():#checks if the value given is a digit
            amount = int(amount)#changes the string to an integer
            if amount > 0:#checks if the given value is greater than 0
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    
    return amount

#Requests the number of lines to bet on with similar checks to deposit()
def get_number_of_lines():
    while True:
        lines = input("What number of lines would you like to bet on? (1-" + str(MAX_LINES) + ") ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:#has to be less than the global variable
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")
    
    return lines

#Requests the amount to bet per line
def get_bet():
    while True:
        amount = input("How much would you like to bet per line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:#has to be between the global variables
                break
            else:
                print(f"The bet must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")
    
    return amount

#completes a spin and returns winnings/losses
def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:#checks against current ballance
            print(f"You do not have enough balance to make that bet. Your current balance is ${balance}.")
        else:
            break
        
    print(f"You are betting ${bet} on {lines} lines. Your total bet is ${total_bet}.")
    input("Press enter to spin.")
    slots = get_slot_machine_spin(SLOT_ROWS, SLOT_COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    if winnings > 0:
        print("You won on line(s):", *winning_lines)#prints a list separated by spaces (* = splat)
        
    return winnings - total_bet

def main():
    balance = deposit()
    
    while True:
        print(f"Your current balance is ${balance}")
        play = input("Press enter to make a bet. (q to quit while you still have money) ")
        if play.lower() == "q":
            break
        balance += spin(balance)
        if balance == 0:#exits automatically if the player ran out of money
            break
        
    if balance == 0:
        print("You lost all your money.")
    else:
        print(f"You left with ${balance}!")
        
while True:
    main()
    play_again = input("Would you like to play again? Y/N ")
    if play_again.upper() == "Y":#cleaned input using upper since "or" wasn't working
        print("Here we go again!")
    elif play_again.upper() == "N":
        print("Thanks for playing!")
        break
    else:#Not going to add checks for "yes" "no" or other such things
        print("I'm not building in any more checks for a silly person like you :)\nHave a great day!")
        break