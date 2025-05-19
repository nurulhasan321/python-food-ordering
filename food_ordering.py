menu = {
    "Pizza": 299,
    "Burger": 199,
    "Sandwich": 249,
    "Paneer_Butter": 279,
    "Biryani": 329,
    "Dosa": 149,
    "Pasta": 259,
    "Tandoori": 349,
    "French_Fries": 99,
    "Chocolate_Brownie": 129
}

lowercase_menu = {key.lower(): value for key, value in menu.items()}

# Print menu
print("Menu:")
for item, price in menu.items():
    print(f"- {item}: ₹{price}")

order_amount = 0


while True:
    item = input("Choose one item that you want to order: ").lower()
    
    if item in lowercase_menu:
        order_amount += lowercase_menu[item]
        print(f"Item '{item.title()}' added successfully.")
    else:
        print("Item is not available!")

    another_order = input("Do you want to add another item? (Y/N): ").lower()
    if another_order != "y":
        break


print(f"\n🧾 Total order amount is ₹{order_amount}")
