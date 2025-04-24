# property tax program calculator 2
def getinput(msg):
    xin = float(input(msg))
    return xin

def main():
    print('\n'*1)
    AssesmentLevel = .10
    HomeOwnerEx = 500.43
    SeniorCEX = 357.45
    PropertyValue = getinput('Enter value of property: ')
    LocalTaxRate = getinput('Enter local tax rate: ')
    StateEqualizer = getinput('Enter state equalizer rate: ')
    print('\n'*1)
    AssessedValue= PropertyValue * AssesmentLevel
    EqualizeValue = AssessedValue * StateEqualizer
    PropertTaxBefore = EqualizeValue * LocalTaxRate
    TotalPropertyTax = PropertTaxBefore - HomeOwnerEx - SeniorCEX
    print('\n'*1)
    print('Property tax due: ', TotalPropertyTax)
    print('\n'*1)
    return
main()

# EVP: 259440
# ELTR: 0.07149
# ESER: 2.8032
