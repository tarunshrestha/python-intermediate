from menu import MENU

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0


def main():
    canplay = True
    while canplay:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if choice == "off":
            print("Machine turning off.....")
            canplay = False
        elif choice == "report":
            print(f"Water : {resources['water']}ml")
            print(f"Milk : {resources['milk']}ml")
            print(f"Coffee : {resources['coffee']}g")
            print(f"Money : ${profit}")
        else:
            if choice == "espresso" or choice == "latte" or choice == "cappuccino":
                drink = MENU[choice]
                if is_resource_sufficient(drink["ingredients"]):
                    payment = process_coins()
                    if transaction(payment, drink["cost"]):
                        make_coffee(choice, drink["ingredients"])

            else:
                print("Invalid choice.")


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry not enough {item}.")
            return False
    return True


def process_coins():
    print("Please insert coins.")
    total = int(input("How many quarters?")) * 0.25
    total += int(input("How many dimes?")) * 0.1
    total += int(input("How many nickles?")) * 0.05
    total += int(input("How many pennies?")) * 0.01
    return total


def transaction(money_got , drink_cost):
    """Return True when the payment is accepted or False"""
    if money_got >= drink_cost:
        change = round(money_got - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(name, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {name}.")


main()