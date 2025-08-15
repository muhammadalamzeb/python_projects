import random


while True:
    n = input("Roll the dice? Y/N: ").lower()
    if n == "n":
        break
    elif n == "y":
        d1 = random.randint(1,6)
        d2 = random.randint(1,6)
        print(f"{d1,d2}You rolled a")
    else:
        print("Invalid input. Please enter Y or N.")
        
#n = input("Roll the dice? Y/N: ")
#print(f"{n}???")

