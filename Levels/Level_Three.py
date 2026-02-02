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

def run_level_three():
    pygame_icon = pygame.image.load(get_asset_path('game_icon.webp'))
    pygame.display.set_icon(pygame_icon)

    # Initialize Pygame
    pygame.init()

    # Screen dimensions
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Level Three")

    # Colors
    WHITE = (255, 192, 203)
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)

    # Clock for frame rate control
    clock = pygame.time.Clock()

    # Load assets for the first segment
    background = pygame.image.load(get_asset_path("background_2.png"))
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    player_image = pygame.image.load(get_asset_path("protag_front.png"))
    player_image = pygame.transform.scale(player_image, (50, 50))

    # Load assets for turn-based mode
    turn_based_background = pygame.image.load(get_asset_path("background_turn.jpg"))
    turn_based_background = pygame.transform.scale(turn_based_background, (WIDTH, HEIGHT))
    player_idle_image = pygame.image.load(get_asset_path("protag_side.png"))
    player_idle_image = pygame.transform.scale(player_idle_image, (100, 100))
    player_attack_image = pygame.image.load(get_asset_path("Hero_attack_1.png"))
    player_attack_image = pygame.transform.scale(player_attack_image, (100, 100))
    opponent_idle_image = pygame.image.load(get_asset_path("The_Creature.png"))
    opponent_idle_image = pygame.transform.scale(opponent_idle_image, (300, 300))
    opponent_attack_image = pygame.image.load(get_asset_path("The_Creature_attack.png") )
    opponent_attack_image = pygame.transform.scale(opponent_attack_image, (300, 300))
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
        image = pygame.image.load(get_asset_path("obstical2.jpg"))
        image = pygame.transform.scale(image, (obstacle["dimensions"][2], obstacle["dimensions"][3]))
        obstacle["picture"] = image

    # Font for text
    font = pygame.font.Font(None, 74)
    small_font = pygame.font.Font(None, 40)

    # Game state
    game_state = "playing"  # "playing", "turn_based", "win", "lose"
    turn = "player"  # "player" or "opponent"

    # Turn-based properties
    player_health = 100
    opponent_health = 100
    player_name = "Hero"  # Name for the player's character
    opponent_name = "Villain"  # Name for the opponent
    player_health = 150
    opponent_health = 100
    sprite_y_offset = 150
    attack_duration = 650
    attack_opponent_duration = 650
    player_attacking = False
    opponent_attacking = False
    attack_start_time = 0
    # Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if game_state == "playing":
            # Handle player movement
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                player_rect.x -= player_speed
            if keys[pygame.K_d]:
                player_rect.x += player_speed
            if keys[pygame.K_w]:
                player_rect.y -= player_speed
            if keys[pygame.K_s]:
                player_rect.y += player_speed

            # Check collision with obstacles
            for obstacle in obstacles:
                if player_rect.colliderect(obstacle["rect"]):
                    # Undo movement if collision happens
                    player_rect.x -= player_speed if keys[pygame.K_d] else -player_speed if keys[pygame.K_a] else 0
                    player_rect.y -= player_speed if keys[pygame.K_s] else -player_speed if keys[pygame.K_w] else 0

            # Check for reaching the goal
            if player_rect.colliderect(goal_rect):
                game_state = "turn_based"  # Transition to turn-based mode


        elif game_state == "turn_based":
            # Clear assets and set up the turn-based mode
            screen.fill(WHITE)
            screen.blit(turn_based_background, (0, 0))

            # Display sprites
            screen.blit(player_idle_image, (100, HEIGHT // 2 - player_idle_image.get_height() // 2 + sprite_y_offset))
            screen.blit(opponent_idle_image, (WIDTH - 220, HEIGHT // 2 - opponent_idle_image.get_height() // 2 + sprite_y_offset))
            #player and opponent names
            player_name_text = small_font.render("Hero", True, BLACK)
            screen.blit(player_name_text, (50, 20))  # Above player health bar
            opponent_name_text = small_font.render("The Creature", True, BLACK)
            screen.blit(opponent_name_text, (WIDTH - 250, 20))  # Above opponent health bar

            # Display health bars
            pygame.draw.rect(screen, (255, 0, 0), (50, 50, player_health * 2, 20))  # Player health bar
            pygame.draw.rect(screen, (255, 0, 0), (WIDTH - 250, 50, opponent_health * 2, 20))  # Opponent health bar
            
            if player_attacking and pygame.time.get_ticks() - attack_start_time < attack_duration:
             screen.blit(player_attack_image, (100, HEIGHT // 2 - player_idle_image.get_height() // 2 + sprite_y_offset))
            else:
             player_attacking = False
             screen.blit(player_idle_image, (100, HEIGHT // 2 - player_idle_image.get_height() // 2 + sprite_y_offset))

            if opponent_attacking and pygame.time.get_ticks() - attack_start_time < attack_opponent_duration:
             screen.blit(opponent_attack_image, (WIDTH - 220, HEIGHT // 2 - opponent_idle_image.get_height() // 2 + sprite_y_offset))
            else:
             opponent_attacking = False
             screen.blit(opponent_idle_image, (WIDTH - 220, HEIGHT // 2 - opponent_idle_image.get_height() // 2 + sprite_y_offset))

            # Turn-based actions
            if turn == "player":
                text = small_font.render("Player's Turn: Press Space to Attack", True, BLACK)
                screen.blit(text, (50, HEIGHT - 50))
                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE]:
                    opponent_health -= 10
                    player_attacking = True
                    attack_start_time = pygame.time.get_ticks()
                    turn = "opponent"
            elif turn == "opponent":
                text = small_font.render("Opponent's Turn: Wait...", True, BLACK)
                screen.blit(text, (50, HEIGHT - 50))
                pygame.time.wait(2000)  # Simulate opponent's action delay
                player_health -= 10
                opponent_attacking = True
                attack_start_time = pygame.time.get_ticks()
                if opponent_attacking:
        # Check if the attack animation duration has elapsed
                    if pygame.time.get_ticks() - attack_start_time < attack_opponent_duration:
                    # Display attack sprite
                     screen.blit(opponent_attack_image, (WIDTH - 220, HEIGHT // 2 - opponent_attack_image.get_height() // 2 + sprite_y_offset))
                    else:
                    # Reset after the attack animation ends
                     opponent_attacking = False
                     screen.blit(opponent_idle_image, (WIDTH - 220, HEIGHT // 2 - opponent_idle_image.get_height() // 2 + sprite_y_offset))
                else:
                    # Display idle sprite if not attacking
                    screen.blit(opponent_idle_image, (WIDTH - 220, HEIGHT // 2 - opponent_idle_image.get_height() // 2 + sprite_y_offset))
                turn = "player"

            # Check for win/lose conditions
            if opponent_health <= 0:
                game_state = "win"
            elif player_health <= 0:
                game_state = "lose"

        elif game_state == "win":
            screen.fill(BLACK)
            win_text = font.render("You Win!", True, WHITE)
            screen.blit(win_text, (WIDTH // 2 - win_text.get_width() // 2, HEIGHT // 2 - win_text.get_height() // 2))
            pygame.time.wait(2000)
            return

        elif game_state == "lose":
            screen.fill(BLACK)
            lose_text = font.render("You Lose!", True, WHITE)
            screen.blit(lose_text, (WIDTH // 2 - lose_text.get_width() // 2, HEIGHT // 2 - lose_text.get_height() // 2))
            pygame.time.wait(2000)
            return

        # Render the first segment's elements
        if game_state == "playing":
            screen.blit(background, (0, 0))
            screen.blit(player_image, (player_rect.x, player_rect.y))
            pygame.draw.rect(screen, GREEN, goal_rect)
            for obstacle in obstacles:
                x, y, width, height = obstacle["dimensions"]
                screen.blit(obstacle["picture"], (x, y))

        pygame.display.flip()
        clock.tick(30)


    # Call the function to start level three when appropriate, e.g., on game start or after completing level 2
run_level_three()
