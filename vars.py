def vars1(vars):
    if vars < 10:
        returns = 10 - vars
    else:
        returns = 0
        print('Number is greater than 10')

    return(returns)

in_num = input('please enter a number: ')
try:
    print(vars1(int(in_num)))
except:
    print('Non Numeric input detected')