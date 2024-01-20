# from turtle import Turtle, Screen
#
# timmy = Turtle()
# my_screen = Screen()
# timmy.shape("turtle")
# timmy.color("green")
# timmy.forward(100)
# my_screen.exitonclick()


# from prettytable import PrettyTable
#
# table = PrettyTable()
# table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
# table.add_column("Type", ["Electric", "Water", "Fire"])
# table.align = "l"
# print(table)


from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

coffee_maker.report()
money_machine.report()
menu = Menu()

machine = "working"
while machine == "working":
    options = menu.get_items()
    decision = input(f"What would you like? ({options}): ")
    if decision == "off" or machine == "stop":
        break
    elif decision == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(decision)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
        machine = "working"
