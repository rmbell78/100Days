from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

ison = True
menu = Menu()
money_man = MoneyMachine()
coffee_man = CoffeeMaker()

while ison:
    print("Welcome!")
    selection = input('What Would You Like? ' + menu.get_items() + ": ")
    if selection == 'report':
        coffee_man.report()
        money_man.report()
    else:
        item = menu.find_drink(selection)
        if item is not None:
            if coffee_man.is_resource_sufficient(item):
                if money_man.make_payment(item.cost):
                    coffee_man.make_coffee(item)