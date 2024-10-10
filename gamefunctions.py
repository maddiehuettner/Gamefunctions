#gamefunctions.py
#Maddie Huettner
#10/10/24

#This project examines functions in an adventerous way.
#Below it calls two main functions three separate time with dif inputs.

import random
random.randint(1, 6)

def purchase_item(itemPrice: float, startingMoney: float, quantityToPurchase: int = 1):
    #Calculate total cost of the desired quantity.
    totalCost = itemPrice * quantityToPurchase
    
    #Determines how many can be purchased.
    if totalCost <= startingMoney:
        quantityPurchased = quantityToPurchase
        remainingMoney = startingMoney - totalCost
    else:
        quantityPurchased = int(startingMoney // itemPrice)
        remainingMoney = startingMoney - (quantityPurchased * itemPrice)
    
    return quantityPurchased, remainingMoney

def new_random_monster():
    #Defines possible monster types with their properties.
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
    
    #Selects a random monster from the list.
    chosen_monster = random.choice(monster_types)
    
    return chosen_monster

#Below returns the outputs to the functions above(purchases).
if __name__ == "__main__":

    print("Transactions of Purchased Items:")
    # Call 1: The correct number of items and the correct change are returned
    num_purchased, leftover_money = purchase_item(1.23, 10, 3)
    print(f"Purchased: {num_purchased}, Remaining Money: ${leftover_money:.2f}")

    # Call 2: The default value of quantityToPurchase works
    num_purchased, leftover_money = purchase_item(3.41, 21.12)
    print(f"Purchased: {num_purchased}, Remaining Money: ${leftover_money:.2f}")

    # Call 3: Attempting to purchase more items that you can afford is properly limited    num_purchased, leftover_money = purchase_item(31.41, 21.12)
    num_purchased, leftover_money = purchase_item(31.41, 21.12)
    print(f"Purchased: {num_purchased}, Remaining Money: ${leftover_money:.2f}")

    # Demonstrating new_random_monster function
    print("\n\nRandom Monster Demonstrations:")

#Below returns the outputs to the functions above(monsters).
    #Call 1
    monster1 = new_random_monster()
    print(f"Name: {monster1['Name']}\n"
          f"Description: {monster1['Description']}\n"
          f"Health: {monster1['Health']}\n"
          f"Power: {monster1['Power']}\n"
          f"Money: {monster1['Money']}\n")

    #Call 2
    monster2 = new_random_monster()
    print(f"Name: {monster2['Name']}\n"
          f"Description: {monster2['Description']}\n"
          f"Health: {monster2['Health']}\n"
          f"Power: {monster2['Power']}\n"
          f"Money: {monster2['Money']}\n")

    #Call 3
    monster3 = new_random_monster()
    print(f"Name: {monster3['Name']}\n"
          f"Description: {monster3['Description']}\n"
          f"Health: {monster3['Health']}\n"
          f"Power: {monster3['Power']}\n"
          f"Money: {monster3['Money']}\n")







#Assignment 2, Documentation and Strings
import random
#Below is the code for docstring print_welcome.
def print_welcome(name: str, width: int = 20) -> None:
    """Prints a welcome message centered within a specified width.
    
    Parameters:
        name (str): The name of the user.
        width (int): The total width for centering the message. Default is 20.
    """
    welcome_message = f'Hello, {name}!'
    print(welcome_message.center(width))
#Below is the code for docstring print_shop_menu.
def print_shop_menu(item1Name: str, item1Price: float, item2Name: str, item2Price: float) -> None:
    """Prints a shop menu with items and prices formatted with borders.
    
    Parameters:
        item1Name (str): The name of the first item.
        item1Price (float): The price of the first item.
        item2Name (str): The name of the second item.
        item2Price (float): The price of the second item.
    """
#This is the code that allows the dollar sign to be directly left of the price.
    item1PriceStr = f"${item1Price:.2f}"
    item2PriceStr = f"${item2Price:.2f}"
#Below is the code in order for the border to be created.    
    border_length = 22
    print("/" + "-" * border_length + "\\")
    print(f"| {item1Name:<12}{item1PriceStr:>8} |")
    print(f"| {item2Name:<12}{item2PriceStr:>8} |")
    print("\\" + "-" * border_length + "/")
#Below is the code for docstring purchase_item.
def purchase_item(itemPrice: float, startingMoney: float, quantityToPurchase: int = 1):
    """Calculates how many items can be purchased and returns the quantity purchased and remaining money.
    
    Parameters:
        itemPrice (float): The price of a single item.
        startingMoney (float): The amount of money available to spend.
        quantityToPurchase (int): The desired quantity to purchase. Default is 1.
    
    Returns:
        tuple: A tuple containing the quantity purchased and the remaining money.
    """
    totalCost = itemPrice * quantityToPurchase
    
    if totalCost <= startingMoney:
        quantityPurchased = quantityToPurchase
        remainingMoney = startingMoney - totalCost
    else:
        quantityPurchased = int(startingMoney // itemPrice)
        remainingMoney = startingMoney - (quantityPurchased * itemPrice)
    
    return quantityPurchased, remainingMoney
#Below is the code for docstring new_random_monster.
def new_random_monster():
    """Generates a random monster with properties like name, description, health, power, and money.
    
    Returns:
        dict: A dictionary containing the properties of the chosen monster.
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

#Demonstration of functions from above.
if __name__ == "__main__":
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
    monster1 = new_random_monster()
    print(f"Name: {monster1['Name']}\n"
          f"Description: {monster1['Description']}\n"
          f"Health: {monster1['Health']}\n"
          f"Power: {monster1['Power']}\n"
          f"Money: {monster1['Money']}\n")
    
    monster2 = new_random_monster()
    print(f"Name: {monster2['Name']}\n"
          f"Description: {monster2['Description']}\n"
          f"Health: {monster2['Health']}\n"
          f"Power: {monster2['Power']}\n"
          f"Money: {monster2['Money']}\n")
    
    monster3 = new_random_monster()
    print(f"Name: {monster3['Name']}\n"
          f"Description: {monster3['Description']}\n"
          f"Health: {monster3['Health']}\n"
          f"Power: {monster3['Power']}\n"
          f"Money: {monster3['Money']}\n")
