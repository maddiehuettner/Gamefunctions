#gamefunctions.py
#Maddie Huettner
#10/17/24

#Below is a module docstring that provides an overview of this module.
"""
This module provides functions for an interactive game.

It includes functions for welcoming the user,
displaying shop menu, purchasing items, and generating random monsters.

Functions:
1. print_welcome(name: str, width: int = 20) -> None: Displays a welcome message.
2. print_shop_menu(item1Name: str, item1Price: float, item2Name: str, item2Price: float) -> None:
Creates a shop menu with items & prices.
3. purchase_item(itemPrice: float, startingMoney: float, quantityToPurchase: int = 1):
Calculates purchases & remaining money.
4. new_random_monster(): Generates random monsters & various attributes.
"""

import random
#Below is the code for the function docstring print_welcome.
def print_welcome(name: str, width: int = 20) -> None:
    """Prints a welcome message centered within a specified width.
    
    Parameters:
        name (str): The name of the user.
        width (int): The total width for centering the message. Default is 20.

    Returns:
        None
    """
    welcome_message = f'Hello, {name}!'
    print(welcome_message.center(width))


#Below is the code for the function docstring print_shop_menu.
def print_shop_menu(item1Name: str, item1Price: float, item2Name: str, item2Price: float) -> None:
    """Prints a shop menu with items and prices formatted with borders.
    
    Parameters:
        item1Name (str): The name of the first item.
        item1Price (float): The price of the first item.
        item2Name (str): The name of the second item.
        item2Price (float): The price of the second item.

    Returns:
        None
    """
#This is the code that allows the dollar sign to be directly left of the price.
    item1PriceStr = f"${item1Price:.2f}"
    item2PriceStr = f"${item2Price:.2f}"
    border_length = 22
#Below is the code in order for the border to be created.
    print("/" + "-" * border_length + "\\")
    print(f"| {item1Name:<12}{item1PriceStr:>8} |")
    print(f"| {item2Name:<12}{item2PriceStr:>8} |")
    print("\\" + "-" * border_length + "/")


#Below is the code for the function docstring purchase_item.
def purchase_item(itemPrice: float, startingMoney: float, quantityToPurchase: int = 1) -> tuple:
    """Calculates how many items can be purchased and returns the quantity 
    purchased and remaining money.
    
    Parameters:
        itemPrice (float): The price of a single item.
        startingMoney (float): The amount of money available to spend.
        quantityToPurchase (int): The desired quantity to purchase. Default is 1.
    
    Returns:
        Tuple: A tuple containing the quantity purchased and the remaining money.
    """
    totalCost = itemPrice * quantityToPurchase
    
    if totalCost <= startingMoney:
        quantityPurchased = quantityToPurchase
        remainingMoney = startingMoney - totalCost
    else:
        quantityPurchased = int(startingMoney // itemPrice)
        remainingMoney = startingMoney - (quantityPurchased * itemPrice)
    
    return quantityPurchased, remainingMoney


#Below is the code for the function docstring new_random_monster.
def new_random_monster() -> dict:
    """Generates a random monster with various properties such as name, description, 
    health, power, and money.
    
    Returns:
        Dict: A dictionary containing the properties of the chosen monster.
    """
    monster_types = [
        {
            "Name": "Goblin",
            "Description": "A small, green creature that loves to steal.",
            "Health": random.randint(15, 25),
            "Power": random.randint(5, 10),
            "Money": random.randint(1, 5)
        },
        {
            "Name": "Troll",
            "Description": "A large, brutish creature known for its strength.",
            "Health": random.randint(25, 40),
            "Power": random.randint(10, 15),
            "Money": random.randint(5, 10)
        },
        {
            "Name": "Dragon",
            "Description": "A fierce beast that breathes fire.",
            "Health": random.randint(40, 60),
            "Power": random.randint(15, 25),
            "Money": random.randint(10, 20)
        }
    ]
    
    chosen_monster = random.choice(monster_types)
    
    return chosen_monster


#Below is the code for the function docstring test_function.
def test_functions():
    """This is the function that tests the module functions from above.

    Parameters:
        print(): Prints the code that is being called from above.

    Returns:
    """
    print("Welcome Messages:")
    print_welcome("Jeff")
    print_welcome("Maddie")
    print_welcome("Matthias")

    print("\nShop Menus:")
    print_shop_menu("Berries", 31, "Milk", 1.234)
    print_shop_menu("Egg", 0.23, "Bag of Oats", 12.34)
    print_shop_menu("Banana", 0.99, "Apple Juice", 3.5)

    print("\nTransactions of Purchased Items:")
    num_purchased, leftover_money = purchase_item(1.23, 10, 3)
    print(f"Purchased: {num_purchased}, Remaining Money: ${leftover_money:.2f}")
    num_purchased, leftover_money = purchase_item(3.41, 21.12)
    print(f"Purchased: {num_purchased}, Remaining Money: ${leftover_money:.2f}")
    num_purchased, leftover_money = purchase_item(31.41, 21.12)
    print(f"Purchased: {num_purchased}, Remaining Money: ${leftover_money:.2f}")

    print("\nRandom Monster Demonstrations:")
    for _ in range(3):
        monster = new_random_monster()
        print(f"Name: {monster['Name']}\n"
              f"Description: {monster['Description']}\n"
              f"Health: {monster['Health']}\n"
              f"Power: {monster['Power']}\n"
              f"Money: {monster['Money']}\n")

#Demonstration of functions from above.
if __name__ == "__main__":
    test_functions()
