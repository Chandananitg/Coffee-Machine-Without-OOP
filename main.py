from data import MENU, resources
import time
# import copy
menu = MENU
menu_opt = {1: "espresso", 2: "latte", 3: "cappuccino"}
money = 0
opt = 0
beverage = ""
resource_needed = {"water": 0, "milk": 0, "coffee": 0}
resource_remain = resources.copy()


def inpint(message):
    while True:
        try:
            n = int(input(message))
        except ValueError:
            print("Not a valid input! Please enter a valid number.")
        else:
            return n


def display_menu():
    global beverage, resource_needed, menu_opt, opt
    opt = 0
    time.sleep(2)
    print("Welcome! What would you like to have?")
    print("\n 1.Espresso :$1.50\n 2.Latte :$2.50\n 3.Cappuccino :$3.00\n  or\n 4.Display Report\n 5.Refill\n 6.Exit")
    opt = int(inpint(""))
    if 1 <= opt <= 3:
        beverage = menu_opt[opt]
        for item in resource_needed:
            resource_needed[item] = menu[beverage]["ingredients"][item]
    elif opt == 4:
        display_resources()
    elif opt == 5:
        refill()
    elif opt == 6:
        print("Goodbye! Come again.")


def display_resources():
    global resource_remain
    print(f"""Resources Remaining:\n Water={resource_remain["water"]}\n Milk={resource_remain["milk"]}\n Coffee={resource_remain["coffee"]}\n Money=${money:.2f}\n""")


def amt_pay():
    print("Please insert coins:")
    quarters = int(inpint("quarters="))
    dimes = int(inpint("dimes="))
    nickles = int(inpint("nickles="))
    pennies = int(inpint("pennies="))
    total = quarters*0.25+dimes*0.10+nickles*0.05+pennies*0.01
    return total


def is_enough_resources():
    global resource_remain, resource_needed
    for item in resource_needed:
        if resource_remain[item] < resource_needed[item]:
            print(f"Sorry, Not enough {item}. choose again.\n")
            return False
    return True


def make_coffee():
    global money, resource_remain, menu, beverage, resource_needed
    for item in resource_needed:
        resource_remain[item] -= resource_needed[item]
    money += menu[beverage]["cost"]


def transaction():
    global beverage, opt
    if is_enough_resources():
        amt_paid = amt_pay()
        balance = amt_paid - menu[beverage]["cost"]
        if balance < 0:
            print(f"Amount paid = ${amt_paid}")
            print("Amount insufficient. Money Refunded.")
        else:
            make_coffee()
            print(f"Amount paid = ${amt_paid:.2f}")
            print(f"Here's your Change:${balance:.2f}")
            print(f"Here's your {beverage} ☕. Have a nice day!😄.\n")


def refill():
    global resource_remain
    resource_remain = resources.copy()
    print("\nRefilling...\n")
    time.sleep(2)
    print("\nRefill Complete!\n")
    display_resources()


display_menu()
while opt != 6:
    if 1 <= opt <= 3:
        transaction()
    display_menu()
