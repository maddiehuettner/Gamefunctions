# gameGraphics.py
# Maddie Huettner
# 12/04/24

"""
This is a third file that corresponds to gamefunctions, the adventure game.

It creates an interactive game that takes place on a square grid.

Functions:
main():
"""

import sys
import pygame
import random
from gamefunctions import print_shop_menu, purchase_item, new_random_monster
from game import fight_monster 

pygame.init()

# Grid and squares instructions.
WIDTH, HEIGHT = 320, 320
GRID_SIZE = 10
SQUARE_SIZE = 32
FPS = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Title and screen display instructions.
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Interactive Game")

# Initial positions instructions.
player_x, player_y = 0, 0
player_rect = pygame.Rect(player_x * SQUARE_SIZE, player_y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)

user_gold = 50

# Font instructions.
font = pygame.font.SysFont('Arial', 16)

shop_visited = False

# Below is the code for the function docstring load_image.
def load_image(filename, fallback_color, description):
    """
    Loads an image from a file.

    Parameters:
        filename (str): The path to the image file to load.
        fallback_color (str): The fallback color to use if the image cannot be loaded (blue or red).
        description (str): A description of the image being loaded (player or monster).

    Returns:
        pygame.Surface: The loaded and scaled image, or None if the file is not found or cannot be loaded.
    """
    try:
        image = pygame.image.load(filename).convert_alpha()
        return pygame.transform.scale(image, (SQUARE_SIZE, SQUARE_SIZE))
    except Exception as e:
        print(f"Error: {description} image not found. Defaulting to {fallback_color} square. ({e})")
        return None

player_image = load_image("person.png", "blue", "Player")
monster_image = load_image("monster.png", "red", "Monster")

# Below is the code for the function docstring draw_grid.
def draw_grid():
    """
    Draws a grid of squares on the screen.

    Parameters:
        None

    Returns:
        None
    """
    for x in range(0, WIDTH, SQUARE_SIZE):
        for y in range(0, HEIGHT, SQUARE_SIZE):
            pygame.draw.rect(screen, WHITE, pygame.Rect(x, y, SQUARE_SIZE, SQUARE_SIZE), 1)

# Below is the code for the function docstring display_message.
def display_message(text):
    """
    Displays a text message on the screen.

     Parameters:
        text (str): The message to display.

    Returns:
        None
    """
    text_surface = font.render(text, True, BLACK)
    screen.blit(text_surface, (10, HEIGHT - 30))

class Monster:
    # Below is the code for the function docstring __init__(self, x, y).
    def __init__(self, x, y):
        """
        Initializes a Monster object with its position and rectangular boundary.
    
        Parameters:
            x (int): The initial x-coordinate of the monster on the grid.
            y (int): The initial y-coordinate of the monster on the grid.
    
        Attributes:
            x (int): The current x-coordinate of the monster on the grid.
            y (int): The current y-coordinate of the monster on the grid.
            rect (pygame.Rect): The rectangle representing the monster's position and size on the screen.
    
        Returns:
            None
        """
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x * SQUARE_SIZE, self.y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)

    # Below is the code for the function docstring move(self).
    def move(self):
        """
        Move the monster randomly in one of the four cardinal directions.

        The movement is restricted within the bounds of the grid, ensuring that the monster 
        does not move outside of the defined grid area.

        Returns:
            None
        """
        direction = random.choice(['up', 'down', 'left', 'right'])

        if direction == 'up' and self.y > 0:
            self.y -= 1
        elif direction == 'down' and self.y < GRID_SIZE - 1:
            self.y += 1
        elif direction == 'left' and self.x > 0:
            self.x -= 1
        elif direction == 'right' and self.x < GRID_SIZE - 1:
            self.x += 1
        
        self.rect.topleft = (self.x * SQUARE_SIZE, self.y * SQUARE_SIZE)

    
# Below is the code for the function docstring game_loop.
def game_loop():
    """
    Loop that controls the game. The loop continuously updates the game state 
    and renders the game screen until the player quits or is defeated.

    Parameters:
        None

    Returns:
        None
    """
    global player_x, player_y, player_rect, user_gold, shop_visited
    clock = pygame.time.Clock()

    monsters = [Monster(random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))]
    encountered = False

    # Initialize player stats once at the beginning of the game.
    user_hp = 100
    user_power = 10

    running = True
    while running:
        screen.fill((0, 0, 0))
        draw_grid()

        # Draw the player using the image or a default blue rectangle
        if player_image:
            screen.blit(player_image, player_rect.topleft)
        else:
            pygame.draw.rect(screen, (0, 0, 255), player_rect)

        # Draw monsters using the image or a default red rectangle
        for monster in monsters:
            if monster_image:
                screen.blit(monster_image, monster.rect.topleft)
            else:
                pygame.draw.rect(screen, (255, 0, 0), monster.rect)

        player_moved = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if player_y > 0:
                        player_y -= 1
                        player_moved = True
                elif event.key == pygame.K_DOWN:
                    if player_y < GRID_SIZE - 1:
                        player_y += 1
                        player_moved = True
                elif event.key == pygame.K_LEFT:
                    if player_x > 0:
                        player_x -= 1
                        player_moved = True
                elif event.key == pygame.K_RIGHT:
                    if player_x < GRID_SIZE - 1:
                        player_x += 1
                        player_moved = True
                elif event.key == pygame.K_q:
                    running = False  

        player_rect.topleft = (player_x * SQUARE_SIZE, player_y * SQUARE_SIZE)

        # Monsters move if the player moves.
        if player_moved:
            for monster in monsters:
                monster.move()

        # Checking if player and monster are in the same position.
        for monster in monsters:
            if player_x == monster.x and player_y == monster.y:
                if not encountered:  
                    print("Encounter! The monster is here!")
                    choice = input("Do you want to (1) Fight or (2) Run? ").strip()
                    if choice == "1":
                        user_hp = fight_monster(user_hp, user_power)  
                        if user_hp <= 0:
                            print("You have been defeated!")
                            running = False
                        else:
                            monsters.remove(monster)  
                            monsters.append(Monster(random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)))
                            monsters.append(Monster(random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1)))
                    elif choice == "2":
                        print("You chose to run away!")
                        encountered = False
                        continue  
                    else:
                        print("Invalid choice, you missed your chance to act!")
                        encountered = False
                encountered = True
        else:
            encountered = False 

        pygame.display.update() 
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    game_loop()
