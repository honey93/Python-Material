def hello(n):
    
    if (n  == 0): 
        return 0
    digit = n%10
    if (digit == 0):
        digit = 5
    return(hello(n/10)*10 + digit)
    
def lello(n):
    if(n == 0):
        return 5
    else:
        return hello(n)


num = 12005600
print(lello(num))

