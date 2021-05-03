#! /usr/bin/env python3

def coffee():
    selection = 'on'
    current_resources = resources
    while selection != 'off':
        selection = input('What Would You Like? (espresso/latte/cappuccino): ')
        if selection == 'report':
            print('Water: ' + str(current_resources.get('water')) + "ml")
            print('Milk: ' + str(current_resources.get('milk')) + "ml")
            print('Coffee: ' + str(current_resources.get('coffee')) + "ml")
        elif selection not in MENU:
            print('What was that?')
        else:
            result = stock(selection, current_resources)
            if result == 0:
                pass
            elif result == 1:
                print("Insert Coins!")
                result = check(selection, coins())
                if result == 0:
                    print("Not Enough Money")
                elif result == 1:
                    print('Thank You For Your Purchase, Here is Your ' + selection)
                    for i in MENU[selection]["ingredients"]:
                        current_resources[i] = current_resources[i] - MENU[selection]["ingredients"][i]


def stock(drink, current_resources):
    drink = MENU[drink]["ingredients"]
    rvalue = 0
    for i in drink:
        if current_resources[i] < drink[i]:
            print('Out Of Stock!')
            rvalue = 0
    else:
        rvalue = 1
    return rvalue


def check(drink, money):
    cost = MENU[drink]["cost"]
    rvalue = ()
    if cost > money:
        rvalue = 0
    elif money > cost:
        rvalue = 1
        if money > cost and money != cost:
            change = money - cost
            print('Here Is Your Change: ${0}'.format(str(change)))
    return rvalue


def coins():
    money = int()
    try:
        quarters = input("How Many Quarters:")
        money += (int(quarters) * 0.25)
    except ValueError:
        print('What was that?')
    try:
        dimes = input("How Many Dimes:")
        money += (int(dimes) * 0.10)
    except ValueError:
        print('What was that?')
    try:
        nickles = input('How Many Nickles:')
        money += (int(nickles) * 0.05)
    except ValueError:
        print('What was that?')
    try:
        pennies = input('How Many Pennies:')
        money += (int(pennies) * 0.01)
    except ValueError:
        print('What was that?')
    return money


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
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
}

if __name__ == "__main__":
    coffee()
