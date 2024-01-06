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
    "money": 0
}


def coffee_mach():
    cont = True
    customer = True
    while customer:
        inp = input("What would you like? (espresso/latte/cappuccino) ")
        if inp == 'off':
            return
        if inp == 'report':
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${resources['money']:.2f}".format(resources['money']))
        for i in MENU:
            if inp == i:
                for j in MENU[i]["ingredients"]:
                    if MENU[i]["ingredients"][j] > resources[j]:
                        print(f"Sorry there is not enough {j.lower()}")
                        cont = False
                        break
                money_inserted = 0
                if cont:
                    while money_inserted < MENU[i]["cost"]:
                        coins = input("What type of coin would you like to insert? Type 'refund' to refund your "
                                      "money. (pennies/nickels/dimes/quarters) ")
                        if coins == 'refund':
                            print(f"${money_inserted} has been refunded.")
                            money_inserted = 0
                            break
                        amt = int(input("How many would you like to insert? "))
                        if coins == 'pennies':
                            money_inserted += 0.01 * amt
                        elif coins == 'nickels':
                            money_inserted += 0.05 * amt
                        elif coins == 'dimes':
                            money_inserted += 0.10 * amt
                        elif coins == 'quarters':
                            money_inserted += 0.25 * amt
                    if money_inserted >= MENU[i]["cost"]:
                        if money_inserted > MENU[i]["cost"]:
                            change = money_inserted - MENU[i]['cost']
                            print(f"Here is ${change:.2f} in change.".format(change))
                            resources["money"] += MENU[i]['cost']
                        elif money_inserted == MENU[i]["cost"]:
                            resources["money"] += money_inserted
                        for j in resources:
                            if j in MENU[i]["ingredients"]:
                                resources[j] -= MENU[i]["ingredients"][j]
                        print(f"Here is your {i}. Enjoy!")
                        break

    another = input("Would you like another drink? Type 'yes' or 'no'. ")
    if another == 'yes':
        coffee_mach()


coffee_mach()


