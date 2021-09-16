from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffe_maker2000 = CoffeeMaker()
menu = Menu()

on = True

while on:
    options = menu.get_items()
    choice = input(f"What would you like to drink? Choose from {options} ")
    if choice == "off":
        on = False
    elif choice == "report":
        coffe_maker2000.report()
        money_machine.report()
    else:
        order = menu.find_drink(choice)
        if coffe_maker2000.is_resource_sufficient(order):
            if money_machine.make_payment(order.cost):
                coffe_maker2000.make_coffee(order)