# gamefunctions.py
# Maddie Huettner
# 11/10/24

# Below is a module docstring that provides an overview of this module.
"""
This module provides functions for an interactive game.

It includes functions for welcoming the user,
displaying shop menu, purchasing items, and generating random monsters.

Functions:
1. print_welcome(name: str, width: int = 20) -> None: Displays a welcome message.
2. print_shop_menu(items: list) -> None: Creates a shop menu with items & prices.
3. purchase_item(itemPrice: float, startingMoney: float, quantityToPurchase: int = 1):
Calculates purchases & remaining money.
4. new_random_monster() -> dict: Generates random monsters & various attributes.
"""

import json
import random

# Below is the code for the function docstring print_welcome.
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


# Below is the code for the function docstring print_shop_menu.
def print_shop_menu(items: list) -> None:
    """Prints a shop menu with items and prices formatted with borders.

    Parameters:
        items (list): A list of dictionaries, each representing an item with 'name' and 'cost'.

    Returns:
        None
    """
    border_length = 22
    print("/" + "-" * border_length + "\\")

    for item in items:
        item_name = item["name"]
        item_price = f"${item['cost']:.2f}"
        print(f"| {item_name:<12}{item_price:>8} |")

    print("\\" + "-" * border_length + "/")


# Below is the code for the function docstring purchase_item.
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


# Below is the code for the function docstring new_random_monster.
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


# Below is the code for the function docstring test_function.
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
    print_shop_menu([
        {"name": "Berries", "cost": 31},
        {"name": "Milk", "cost": 1.234}
    ])
    print_shop_menu([
        {"name": "Egg", "cost": 0.23},
        {"name": "Bag of Oats", "cost": 12.34}
    ])
    print_shop_menu([
        {"name": "Banana", "cost": 0.99},
        {"name": "Apple Juice", "cost": 3.5}
    ])

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


# Demonstration of functions from above.
if __name__ == "__main__":
    test_functions()

# New function to save the game state
def save_game(user_hp: int, user_gold: int, inventory: list, filename: str = "save_game.json") -> None:
    """Saves the current game state to a JSON file."""
    game_state = {
        "user_hp": user_hp,
        "user_gold": user_gold,
        "inventory": inventory
    }
    try:
        with open(filename, "w") as file:
            json.dump(game_state, file, indent=4)
        print(f"Game saved successfully to {filename}.")
    except Exception as e:
        print(f"Error saving the game: {e}")


# New function to load the game state from a JSON file
def load_game(filename: str = "save_game.json") -> dict:
    """Loads the game state from a JSON file."""
    try:
        with open(filename, "r") as file:
            game_state = json.load(file)
        print(f"Game loaded successfully from {filename}.")
        return game_state
    except FileNotFoundError:
        print("No saved game found. Starting a new game.")
        return None
    except Exception as e:
        print(f"Error loading the game: {e}")
        return None
