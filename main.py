"""
An attempt to simulate a simple coffee machine and it's functionality. This version is used as in depth exercise, before
writing same program using OOP later within the programming course.

The main requirements where:
1. Output a report on resources.
2. Receive user input, referring to type of coffee they want.
3. Check for sufficient resources.
4. Process coin payment. Check if transaction is successful. (refund if payment is not sufficient. )
5. Return amount of change if needed.
"""
from functions_module import clear, output_ascii_title, money_function, resource_output_formatter, \
    resource_checker_function, resource_modifier_function

# MAIN PROGRAM
off = False

print(output_ascii_title())
while not off:
    order = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()
    if order not in ["latte", "espresso", "cappuccino"]:
        if order == "off":
            break
        elif order == "report":
            resource_output_formatter()
            continue
        else:
            print("Unknown coffee request.")
            continue

    if resource_checker_function(order):
        print("Please insert coins.")
        euro_coins = int(input("How many euros: "))
        cent_50 = int(input("How many 50 cents: "))
        cent_20 = int(input("How many 20 cents: "))
        cent_10 = int(input("How many 10 cents: "))

        is_enough_money = money_function(order, euro_coins, cent_50, cent_20, cent_10)

        if not is_enough_money:
            clear()
            continue

        resource_modifier_function(order)
        print(f"Here is your {order}. Enjoy!")
        clear()
    else:
        continue

    """
    PSEUDO CODE:
        
    if off: DONE!!
        maintenance, break from loop, exit coffee machine.
    elif report:
        show report on resources
    else:
        1.check resource quantity (if sufficient or not) when user asks for drink. If there's not enough let user know.
        2. if resources are OK., ask for coins -PAYMENT.
        3. check if money given is sufficient in amount. ADD profit to machine registry if so, else let user know they 
        didn't give enough money.
        4. if all ok, give drink. (behind scenes: take away resources, add money)
    """

print("\nMaintenance time! Turning off.")

