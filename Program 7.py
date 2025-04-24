M = int(input('Miles: '))

def distance_formula(m, dec): #m == miles & dec == 1.609344
    kilometers = m * dec
    return kilometers

m = M
dec = float(1.609244)
kilometers = m * dec
print('Kilometers: ', kilometers)

print('----------------------')

LB = int(input('Weight: '))

def weight_formula(lb, dec): #m == miles & dec == 0.45359237
    kilograms = lb * dec
    return kilograms

lb = LB
dec = float(0.45359237)
kilograms = lb * dec
print('Kilograms: ', kilograms)

print('----------------------')

F = int(input('Farenheit: '))
    
def temperature_formula(f):
    celsius = (f - 32) * 5/9
    return celsius

f = F
celsius = (f-32) * 5/9
print('Celsius: ', celsius)  

print('----------------------')
print('         Done!        ')
