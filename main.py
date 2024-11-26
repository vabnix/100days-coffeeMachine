from random import choice

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

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            is_enough = False
    return is_enough

def process_coin():
    """Return the total calculated dollar from the coins inserted"""
    total = 0
    print("Please insert coin:")
    total += int(input("How many quaters?:")) * 0.25
    total += int(input("How many dimes?:")) * 0.1
    total += int(input("How many nickles?:")) * 0.05
    total += int(input("How many pennies?:")) * 0.01
    return total

def is_transaction_successful(money_recieved, drink_cost):
    """Check if the inserted amount is sufficient to buy the coffee"""
    if money_recieved >= drink_cost:
        change = round((money_recieved - drink_cost),2)
        print(f"Here is your 💵${change} change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough to buy the drink")
        return False
    
def make_drink(drink_name, order_ingredients):
    """Make the coffee and order the required ingredients from resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️Enjoy!😊")


is_on = True

while is_on:
    choice = input("What would you like ? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        print(drink)
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coin()
            if is_transaction_successful(payment, drink["cost"]):
                make_drink(choice, drink["ingredients"])

