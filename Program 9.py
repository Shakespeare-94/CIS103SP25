def main():
    #1 Acres to Hectares conversion
    try:
        acres = float(input('Enter Acres: '))
        if acres < 0:
            print('Input error - Acres')
        else:
            hectares = acres * 0.4047
            print(acres, 'converts to', hectares)
    except:
        print('Input error - Acres')

    print('--------------------------')

    #2 Quarts to Liters conversion
    try:
        quarts = float(input('Enter Quarts: '))
        if quarts < 0:
            print('Input error - Quarts')
        else:
            liters = quarts * 0.946353
            print(quarts, 'converts to', liters)
    except:
        print('Input error - Quarts')

    print('--------------------------')

    #3 Fahrenheit to Kelvin conversion
    try:
        fahrenheit = float(input('Enter Fahrenheit: '))
        kelvin = (fahrenheit - 32) * (5/9) + 273.15
        print(fahrenheit, 'converts to', kelvin)
    except:
        print('Input error - Fahrenheit')

    print('--------------------------')

again = 'y'
while again == 'y':
    main()  
    again = input('Again, y/n?: ')
    print('--------------------------')
    print('--------------------------')

print('Done!')

