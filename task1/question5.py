def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter the operation (+,-,*,/): ")

result = 0

if operation == '+':
    result = add(num1, num2)

elif operation == '-':
    result = sub(num1, num2)

elif operation == '*':
    result = mul(num1, num2)

elif operation == '/':
    result = div(num1, num2)

else:
    print("Invalid operation")

print(f"Result is: {result}")
    