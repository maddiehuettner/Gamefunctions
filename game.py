#game.py
#Maddie Huettner
#11/03/24

#Below is a module docstring that provides an overview of this module.
"""
This is a second file that corresponds to gamefunctions, the adventure game.

It imports functions from the gamefunctions module to interact with
the user and simulate game mechanics. It includes one function docstring.

Functions:
main():
"""

from gamefunctions import print_welcome, print_shop_menu, purchase_item, new_random_monster
import random





#Below is the code for the function docstring display_menu.
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
    print("3) Quit")






#Below is the code for the function docstring get_user_choice.
def get_user_choice() -> int:
    """Validates and retrieves the user's choice from the menu.
    
    This function prompts the user to enter their choice and validates
    the input to ensure it is a valid option (1, 2, or 3). If the input
    is invalid, the user is prompted again until a valid choice is made.

    Returns:
        int: The validated choice made by the user (1, 2, or 3).
    """
    while True:
        try:
            choice = int(input("Enter your choice: "))
            if choice in [1, 2, 3]:
                return choice
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")





#Below is the code for the function docstring fight_monster.
def fight_monster(user_hp: int, user_power: int) -> int:
    """Handles the combat mechanics between the user and a random monster.

    Parameters:
        user_hp (int): The user's current health points.
        user_power (int): The user's attack power.

    Returns:
        int: The user's remaining health points after the fight.
            Returns 0 if the user is defeated.
    """
    monster = new_random_monster()
    monster_hp = monster["Health"]
    print(f"A wild {monster['Name']} appears!")

    while user_hp > 0 and monster_hp > 0:
            #User attacks the monster
            user_damage = user_power + random.randint(0, 5)
            monster_hp -= user_damage
            print(f"You deal {user_damage} damage to the {monster['Name']}!")

            if monster_hp <= 0:
                print(f"You defeated the {monster['Name']}!")
                return user_hp

            # Monster attacks the user
            monster_damage = random.randint(1, monster["Power"]) 
            user_hp -= monster_damage
            print(f"The {monster['Name']} deals {monster_damage} damage to you!")

            if user_hp <= 0:
                print("You have been defeated!")
                return 0




#Below is the code for the function docstring sleep.
def sleep(user_hp: int, gold: int) -> tuple:
    """Restores health points for a cost of gold.

    Parameters:
        user_hp (int): The user's current health points.
        gold (int): The user's current amount of gold.

    Returns:
        tuple: A tuple containing the updated user health points and remaining gold.
    """
    if gold >= 5:
        user_hp = min(100, user_hp + 20)
        gold -= 5
        print("You slept and restored 20 HP.")
    else:
        print("Not enough gold to sleep.")
    return user_hp, gold





#Below is the code for the function docstring main().
def main():
    name = input("Enter your name: ")
    print_welcome(name)

    user_hp = 100
    user_gold = 50  # Starting gold
    user_power = 10  # Starting power

    while True:
        display_menu(user_hp, user_gold)
        choice = get_user_choice()

        if choice == 1:  # Fight Monster
            user_hp = fight_monster(user_hp, user_power)
            if user_hp <= 0:
                print("Game Over!")
                break
        elif choice == 2:  # Sleep
            user_hp, user_gold = sleep(user_hp, user_gold)
        elif choice == 3:  # Quit
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
