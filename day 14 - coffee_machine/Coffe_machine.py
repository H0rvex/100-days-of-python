import coffee_art

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

money = 0


def check_resources():
    for ingredient in COFFEE_SELECTED["ingredients"]:
        if resources[ingredient] < COFFEE_SELECTED["ingredients"][ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    else:
        return True


def process_coins():
    inserted_coins = 0.00
    print("Please insert coins.")
    quarters = int(input("How many quarters?"))
    quarters = 0.25 * quarters
    dimes = int(input("How many dimes?"))
    dimes = 0.10 * dimes
    nickles = int(input("How many nickles?"))
    nickles = 0.05 * nickles
    pennies = int(input("How many pennies?"))
    pennies = 0.01 * pennies
    inserted_coins += quarters + dimes + nickles + pennies
    if inserted_coins >= COFFEE_SELECTED["cost"]:
        change = inserted_coins - COFFEE_SELECTED["cost"]
        global money
        money += COFFEE_SELECTED["cost"]
        print(f"Here is your change: ${round(change,2)}")
        return True
    elif inserted_coins < COFFEE_SELECTED["cost"]:
        print(f"Sorry, the inserted money is not enough. Here is your refund: ${round(inserted_coins,2)}")
        return False
    return inserted_coins



MACHINE_ON = True
COFFEE_SELECTED = {}
print(f"{coffee_art.logo}\n")
while MACHINE_ON:
    coffee_type = input("What would you like? (espresso/latte/cappuccino):").lower()
    if coffee_type in MENU:
        COFFEE_SELECTED = MENU[coffee_type]
        if check_resources():
            if process_coins():
                print(f"Here is your {coffee_type}. Enjoy! ☕")
                for res in resources:
                    resources[res] -= COFFEE_SELECTED["ingredients"].get(res,0)
    elif coffee_type == "off" or coffee_type == "exit":
        MACHINE_ON = False
    elif coffee_type == "report":
        for key in resources:
            print(f"{key}: {resources[key]}")
        print(f"money: ${round(money,2)}")
    else:
        print("Please enter a valid coffee type.")



