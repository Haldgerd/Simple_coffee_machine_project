"""
File containing all functions needed for "coffee machine" project.
"""
import os

from pyfiglet import figlet_format
from termcolor2 import c

from data_module import MENU, resource_stash


def clear():
    """Clears current output in terminal window."""
    os.system("clear")


def output_ascii_title():
    """
    Return customized ASCII text(title) using pyfiglet and termcolor2 modules.
    :return: string, ASCII text.
    """
    ascii_title = figlet_format("The coffee machine", font="slant")
    colored_ascii_title = c(ascii_title, color="magenta")
    return colored_ascii_title


def resource_checker_function(requested_drink):  # parameter should be resource dictionary.
    missing_resources = []
    resource_stash_keys = list(resource_stash.keys())
    resource_stash_values = list(resource_stash.values())
    requested_drink_values = list(MENU[requested_drink]["ingredients"].values())

    for i in range(len(requested_drink_values)):
        if resource_stash_values[i] < requested_drink_values[i]:
            missing_resources.append(resource_stash_keys[i])

    if not missing_resources:
        return True
    else:
        for item in missing_resources:
            print(f"Sorry, there's not enough {item}.")
        return False


# def resource_modifier_function():


def resource_output_formatter():
    """Formats and outputs the resource data into more readable, cleaner form."""
    for k, v in resource_stash.items():
        if k == "money":
            print(f"{k.title()}: {v}€")
        else:
            print(f"{k.title()}: {v}ml")


def money_function(requested_drink, euro, cent1, cent2, cent3):
    """
    Counts if there's enough money given to the machine for selected coffee. Adds money to resource stash and returns
    True or False depending if money was sufficient or not.
    :param requested_drink:
    :param euro: integer
    :param cent1: float
    :param cent2: float
    :param cent3: float
    :return: True, False
    """
    money_sum = float((euro*1) + (cent1*0.50) + (cent2*0.20) + (cent3*0.10))
    coffee_price = MENU[requested_drink]["cost"]

    resource_stash["money"] += coffee_price
    if money_sum != coffee_price:
        print("Sorry not enough money. Money refunded.")
        resource_stash["money"] -= money_sum
        return False

    if money_sum > coffee_price:
        change = round(money_sum - coffee_price, 2)
        if resource_stash["money"] < change:
            resource_stash["money"] = 0
            print(f"Sorry, we don't have enough change to return.\nReturning {resource_stash['money']}€.")
        else:
            resource_stash["money"] -= change
            print(f"Here's {change}€ in change.")

    return True  # upon this function evaluation we will then either modify resource stash or not.
