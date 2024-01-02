import os
import art

from module.menu import Menu, MenuItem
from module.coffee_maker import CoffeeMaker
from module.money_machine import MoneyMachine


def start_machine():
    stop_machine = False

    os.system("cls")
    print(art.logo)

    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    while not stop_machine:
        money_machine.report()
        print(f"Resources: {coffee_maker.resources}")

        choice = input(f"What would you like? ({menu.get_items()}): ").lower()

        if choice == "off":
            print("Machine turned off.")
            stop_machine = True
        else:
            menu_item = menu.find_drink(choice)

            if menu_item is None:
                print("")
            else:
                if not coffee_maker.is_resource_sufficient(menu_item):
                    print("")
                else:
                    if not money_machine.make_payment(menu_item.cost):
                        print("")
                    else:
                        coffee_maker.make_coffee(menu_item)
                        print("")


start_machine()
