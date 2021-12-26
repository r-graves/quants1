def vars1(vars):
    if vars < 10:
        returns = 10 - vars

    return(returns)

in_num = input('please enter a number')
print(vars1(int(in_num)))