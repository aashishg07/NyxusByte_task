set1 = set()
set2 = set()

print("Enter the numbers for the first set:")
numbers = input().split()
set1 = set(int(num) for num in numbers) 

print("Enter the numbers for the second set:")
numbers = input().split()
set2 = set(int(num) for num in numbers)

print("\nIntersection of the two sets:", set1.intersection(set2))
print("Union of the two sets:", set1.union(set2))



