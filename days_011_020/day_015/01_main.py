import os
import art
import data


# 1. Print resources report
# 2. Check if resources are sufficient
# 3. Process coins
# 4. Check if transaction is successful
# 5. Make the coffee

def select_product():
    os.system("cls")
    print(art.logo)

    products = "/".join(data.menu.keys())
    product = input(f"What would you like? ({products}): ").lower()

    if product in data.menu:
        cost = data.menu[product]["cost"]
        print(f"You have selected: {product.upper()}. Total cost: ${cost}.")
    else:
        print("Product not found. Please, select a new product.")
        select_product()

    return data.menu[product]


def insert_coins():
    coins = ", ".join(data.coins)
    print(f"Please insert coins. Accepted: {coins}.")
    quarters = int(input("How many quarters: "))
    dimes = int(input("How many dimes: "))
    nickels = int(input("How many nickels: "))
    pennies = int(input("How many pennies: "))

    money = 0
    money += quarters * data.coins["Quarter"]
    money += dimes * data.coins["Dime"]
    money += nickels * data.coins["Nickel"]
    money += pennies * data.coins["Penny"]

    return round(money, 2)


def accept_order():
    product = select_product()
    money = insert_coins()
    
    if money < product["cost"]:
        total_money = 0
        print("Sorry that's not enough money. Money refund.")
    else:
        extra = money - product["cost"]
        total_money += product["cost"]
        print(f"Here is ${extra} in change.")


def start_machine():
    total_money = 0
    
    resource_are_enough = False

    while resource_are_enough:
        accept_order()
    
    
start_machine()