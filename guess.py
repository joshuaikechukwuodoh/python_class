import random

user_guess = input("Type a number: ")

if user_guess.isdigit():
    user_guess = int(user_guess)
else:
    print("This is not an integer")
    quit()

computer_guess = random.randint(1, 30)

score = 0
while True:
    score += 1
    user_guess = input("Type a number: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("This is not an integer")
        continue

    if user_guess == computer_guess:
        print(f"You win! It took you {score} attempts.")
        break
    else:
        print("Try again!")
