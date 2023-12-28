import os
import art
import data


def select_product():
    os.system("cls")
    print(art.logo)

    products = "/".join(available_products())
    product = input(f"What would you like? ({products}): ").lower()

    if product in data.menu:
        cost = data.menu[product]["cost"]
        print(f"You have selected: {product.upper()}. Total cost: ${cost}.")
    elif product == "off":
        return None
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


def accept_order(total_money):
    product = select_product()

    if product == "off":
        return
    else:
        money = insert_coins()

        if money < product["cost"]:
            total_money = 0
            print("Sorry that's not enough money. Money refund.")
        else:
            extra = round(money - product["cost"], 2)
            total_money += product["cost"]
            print(f"Here is ${extra} in change.")

    return total_money


def available_products():
    available_products = []

    for product in data.menu:
        enough_resources = True

        ingredients = data.menu[product]["ingredients"]

        for ingredient in ingredients:
            if ingredients[ingredient] > data.resources[ingredient]:
                enough_resources = False
                break

        if enough_resources:
            available_products.append(product)

    return available_products


def print_resources():
    for resource in data.resources:
        print(f"{resource.capitalize()}: {data.resources[resource]}")


def start_machine():
    total_money = 0

    products = available_products()

    if len(available_products()) == 0:
        print("No enough resources left. Please fill the machine.")
        print_resources()

    # while len(available_products()) > 0:
    #     total_money += accept_order(total_money)

    # print("No enough resources left.")
    # print_resources()


start_machine()
