import random
import time

subject = [
    "Shahrukh Khan",
    "Virat Kohli",
    "Nirmala Sitharaman",
    "A Cat",
    "A Group of Monkeys",
    "Prime Minister",
    "Auto Rickshaw Driver from Sukkur"
]

actions = [
    "launches",
    "cancels",
    "dances with",
    "eats",
    "declares war on",
    "orders",
    "celebrates",
]

places_things = [
    "at Red Fort",
    "in Sukkur Local Train",
    "a plate of Samosa",
    "inside parliament",
    "sukkur local market",
    "during a cricket match",
    "a plate of biryani",
]

while True:
    print("Breaking News: " + random.choice(subject) + " " + random.choice(actions) + " " + random.choice(places_things))
    time.sleep(1)
    if input("Continue Y/N: ").upper().strip() != "Y":
        break