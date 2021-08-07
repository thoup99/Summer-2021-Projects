import random
import time

fin_num = int(input("Pick a number between 1 and 1,000,000: "))

while fin_num > 1000000 or fin_num < 1:
    fin_num = int(input("Please pick a number between 1 and 1,000,000: "))

min_num = 0
max_num = 1000000
num_found = False

while num_found == False:
    guess = random.randint(min_num, max_num)
    guesses = []
    while guess in guesses:
        guess = random.randint(min_num, max_num)
    if guess == fin_num:
        print("The number was found")
        print(guess)
        num_found = True
        break
    elif guess < fin_num:
        print("Higher")
        if guess > min_num:
            min_num = guess
    else:
        print("Lower")
        if guess < max_num:
            max_num = guess
    guesses.append(guess)
    print(guess)
    time.sleep(0.5)