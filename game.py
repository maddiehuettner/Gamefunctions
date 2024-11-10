# game.py
# Maddie Huettner
# 11/03/24

"""
This is a second file that corresponds to gamefunctions, the adventure game.

It imports functions from the gamefunctions module to interact with
the user and simulate game mechanics. It includes one function docstring.

Functions:
main():
"""

from gamefunctions import print_welcome, print_shop_menu, purchase_item, new_random_monster
import random

inventory = []



# Below is the code for the function docstring display_menu.
def display_menu(current_hp: int, current_gold: int):
    """Displays the current status and menu options.
    
    Parameters:
        current_hp (int): The user's current health points.
        current_gold (int): The user's current amount of gold.

    Returns:
        None
    """
    print(f"\nCurrent HP: {current_hp}, Current Gold: {current_gold}")
    print("What would you like to do?")
    print("1) Fight Monster")
    print("2) Sleep (Restore HP for 5 Gold)")
    print("3) Shop (Purchase Items)")
    print("4) Equip Item")
    print("5) Quit")
    print("6) Quit without Saving")


# Below is the code for the function docstring get_user_choice.
def get_user_choice() -> int:
    """Validates and retrieves the user's choice from the menu.

    This function prompts the user to enter their choice and validates
    the input to ensure it is a valid option (1-5). If the input
    is invalid, the user is prompted again until a valid choice is made.
    
    Returns:
        int: The validated choice made by the user (1, 2, 3, 4, or 5).
    """
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice in [1, 2, 3, 4, 5]:
                return choice
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")



# Main function with game loop
def main():
    print("Welcome to the Adventure Game!")
    
    # Prompt to load or start new game
    choice = input("Do you want to (1) Start a new game or (2) Load a saved game? (Enter 1 or 2): ").strip()
    if choice == "2":
        game_data = load_game()  # Load the saved game if available
        if game_data:
            user_hp = game_data["user_hp"]
            user_gold = game_data["user_gold"]
            inventory = game_data["inventory"]
        else:
            # If no saved game, start a new game
            user_hp = 100
            user_gold = 50
            inventory = []
    else:
        # New game setup
        user_hp = 100
        user_gold = 50
        inventory = []

    user_power = 10
    equipped_weapon = None

    while True:
        display_menu(user_hp, user_gold)
        choice = get_user_choice()

        if choice == 1:  # Fight Monster
            user_hp = fight_monster(user_hp, user_power, equipped_weapon)
            if user_hp <= 0:
                print("Game Over!")
                break
        elif choice == 2:  # Sleep
            user_hp, user_gold = sleep(user_hp, user_gold)
        elif choice == 3:  # Shop
            user_gold = shop(user_gold)
        elif choice == 4:  # Equip Item
            equipped_weapon = equip_item()
        elif choice == 5:  # Save and Quit
            save_game(user_hp, user_gold, inventory)  # Save the game
            print("Game saved! Thanks for playing!")
            break
        elif choice == 6:  # Quit without Saving
            print("Thanks for playing!")
            break



# Below is the code for the function docstring fight_monster.
def fight_monster(user_hp: int, user_power: int, equipped_weapon: dict = None) -> int:
    """Handles the combat mechanics between the user and a random monster.

    Parameters:
        user_hp (int): The user's current health points.
        user_power (int): The user's attack power.
        equipped_weapon (dict or None): The equipped weapon item.

    Returns:
        int: The user's remaining health points after the fight.
            Returns 0 if the user is defeated.
    """
    monster = new_random_monster()
    monster_hp = monster["Health"]
    print(f"A wild {monster['Name']} appears!")

    while user_hp > 0 and monster_hp > 0:
        print(f"\nYour HP: {user_hp}, {monster['Name']} HP: {monster_hp}")
        action = input("What do you want to do? (fight/run/use transporter): ").strip().lower()
        
        if action == 'fight':
            weapon_power = equipped_weapon["maxDurability"] if equipped_weapon else 0
            user_damage = user_power + weapon_power + random.randint(0, 5)
            monster_hp -= user_damage
            print(f"You deal {user_damage} damage to the {monster['Name']}!")
            if monster_hp <= 0: return user_hp

            monster_damage = random.randint(1, monster["Power"])
            user_hp -= monster_damage
            print(f"The {monster['Name']} deals {monster_damage} damage to you!")
            if user_hp <= 0: return 0
        
        elif action == 'run':
            print("You chose to run away!")
            return user_hp
        
        elif action == 'use transporter':
            transporter = next((item for item in inventory if item["name"].lower() == "special transporter"), None)
            if transporter:
                print("You used the Special Transporter! The monster has been sent away.")
                inventory.remove(transporter)
                return user_hp
            else:
                print("You don't have a Special Transporter to use!")

    return user_hp



# Below is the code for the function docstring sleep.
def sleep(user_hp: int, gold: int) -> tuple:
    """Restores health points for a cost of gold.

    Parameters:
        user_hp (int): The user's current health points.
        gold (int): The user's current amount of gold.

    Returns:
        tuple: Updated user health points and remaining gold.
    """
    if gold >= 5:
        user_hp = min(100, user_hp + 20)
        gold -= 5
        print("You slept and restored 20 HP.")
    else:
        print("Not enough gold to sleep.")
    return user_hp, gold



# Below is the code for the function docstring shop.
def shop(user_gold: int):
    """Displays shop items and allows the user to purchase them.

    Parameters:
        user_gold (int): The user's current amount of gold.

    Returns:
        int: The updated amount of gold after purchases.
    """
    items = [
        {"name": "Sword", "type": "weapon", "maxDurability": 10, "currentDurability": 10, "cost": 15},
        {"name": "Special Transporter", "type": "misc", "cost": 30, "note": "Sends monsters away."}
    ]
    print_shop_menu(items)
    choice = input("Which item would you like to purchase? (Enter name): ").strip()
    for item in items:
        if item["name"].lower() == choice.lower() and user_gold >= item["cost"]:
            inventory.append(item)
            user_gold -= item["cost"]
            print(f"You purchased a {item['name']}!")
            return user_gold
    print("Invalid choice or not enough gold.")
    return user_gold



# Below is the code for the function docstring equip_item.
def equip_item():
    """Allows the user to equip a relevant item from their inventory.

    This function displays the available weapons in the user's inventory,
    prompts the user to select one to equip, and indicates whether the 
    item has been successfully equipped. If no weapons are available, 
    the user is informed.

    Parameters:
        None

    Returns:
        dict or None: The equipped item as a dictionary if successful, 
                      or None if no weapons are available to equip.
    """
    weapons = [item for item in inventory if item["type"] == "weapon"]
    if weapons:
        print("Choose a weapon to equip:")
        for idx, item in enumerate(weapons):
            print(f"{idx + 1}) {item['name']} (Durability: {item['currentDurability']})")
        while True:
            try:
                choice = int(input("Select the number of the item to equip: ")) - 1
                if 0 <= choice < len(weapons):
                    equipped_item = weapons[choice]
                    print(f"You have equipped the {equipped_item['name']}.")
                    return equipped_item
                else:
                    print("Invalid choice. Please select a valid weapon number.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    print("No weapons available to equip.")
    return None

