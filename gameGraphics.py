# game.py
# Maddie Huettner
# 11/13/24

"""
This is a third file that corresponds to gamefunctions, the adventure game.

It imports functions from the gamefunctions and the game module to interact with
the user and simulate game mechanics.

Functions:
main():
"""

import pygame
import random
from gamefunctions import print_shop_menu, purchase_item, new_random_monster
from game import shop

# Initialize pygame
pygame.init()

# Game settings
WIDTH, HEIGHT = 320, 320  # 10x10 grid of 32x32 squares
GRID_SIZE = 10
SQUARE_SIZE = 32
FPS = 30
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Interactive Game")

# Initial positions
player_x, player_y = 0, 0
player_rect = pygame.Rect(player_x * SQUARE_SIZE, player_y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)

# Shop and encounter locations
shop_location = (5, 5)  # Example shop location at (5, 5)
encounter_location = (7, 7)  # Example random encounter location at (7, 7)

# Inventory and money
user_gold = 50

# Font for displaying text
font = pygame.font.SysFont('Arial', 16)

def draw_grid():
    for x in range(0, WIDTH, SQUARE_SIZE):
        for y in range(0, HEIGHT, SQUARE_SIZE):
            pygame.draw.rect(screen, WHITE, pygame.Rect(x, y, SQUARE_SIZE, SQUARE_SIZE), 1)

def display_message(text):
    text_surface = font.render(text, True, BLACK)
    screen.blit(text_surface, (10, HEIGHT - 30))

def game_loop():
    global player_x, player_y, player_rect, user_gold
    clock = pygame.time.Clock()
    
    running = True
    while running:
        screen.fill((0, 0, 0))  # Clear screen
        draw_grid()

        # Draw player
        pygame.draw.rect(screen, (0, 0, 255), player_rect)

        # Draw shop and encounter locations
        pygame.draw.circle(screen, GREEN, (shop_location[0] * SQUARE_SIZE + 16, shop_location[1] * SQUARE_SIZE + 16), 10)
        pygame.draw.circle(screen, RED, (encounter_location[0] * SQUARE_SIZE + 16, encounter_location[1] * SQUARE_SIZE + 16), 10)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if player_y > 0:
                        player_y -= 1
                elif event.key == pygame.K_DOWN:
                    if player_y < GRID_SIZE - 1:
                        player_y += 1
                elif event.key == pygame.K_LEFT:
                    if player_x > 0:
                        player_x -= 1
                elif event.key == pygame.K_RIGHT:
                    if player_x < GRID_SIZE - 1:
                        player_x += 1
                elif event.key == pygame.K_q:
                    running = False  # Quit the game

        # Update player position
        player_rect.topleft = (player_x * SQUARE_SIZE, player_y * SQUARE_SIZE)

        # Check for interaction with shop
        if (player_x, player_y) == shop_location:
            display_message("You've reached the shop!")
            # Show shop menu and interact (you can customize the interaction here)
            items = [
                {"name": "Sword", "cost": 15},
                {"name": "Special Transporter", "cost": 30}
            ]
            print_shop_menu(items)
            user_gold = shop(user_gold)
            display_message(f"Gold: {user_gold}")

        # Check for random encounter
        if (player_x, player_y) == encounter_location:
            display_message("A wild monster appears!")
            monster = new_random_monster()
            display_message(f"Name: {monster['Name']}\nHealth: {monster['Health']}")
            # You can add further combat interaction here

        pygame.display.update()  # Update the screen
        clock.tick(FPS)

    pygame.quit()


# Run the game
if __name__ == "__main__":
    game_loop()

