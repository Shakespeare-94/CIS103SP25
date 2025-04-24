price = float('.99')
gross_sale = ('pounds * price')
dis_one = float('.10')
dis_two = float('.20')
dis_three = float('.30')
dis_four = float('.40')

pounds = float(input('Enter number of pounds: '))
if(pounds >= 10) and (pounds <= 99.99):
    print('Gross Sales: ', pounds * price)
    print('Discount Amount: ', pounds * price * dis_one)
    print ('Final Amount: ', pounds * price - pounds * price * dis_one)
elif (pounds >=100) and (pounds <=999.99):
    print('Gross Sales: ', pounds * price)
    print('Discount: ', pounds * price * dis_two)
    print ('Final Amount: ', pounds * price - pounds * price * dis_two)
elif (pounds >=1000) and (pounds <=9999.99):
    print('Gross Sales: ', pounds * price)
    print('Discount: ', pounds * price * dis_three)
    print ('Final Amount: ', pounds * price - pounds * price * dis_three)
elif (pounds >= 10000):
    print('Gross Sales: ', pounds * price)
    print('Discount: ', pounds * price * dis_four)
    print ('Final Amount: ', pounds * price - pounds * price * dis_four)
else:
    print('Final Amount: ', pounds * price)

