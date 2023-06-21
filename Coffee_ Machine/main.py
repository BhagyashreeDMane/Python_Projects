from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menuob = Menu()
coffeemaker = CoffeeMaker()
moneymachine = MoneyMachine()


MACHINE_ON = True
while MACHINE_ON == True:
    choice = input(f"What would you like? {menuob.get_items()}")
    if choice == "off":
        MACHINE_ON = False
    elif choice == "report":
        coffeemaker.report()
        moneymachine.report()
    else:
        drink = menuob.find_drink(choice)
        if coffeemaker.is_resource_sufficient(drink):
            if moneymachine.make_payment(drink.cost):
                coffeemaker.make_coffee(drink)

