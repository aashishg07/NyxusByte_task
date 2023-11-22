x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

def gcd(x,y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)
    
print(f"The GCD of {x} and {y} is: ",gcd(x,y))
