"""
1. The factorial of a non-negative integer N, denoted by N!, is the product of all positive
integers less than or equal to N.   5! = 5 x 4 x 3 x 2 x 1 = 120

"""


number = int(input("Enter number: "))
fact = 1

if(number < 0):
    print("Enter positive number only!!!")
else:
    for i in range(1, number+1):
        fact = fact * i
    print(fact, end=" ")

