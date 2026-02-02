from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

machine_on = True

while machine_on:
    choice = input(f"What would you like? ({menu.get_items()}):").lower()
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice in menu.get_items():
        order = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(order):
            if money_machine.make_payment(order.cost):
                coffee_maker.make_coffee(order)
    elif choice == "off":
        machine_on = False








