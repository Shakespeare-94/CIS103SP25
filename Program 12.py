def a_e(number):
    try:
        number = float(number)
        if number < 0:
            return 'Cannot be negative'
        return True
    except:
        return 'Invalid number'

    if number == '':
        return 'Cannot be blank'

def main():
    rain_fall_file = 'c:/CIS103/rainlist.txt'
    
    file_rain_fall = open(rain_fall_file, 'r')
    rain_fall_list = []
    invalid_df = False
    error_message = []

    for line in file_rain_fall:
        line = line.strip()
        if 'Rainfall for Chicago (2017):' in line or 'Note: Data from the National Climate Data Center' in line:
            continue

        if line != '':
            try:
                month, rainfall = line.split(':', 1)
                rainfall = rainfall.strip()

                v_r = a_e(rainfall)
                if v_r == True:
                    rain_fall_list.append(float(rainfall))
                else:
                    invalid_df = True
                    error_message.append(month + ': ' + v_r)
            except:
                invalid_df = True
                error_message.append('Error: ' + line)

    file_rain_fall.close()

    if len(rain_fall_list) > 0:
        highest = max(rain_fall_list)
        lowest = min(rain_fall_list)
        total = sum(rain_fall_list)
        average = total / len(rain_fall_list)

        print('Rainfall for Chicago in 2017:')
        print('-----------------------------')
        print('Highest:', highest)
        print('Lowest:', lowest)
        print('Total:', total)
        print('Average:', average)
    else:
        print('No data')

    if invalid_df:
        print('\nError:')
        for error in error_message:
            print(error)

main()
