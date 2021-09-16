MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}ml")
    print(f"Money: ${resources['money']:.2f}")


def input_coins():
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    return [quarters, dimes, nickels, pennies]


on = True

while on:
    order = input("What would you like? (espresso/latte/cappuccino) ")
    if order == 'off':
        on = False
    elif order == 'report':
        print_report()
    else:
        enough = True
        for ingredient in ["water", "milk", "coffee"]:
            if MENU[order]["ingredients"][ingredient] > resources[ingredient]:
                enough = False
                print(f"Sorry, there is not enough {ingredient}.")
                break
        if enough:
            coins = input_coins()
            cash = 0.25*coins[0] + 0.1*coins[1] + 0.05*coins[2] + 0.01*coins[3]
            if cash < MENU[order]["cost"]:
                print("Sorry, that is not enough money. Money is refunded.")
            else:
                if cash > MENU[order]["cost"]:
                    print(f"Here is your ${cash - MENU[order]['cost']:.2f} change.")
                    resources["money"] += MENU[order]["cost"]
                    for ingredient in ["water", "milk", "coffee"]:
                        resources[ingredient] -= MENU[order]["ingredients"][ingredient]
                print(f"Here is your {order}. Enjoy!")
