#! /usr/bin/env python3

def coffee():
    selection = 'on'
    current_resources = resources
    current_money = 0
    while selection != 'off':
        selection = input('What Would You Like? (espresso/latte/cappuccino): ')
        if selection == 'report':
            print('Water: ' + str(current_resources.get('water')) + "ml")
            print('Milk: ' + str(current_resources.get('milk')) + "ml")
            print('Coffee: ' + str(current_resources.get('coffee')) + "ml")
        else:
            result = compare(selection, current_resources)
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


def compare(drink, current_resources):
    drink = MENU[drink]["ingredients"]
    for i in drink:
        if current_resources[i] < drink[i]:
            print('Out Of Stock!')
            return 0
    else:
        return 1


def check(drink, money):
    cost = MENU[drink]["cost"]
    if cost > money:
        return 0
    elif money > cost:
        if money > cost and money != cost:
            change = money - cost
            print('Here Is Your Change: {0}'.format(str(change)))
        return 1


def coins():
    money = int()
    quarters = input("How Many Quarters:")
    money += (int(quarters) * 0.25)
    dimes = input("How Many Dimes:")
    money += (int(dimes) * 0.10)
    nickles = input('How Many Nickles:')
    money += (int(nickles) * 0.05)
    pennies = input('How Many Pennies:')
    money += (int(pennies) * 0.01)
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
coffee()

