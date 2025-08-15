import random

guess = random.randint(1,100)
user_guess = 0
while True:
    try:
        user_guess = int(input("Guess a number between 1 and 100: "))
    except:
        print("Value error!")

    if (user_guess >= 100 or user_guess <= 1):
        print("Please enter a number between 1 and 100")
    elif user_guess == guess:
        print("You win!")
        break
    else:
        print("Too high" if user_guess > guess else "Too low")
    