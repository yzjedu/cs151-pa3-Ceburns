# Programmers:  Caitlin Burns
  # Course:  CS151, Professor Zee
  # Due Date: 11/7
  # Programming Assignment:  PA3
  # Problem Statement:  displays a list of designs from users to choose from and displays the correlating design
  # Data In: design choice, character choice, length of lines, amount of lines
  # Data Out:  designs
  # Credits: this is based on the read me file and the designs are ones I made
import random


# Purpose: displays a menu for the user to choose from
# Parameters:none
# Return: choice
def menu():
    choice = input('Select an option:\n \tC- circle\n \tL-line\n \tR-random\n \tE-exit\n \t Type selection here:')
    choice = choice.upper()
    while choice != 'C' and choice != 'L' and choice != 'R' and choice != 'E':
        choice = input('Select an option:')
        choice = choice.upper()
    return choice


# Purpose: displays circle design
# Parameters:none
# Return: none
def circle():
    print('   -----   \n /       \ \n \       /\n   -----  ')


# Purpose: displays line design and asks questions to display line
# Parameters:none
# Return: none
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


# Purpose: displays first random design
# Parameters:none
# Return: none
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


# Purpose: displays second random design
# Parameters:none
# Return: none
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



# Purpose: displays third random design
# Parameters:none
# Return: none
def random3():
    space = ' '
    lines = '_'
    count = 0
    spaces = 20
    spaces2 = 6
    print(f'{space * 22}{lines*7}')
    while count < 2:
        print(f'{space * spaces}//{space * spaces2} \ ')
        count += 1
        spaces -= 1
        spaces2 += 2
    print(f'{space*7}{lines*11}//  {lines * 7}  \ {lines*15}')
    print(f'{space*6}|=| {space *8} || {space*6} ==|{space*15}|')
    print(f'{space*6}| {space *4}{lines*3}{space*4}|| {space*8} |{space*6}{lines*3}{space*6}|')
    print(f'{space*6}|{lines*3}/ ___ \{lines*19}/ ___ \{lines*4}| ')
    print(f'{space*10}/{space*5}\ {space*18}/{space*5}\ ')
    print(f'{space*10}\{5* lines}/{space*19}\{lines*5}/ ')



# Purpose: chooses between the three random designs when user selects random
# Parameters: none
# Return: none
def random_choice():
    num = random.randint(1,3)
    if num == 1:
        random1()
    elif num == 2:
        random2()
    elif num == 3:
        random3()


# Purpose: allows user to exit game
# Parameters:none
# Return: none
def exit_game():
    print('Thanks for playing!')


# Purpose: runs main program
# Parameters: none
# Return: none
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