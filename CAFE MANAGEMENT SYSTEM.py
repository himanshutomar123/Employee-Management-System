# ---------------------------------------------------------- CAFE MANAGEMENT SYSTEM ----------------------------------------------------------------------------------------
print("Welcome To Our Restaurant!")

menu = {
    "pizza": 300,
    "burger": 100,
    "pasta": 450,
    "sandwich": 600,
    "fries": 200,
    "milkshake": 733,
    "roll": 50
}

total = 0

print("======== MENU ========")
print("Pizza = 300")
print("Burger = 100")
print("Pasta = 450")
print("Sandwich = 600")
print("Fries = 200")
print("Milkshake = 733")
print("Roll = 50")

while True:

    choice = input("Enter item name: ").lower()

    if choice in menu:

        quantity = int(input("Enter quantity: "))

        price = menu[choice] * quantity

        total = total + price

        print("Your Order Has Been Placed")

    else:
        print("Item not available")

    anything = input("Do you want anything else? (y/n): ").lower()

    if anything == "n":
        break

print("Your Total Bill =", total)