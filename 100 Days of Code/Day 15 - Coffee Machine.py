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
    "money": 0,
}


def res_check(coffee_type):
    global resources, machine
    if MENU[coffee_type]["ingredients"]["water"] > resources["water"]:
        print("Not enough water.")
        machine = "no resources"
    elif MENU[coffee_type]["ingredients"]["milk"] > resources["milk"]:
        print("Not enough milk.")
        machine = "no resources"
    elif MENU[coffee_type]["ingredients"]["coffee"] > resources["coffee"]:
        print("Not enough coffee.")
        machine = "no resources"
    else:
        for key in resources:
            if key == "money":
                break
            resources[key] -= MENU[coffee_type]["ingredients"][key]


def money(coffee_type):
    global resources
    quarters = float(input("Insert quarters: "))
    dimes = float(input("Insert dimes: "))
    nickels = float(input("Insert nickels: "))
    pennies = float(input("Insert pennies: "))
    total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    if total < MENU[coffee_type]["cost"]:
        print("Sorry that's not enough money. Money refunded.")
    else:
        change = total - MENU[coffee_type]["cost"]
        resources["money"] += MENU[coffee_type]["cost"]
        print(f"Here is ${round(change, 2)} dollars in change.")


# Main loop
machine = "working"
while machine == "working":
    decision = input("What would you like? (espresso/latte/cappuccino): ")
    if decision == "off" or machine == "stop":
        break
    elif decision == "report":
        print(resources)
    else:
        res_check(decision)
        if machine == "working":
            money(decision)
            print(f"Here is your {decision}, enjoy!")
        machine = "working"
