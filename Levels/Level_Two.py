"""
Course Number: ENGR 13300
Semester:  Fall 2024

Description:
A 10 level turn based game that increases in difficulty over time

Assignment Information:
    Assignment:     Independant project
    Team ID:        011-30
    Author:         Name, login@purdue.edu
    Date:           e.g. 11/28/2024

Contributors:
    Name, login@purdue [repeat for each]

    My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor here as well.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

import pygame
import sys
from asset_manager import get_asset_path


def run_level_two(screen):
    pygame_icon =  pygame.image.load(get_asset_path("game_icon.webp"))
    background2 =  pygame.image.load(get_asset_path("background_2.png"))
    protag_front =  pygame.image.load(get_asset_path("protag_front.png"))
    obstacle_i = pygame.image.load(get_asset_path("obstical2.jpg"))
    pygame.display.set_icon(pygame_icon)

    # Screen dimensions
    WIDTH, HEIGHT = 800, 600

    # Colors
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)

    # Clock for frame rate control
    clock = pygame.time.Clock()

    # Load background image
    background = (background2)
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))

    # Load player image
    player_image = (protag_front)
    player_image = pygame.transform.scale(player_image, (50, 50))  # Scale to fit the player size

    # Player properties
    player_width, player_height = 50, 50
    player_x, player_y = 10, 50
    player_speed = 10
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)

    # Goal area properties
    goal_width, goal_height = 100, 38
    goal_x, goal_y = 650, 470
    goal_rect = pygame.Rect(goal_x, goal_y, goal_width, goal_height)

    # Obstacles
    obstacles = [
        {"rect": pygame.Rect(530, 0, 200, 300), "image": "obstical2.jpg", "dimensions": (510, 0, 400, 470)},
        {"rect": pygame.Rect(0, 0, 500, 30), "image": "obstical2.jpg", "dimensions": (0, 0, 510, 60)},
        {"rect": pygame.Rect(0, 100, 450, 100), "image": "obstical2.jpg", "dimensions": (0, 95, 465, 135)},
        {"rect": pygame.Rect(190, 280, 400, 150), "image": "obstical2.jpg", "dimensions": (165, 265, 345, 205)},
        {"rect": pygame.Rect(0, 200, 100, 300), "image": "obstical2.jpg", "dimensions": (0, 225, 110, 350)},
        {"rect": pygame.Rect(0, 520, 500, 1000), "image": "obstical2.jpg", "dimensions": (0, 505, 1000, 100)},
    ]

    # Preload obstacle images
    for obstacle in obstacles:
        image = obstacle_i
        image = pygame.transform.scale(image, (obstacle["dimensions"][2], obstacle["dimensions"][3]))
        obstacle["picture"] = image

    # Font for the win screen
    font = pygame.font.Font(None, 74)

    # Game state
    game_state = "playing"

    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if game_state == "playing":
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                player_rect.x -= player_speed
            if keys[pygame.K_d]:
                player_rect.x += player_speed
            if keys[pygame.K_w]:
                player_rect.y -= player_speed
            if keys[pygame.K_s]:
                player_rect.y += player_speed

            if player_rect.colliderect(goal_rect):
                game_state = "win"
        
            for obstacle in obstacles:
                if player_rect.colliderect(obstacle["rect"]):
                    # Undo movement if collision happens
                    player_rect.x -= player_speed if keys[pygame.K_d] else -player_speed if keys[pygame.K_a] else 0
                    player_rect.y -= player_speed if keys[pygame.K_s] else -player_speed if keys[pygame.K_w] else 0
                    print("collided object")

        if game_state == "win":
            screen.fill((0, 0, 0))
            win_text = font.render("Level Complete!", True, (255, 192, 203))
            screen.blit(win_text, (WIDTH // 2 - win_text.get_width() // 2, HEIGHT // 2 - win_text.get_height() // 2))
            pygame.display.flip()
            pygame.time.wait(2000)
            return
        else:
            screen.blit(background, (0, 0))
            screen.blit(player_image, (player_rect.x, player_rect.y))
            pygame.draw.rect(screen, GREEN, goal_rect)

            for obstacle in obstacles:
                x, y, width, height = obstacle["dimensions"]
                screen.blit(obstacle["picture"], (x, y))

        pygame.display.flip()
        clock.tick(30)


# Initialize Pygame
pygame.init()

# Create screen object
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Level Two")

# Run the level
run_level_two(screen)
