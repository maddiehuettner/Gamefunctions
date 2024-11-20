# gameGraphics.py
# Maddie Huettner
# 11/20/24

"""
This is a third file that corresponds to gamefunctions, the adventure game.

It creates an interactive game.

Functions:
main():
"""

import sys
import pygame
import random
from gamefunctions import print_shop_menu, purchase_item, new_random_monster
from game import fight_monster  # Import the fight_monster function from game.py

pygame.init()

# Grid and square size instructions.
WIDTH, HEIGHT = 320, 320
GRID_SIZE = 10
SQUARE_SIZE = 32
FPS = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Title and screen display instructions.
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Interactive Game")

# Initial positions.
player_x, player_y = 0, 0
player_rect = pygame.Rect(player_x * SQUARE_SIZE, player_y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)

# Inventory and money.
user_gold = 50

# Font instructions.
font = pygame.font.SysFont('Arial', 16)


shop_visited = False

# Below is the code for function docstring draw_grid.
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

# Below is the code for function docstring display_message.
def display_message(text):
    """
    Displays a text message on the screen.

    Parameters:
        text (str): The message that will be displayed.

    Returns:
        None
    """
    text_surface = font.render(text, True, BLACK)
    screen.blit(text_surface, (10, HEIGHT - 30))

# Below is the code for the Monster class.
class Monster:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x * SQUARE_SIZE, self.y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)

    def move(self):
        """Move the monster randomly in one of the four cardinal directions."""
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

# Below is the code for function docstring game_loop.
def game_loop():
    """
    Loop that controls the game.

    Parameters:
        None

    Returns:
        None
    """
    global player_x, player_y, player_rect, user_gold, shop_visited
    clock = pygame.time.Clock()


    monsters = [Monster(random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))]


    encountered = False

    running = True
    while running:
        screen.fill((0, 0, 0))
        draw_grid()

        
        pygame.draw.rect(screen, (0, 0, 255), player_rect)

        
        for monster in monsters:
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

        # Code so that monsters only move if the player moves.
        if player_moved:
            for monster in monsters:
                monster.move()

        # Checking if player and monster are in the same position.
        for monster in monsters:
            if player_x == monster.x and player_y == monster.y:
                if not encountered:  
                    print("Encounter! The monster is here!")
                    # Offer the player a choice to fight or run
                    choice = input("Do you want to (1) Fight or (2) Run? ").strip()
                    if choice == "1":
                        # Fight function called  from game.py.
                        user_hp = 100  
                        user_power = 10 
                        user_hp = fight_monster(user_hp, user_power)  
                        if user_hp <= 0:
                            print("You have been defeated!")
                            running = False
                        else:
                            # Clears the defeated monster and spawn two new ones.
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
