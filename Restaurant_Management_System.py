menu = {
    'Pizza' : 40,
    'Pasta' : 50,
    'Burger' : 60,
    'Salad' : 70,
    'Coffee' : 80,
}

print("Welcome to Sukkur IBA Restaurant")
for key,value in menu.items():
    print(f"{key} costs {value} PKR")

order_total = 0

while True:
    item_1 = input("Please place your order: ").capitalize()
    if item_1 in menu:
        order_total += menu[item_1]
        print(f"Your item {item_1} has been added to the order")
        print(f"Total Amount: {order_total} PKR")
    else:
        print("Sorry, we do not have this item in our menu")
    again = input("Do you want to order something else? (y/n): ").lower()
    if again == 'n':
        break