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
    space = ' '
    count_1 = 0
    spaces = 5
    spaces2 = 0
    line = '_'
    star = '*'
    print(space * 6, '@')
    while count_1 < 3:
        print(f'{space * spaces} /{space * spaces2} \ ')
        count_1 += 1
        spaces -= 1
        spaces2 += 2
    print(f'{space * 2} /{line * 7}\ ')
    print(f'{space * 1} |{line*9}| ')
    print(space * 2, '|  ===  |')
    print(space * 1, '(|  0 0  |)')
    print(space * 2, '|   U   |')
    print(space * 2, '\*\___/*/')
    print(f'{space * 4}\{star*2} {star*2}/')
    print(f'{space*5}\{star*3}/')
    print(f'{space*7}*')

def random2():
    space = ' '
    count = 0
    star = '*'
    spaces = 5
    spaces2 = 9
    lines = '_'
    print(f'{space * 10}*')
    print(f'{space * 9}***')
    print(f'{space * 7}/{star * 5}\ ')
    print(f'{space *6}/* * * *\ ')
    while count < 2:
        print(f'{space * spaces}/{star * spaces2}\ ')
        count += 1
        spaces -= 1
        spaces2 += 2
    print(f'{space*3}/* * * * * * *\ ')
    print(f'{space * 2}/{lines*15}\ ')
    print(f'{space * 4}{star * 3} |  | {star * 3}')




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
    print('-'* 70)
    print('This program allows users to select patterns to display!')
    print('-'* 70)
    choice = menu()
    while choice != 'E':
        if choice == 'C':
            print('You chose circle')
            circle()
        elif choice == 'L':
            print('You chose line')
            line()
        elif choice == 'R':
            print('You chose random')
            random_choice()
        choice = menu()
    exit_game()

main()