def sumnumber(n):
    if n == 0:
        return 0
    return n + sumnumber(n - 1)

def get_input():
    try:
        print('\n---Sum Up Numbers---')
        snum = input('\nEnter a number: ').strip()

        if snum == '':
            print('Cannot be blank')
            return

        snum = int(snum)  

        if snum < 0:
            print('Cannot be a negative number')
            return
        
        total = sumnumber(snum)

        sum_str = ""
        for i in range(snum, 0, -1):
            sum_str += str(i)  
            if i != 1:  
                sum_str += ' '
        
        print(sum_str + ' = ' + str(total))

    except:
        print('Must be a whole number')
        return

def recur1():
    get_input()

    ans = input('\nAgain, y/n?: ').strip()
    if ans == 'y':
        recur1()  
    elif ans == 'n':
        print('\n---Done!---')
    else:
        print("Please enter 'y' or 'n'.")
        recur1()
        
recur1()







    
