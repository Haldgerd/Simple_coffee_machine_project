"""
File containing main variables/data on which functionality of the program is based.
Contains "offer or menu" and state of resources.
"""


MENU = {  # contains nested dictionary. Each separate dictionary has two keys.
    "espresso": {  # espresso as main key
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "water": 400,
    "milk": 300,
    "coffee": 100,
    "money": 0,
}
# copy of original resources in case of restoring to default values.
resource_stash = resources


coffee_price = MENU["espresso"]["cost"]
print(coffee_price)

print(1 + 2*0.50 + 0.20)
