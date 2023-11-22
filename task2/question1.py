"""
1. The factorial of a non-negative integer N, denoted by N!, is the product of all positive
integers less than or equal to N.   5! = 5 x 4 x 3 x 2 x 1 = 120

"""


def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * fact(n - 1)
    
print(fact(5))

    

