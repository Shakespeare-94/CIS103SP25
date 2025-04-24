print('Program Start')
print('Table codes: A = Add, S = Subtract, M = Multiply, D = Divide\n')

code = input('Select Table code: ')
number = float(input('Enter number for table: '))

if code == 'A':
    for _ in range(1,11):
        print(number + _, '=', number, '+', _)

if code == 'S':
    for _ in range(1,11):
        print(number - _, '=', number, '-', _)

if code == 'M':
    for _ in range(1,11):
        print(number * _, '=', number, '*', _)

if code == 'D':
    for _ in range(1,11):
        print(number / _, '=', number, '/', _)

print('Done')
