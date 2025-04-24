c_p_m = 4.33  # calories per minute
again = 'y'

while again == 'y':
    r_m = input('Enter running minutes: ')  # running minutes

    if r_m.isspace() or r_m == '':
        print('Minutes cannot be blank')
    else:
        r_m = int(r_m)
        if r_m < 5:
            print('Minutes must be greater than 5')
        elif r_m > 5:
            for minutes in range(5, r_m + 1, 5):
                print('Minutes:', minutes, 'Calories:', c_p_m * minutes)
        else:
            print('Minutes cannot be greather than 30')

    again = input('Again? (y/n): ')
    if again == 'n':
        print('----------------------------')
        print('Done!')
    else:
        print('----------------------------')
