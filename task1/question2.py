import random

rand_num = random.randint(1, 100)
print(rand_num)

attempt = 3

for num in range(attempt):
    guess_num = int(input("Enter your guessed number: "))
    if (guess_num == rand_num):
        print("Your guessed number matched.")
        break
    elif(guess_num > rand_num):
        print("Your guessed number greater than random number.")
    elif(guess_num < rand_num):
        print("Your guessed number lower than random number.")

