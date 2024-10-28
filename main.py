# Code goes here and DO NOT FORGET INTRO COMMENTS
import random


def menu():
    choice = input('Select an option:\n \tC- circle\n \tL-line\n \tR-random\n \tE-exit\n \t Type selection here:')
    choice = choice.upper()
    while choice != 'C' and choice != 'L' and choice != 'R' and choice != 'E':
        choice = input('Select an option:')
        choice = choice.upper()
    return choice



def circle():
    print('   -----   \n /       \ \n \       /\n   -----  ')


def line():
    character = input('What character would you like to make up the line?: ')
    char_amt = (input('How many characters would you like?: '))
    while not char_amt.isdigit():
        print('Please enter a valid number.')
        char_amt = input('How many characters would you like?: ')
    char_amt = int(char_amt)
    lines = (input('How many lines would you like?: '))
    while not lines.isdigit():
        print('Please enter a valid number.')
        lines = input('How many lines would you like?: ')
    lines = int(lines)
    count = 0
    while count < lines:
        print(character * char_amt)
        count += 1

def random1():
    print('')


def random2():
    print('')


def random3():
    print('')



def random_choice():
    num = random.randint(1,3)
    if num == 1:
        random1()
    elif num == 2:
        random2()
    elif num == 3:
        random3()



def exit_game():
    print('Thanks for playing!')



def main():
    print('This program allows users to select patterns that will be displayed.')
    choice = menu()
    while choice != 'E':
        if choice == 'C':
            circle()
        elif choice == 'L':
            line()
        elif choice == 'R':
            random_choice()
    exit_game()

main()