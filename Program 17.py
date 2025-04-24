from random import *

def displaymenu():
    print('-'*50)
    print('Illinois Lottery!')
    print('\n1. Powerball')
    print('2. Mega Million')
    print('3. Lucky Day Lotto')
    print('4. Lotto')
    print('\n9. Quit')

def powerball():
    numbers = []
    while len(numbers) < 5:
        num = int(random() * 69) + 1  
        if num not in numbers:
            numbers.append(num)
    numbers.sort()
    print('Powerball Numbers:', *numbers)

def mega_million():
    numbers = []
    while len(numbers) < 5:
        num = int(random() * 70) + 1  
        if num not in numbers:
            numbers.append(num)
    numbers.sort()
    print('Mega Million Numbers:', *numbers)

def lucky_day_lotto():
    numbers = []
    while len(numbers) < 5:
        num = int(random() * 45) + 1  
        if num not in numbers:
            numbers.append(num)
    numbers.sort()
    print('Lucky Day Lotto Numbers:', *numbers)

def lotto():
    numbers = []
    while len(numbers) < 6:
        num = int(random() * 52) + 1  
        if num not in numbers:
            numbers.append(num)
    numbers.sort()
    print('Lotto Numbers:', *numbers)

def main():
    used_choices = []

    for _ in range(10):
        displaymenu()
        choice = input('\nPlease select a game (1-4) or 9 to Quit:')

        if choice == '9':
            print('\nThank you for playing!')
            break

        if not choice.isdigit():
            print('\nError. Please select a game (1-4) or 9 to Quit.')
            continue

        used_choices.append(choice)

        if choice == '1':
            powerball()
        elif choice == '2':
            mega_million()
        elif choice == '3':
            lucky_day_lotto()
        elif choice == '4':
            lotto()
        else:
            print('\nError. Please select a game (1-4) or 9 to Quit.')
            continue

        input('\nHit Enter key to return to menu')

if __name__ == '__main__':
    main()
