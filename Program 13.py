def ask_for_number():
    number_input = input('Input number: ').strip()
    
    if number_input == '':
        print('Cannot be blank')
        return ask_for_number()
    
    try:
        number = int(number_input)
        if number == 0:
            return number
        return number
    
    except:
        print('Must be a number')
        return ask_for_number()

def main():
    roman_numerals = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V',
                      6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X',
                      11: 'XI', 12: 'XII', 13: 'XIII', 14: 'XIV', 15: 'XV',
                      16: 'XVI', 17: 'XVII', 18: 'XVIII', 19: 'XIX', 20: 'XX',
                      21: 'XXI', 22: 'XXII', 23: 'XXIII', 24: 'XXIV'}

    number = ask_for_number()

    while number > 0:
        if number in roman_numerals:
            print(number, 'is', roman_numerals[number])
        if number not in roman_numerals:
            print(number, 'not in dictionary')
            add_to_dict = input('Add ' + str(number) + ' to dictionary, y/n?: ')

            if add_to_dict == 'y':
                roman_input = input('Roman numeral ' + str(number) + ': ')

                if roman_input.isalpha():
                    roman_numerals[number] = roman_input
                    print('Added', number, ':', roman_input, 'to the dictionary')
                else:
                    print('Must be alphabetic')
            else:
                print(number, 'not added to dictionary')

        number = ask_for_number()

    print("\nRoman Numerals:")
    print(roman_numerals)

def run_again():
    continue_program = input("\nRun again, y/n?: ")
    
    if continue_program == 'y':
        main()
        run_again()
    else:
        print('Done')

main()
run_again()

