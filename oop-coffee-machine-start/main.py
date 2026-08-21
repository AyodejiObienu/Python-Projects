from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

myCoffeMaker = CoffeeMaker()
myMenu = Menu()
myMoneyMachine = MoneyMachine()

is_on = True
while is_on:
    
    items = myMenu.get_items()
    user_input = input(f"What would you like? ({items})")

    if user_input == "off":
        is_on = False

    elif user_input == "report":
        myCoffeMaker.report()
        myMoneyMachine.report()

    else:
        latteObject = myMenu.find_drink(user_input)       
        
        if myCoffeMaker.is_resource_sufficient(latteObject) and myMoneyMachine.make_payment(latteObject.cost):
            myCoffeMaker.make_coffee(latteObject)
