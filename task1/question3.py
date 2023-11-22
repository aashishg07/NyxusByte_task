n = int(input("Enter the number of elements: "))

numbers = []
odd = []
even = []

for i in range(n):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

sum_of_odd = sum(odd)
sum_of_even = sum(even)

print(f"Sum of odd numbers: {sum_of_odd}")
print(f"Sum of even numbers: {sum_of_even}")
