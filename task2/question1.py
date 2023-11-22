number = int(input("Enter number: "))
fact = 1

if(number < 0):
    print("Enter positive number only!!!")
else:
    for i in range(1, number+1):
        fact = fact * i
    print(fact, end=" ")

