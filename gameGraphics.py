import sys; sys.executable
import pygame
import random
from gamefunctions import print_shop_menu, purchase_item, new_random_monster
from game import shop

pygame.init()

# Grid and square size instructions.
WIDTH, HEIGHT = 320, 320
GRID_SIZE = 10
SQUARE_SIZE = 32
FPS = 30
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Title and screen display instructions.
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Interactive Game")

# Initial positions.
player_x, player_y = 0, 0
player_rect = pygame.Rect(player_x * SQUARE_SIZE, player_y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)

# Shop and encounter locations.
shop_location = (5, 5)  
encounter_location = (7, 7) 

# Inventory and money.
user_gold = 50

# Font for displaying text.
font = pygame.font.SysFont('Arial', 16)




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


# Below is the code for the function docstring display_message:
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


# Below is the code for the function docstring game_loop.
def game_loop():
    """
    Loop that controls the game.

    Parameters:
        None

    Returns:
        None
    """
    global player_x, player_y, player_rect, user_gold
    clock = pygame.time.Clock()
    
    running = True
    while running:
        screen.fill((0, 0, 0))
        draw_grid()


        pygame.draw.rect(screen, (0, 0, 255), player_rect)


        pygame.draw.circle(screen, GREEN, (shop_location[0] * SQUARE_SIZE + 16, shop_location[1] * SQUARE_SIZE + 16), 10)
        pygame.draw.circle(screen, RED, (encounter_location[0] * SQUARE_SIZE + 16, encounter_location[1] * SQUARE_SIZE + 16), 10)


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
                    running = False  

        # Updates player position.
        player_rect.topleft = (player_x * SQUARE_SIZE, player_y * SQUARE_SIZE)

        # Interaction with shop.
        if (player_x, player_y) == shop_location:
            display_message("You've reached the shop!")

            items = [
                {"name": "Sword", "cost": 15},
                {"name": "Special Transporter", "cost": 30}
            ]
            print_shop_menu(items)
            user_gold = shop(user_gold)
            display_message(f"Gold: {user_gold}")


        if (player_x, player_y) == encounter_location:
            display_message("A wild monster appears!")
            monster = new_random_monster()
            display_message(f"Name: {monster['Name']}\nHealth: {monster['Health']}")

        pygame.display.update() 
        clock.tick(FPS)

    pygame.quit()



if __name__ == "__main__":
    game_loop()
