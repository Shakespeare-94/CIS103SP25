name = input('Name: ')
if name.isspace() or name =='':
    print('Name cannot be blank\n')
elif (len(name) < 3):
    print('Name to short\n')
elif name.isalpha() == False:
    print('Name must be alphabetic\n')
else: print('Valid\n')

acct = input('Account Number: ')
if acct.isspace() or acct == '':
    print('Account number cannot be blank\n')
elif acct.isnumeric() == False:
    print('Account number must be numeric\n')
elif (len(acct) != 9):
    print('Account number must be 9 digits\n')
else: 
    print('Valid\n')

pymt = input('Payment: ')
if name.isspace() or pymt == '':
    print('Payment cannot be blank\n')
elif float(pymt) == 0:
        print('Payment cannot be zero\n')
elif float(pymt) < 0:
      print('Payment cannot be negative\n')
else:
    print('Valid\n')
