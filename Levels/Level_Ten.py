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
import random
from asset_manager import get_asset_path

def run_level_ten():
    # Initialize Pygame
    pygame.init()
    pygame_icon = pygame.image.load(get_asset_path('game_icon.webp'))
    pygame.display.set_icon(pygame_icon)
    # Player properties
    player_width, player_height = 50, 50
    player_x, player_y = 10, 50
    player_speed = 5
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)

    # Goal area properties
    player_x, player_y = 50, 300
    opponent_x, opponent_y = 500, 250

    game_state = "playing"
    WIDTH, HEIGHT = 800, 600
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Level 10 FINAL")
    small_font = pygame.font.Font(None, 40)
    # Colors
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLACK = (0, 0, 0)
    GRAY = (111,111,111)
    PINK = (255, 192, 203)
    # Clock
    clock = pygame.time.Clock()


    player_idle_image = pygame.image.load(get_asset_path("protag_side.png"))
    player_idle_image = pygame.transform.scale(player_idle_image, (100, 100))
    player_attack1_image = pygame.image.load(get_asset_path("Hero_attack_1.png"))
    player_attack1_image = pygame.transform.scale(player_attack1_image, (100, 100))
    player_attack2_image = pygame.image.load(get_asset_path("Hero_attack_2.png"))
    player_attack2_image = pygame.transform.scale(player_attack2_image, (100, 100))
    player_block_image = pygame.image.load(get_asset_path("Hero_block.png"))
    player_block_image = pygame.transform.scale(player_block_image, (100, 100))

    opponent_idle_image_phase1 = pygame.image.load(get_asset_path("Evil_knife_guy.png"))
    opponent_idle_image_phase1 = pygame.transform.scale(opponent_idle_image_phase1, (300, 300))
    opponent_attack1_image_phase1 = pygame.image.load(get_asset_path("Knifeguy_attack1.png"))
    opponent_attack1_image_phase1 = pygame.transform.scale(opponent_attack1_image_phase1, (300, 300))
    opponent_attack2_image_phase1 = pygame.image.load(get_asset_path("Knifeguy_attack2.png"))
    opponent_attack2_image_phase1 = pygame.transform.scale(opponent_attack2_image_phase1, (300, 300))
    opponent_block_image_phase1 = pygame.image.load(get_asset_path("Evil_knife_guy.png"))
    opponent_block_image_phase1 = pygame.transform.scale(opponent_block_image_phase1, (300, 300))

    opponent_idle_image_phase2 = pygame.image.load(get_asset_path("Bingus.png"))
    opponent_idle_image_phase2 = pygame.transform.scale(opponent_idle_image_phase2, (300, 300))
    opponent_attack1_image_phase2 = pygame.image.load(get_asset_path("Bingus_attack1.png"))
    opponent_attack1_image_phase2 = pygame.transform.scale(opponent_attack1_image_phase2, (300, 300))
    opponent_attack2_image_phase2 = pygame.image.load(get_asset_path("Bingus_attack2.png"))
    opponent_attack2_image_phase2 = pygame.transform.scale(opponent_attack2_image_phase2, (300, 300))
    opponent_block_image_phase2 = pygame.image.load(get_asset_path("Bingus.png"))
    opponent_block_image_phase2 = pygame.transform.scale(opponent_block_image_phase2, (300, 300))
    background_image = pygame.image.load(get_asset_path("volcanolvl10.png"))
    background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
    turn_based_background = pygame.image.load(get_asset_path("volcanobackground.jpg"))
    turn_based_background = pygame.transform.scale(turn_based_background, (WIDTH, HEIGHT))
    player_image = pygame.image.load(get_asset_path("protag_front.png"))
    player_image = pygame.transform.scale(player_image, (50, 50))
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
        {"rect": pygame.Rect(0, 520, 1000, 1000), "image": "obstical2.jpg", "dimensions": (0, 505, 1000, 100)},
    ]

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
                    if keys[pygame.K_a]:
                        player_rect.x += player_speed
                    if keys[pygame.K_d]:
                        player_rect.x -= player_speed
                    if keys[pygame.K_w]:
                        player_rect.y += player_speed
                    if keys[pygame.K_s]:
                        player_rect.y -= player_speed

            # Check for reaching the goal
            if player_rect.colliderect(goal_rect):
                game_state = "turn_based"  # Transition to turn-based mode
            #  print("you hit goal yass queen slayy")

        elif game_state == "turn_based":

            pass
    # Draw the game screen (Obstacle phase)
        if game_state == "playing":
            screen.fill(WHITE)
            screen.blit(background_image, (0, 0))  # Draw background



            # Draw the goal area
            pygame.draw.rect(screen, GRAY, goal_rect)

            # Draw the player character
            screen.blit(player_image, player_rect)

            # Check for win/lose conditions based on reaching the goal
            pygame.display.flip()



        
        if game_state == "turn_based":
                #print(("me when i turn"))

                # Fonts
                font = pygame.font.Font(None, 50)
                small_font = pygame.font.Font(None, 40)

                # Game state
                game_state = "turn_based"  # Start directly in turn-based mode
                turn = "player"  # "player" or "opponent"
                current_player_attack = None  # Tracks the current player attack animation
                # Health and attack settings
                player_health = 210
                opponent_total_health = 200
                opponent_health = opponent_total_health
                opponent_phase = 1  # Start at phase 1
                attack_duration = 500
                player_attacking = False
                opponent_attacking = False
                player_blocking = False
                opponent_blocking = False
                attack_start_time = 0
                sprite_y_offset = 150

                # Names
                hero_name = "Hero"
                opponent_name_phase1 = "Evil Knife Guy"
                opponent_name_phase2 = "World Eater Bingus"
                opponent_name = opponent_name_phase1  # Start with phase 1 name
                def reset_animations():
                    global player_attacking, player_blocking, opponent_attacking, opponent_blocking
                    player_attacking = False
                    player_blocking = False
                    opponent_attacking = False
                    opponent_blocking = False
                # Main game loop
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        elif event.type == pygame.KEYDOWN:
                            if turn == "player":
                                if event.key == pygame.K_SPACE:  # Attack 1
                                    opponent_health -= 10
                                    current_player_attack = "attack1"
                                    player_attacking = True
                                    attack_start_time = pygame.time.get_ticks()
                                    turn = "opponent"
                                elif event.key == pygame.K_d:  # Attack 2
                                    opponent_health -= 15
                                    current_player_attack = "attack2"
                                    player_attacking = True
                                    attack_start_time = pygame.time.get_ticks()
                                    turn = "opponent"
                                elif event.key == pygame.K_b:  # Block
                                    player_blocking = True
                                    attack_start_time = pygame.time.get_ticks()
                                    turn = "opponent"
                    if game_state == "turn_based":
                        screen.fill(WHITE)
                        screen.blit(turn_based_background, (0, 0))


                        # Check phase transition and set opponent sprites and name
                        if opponent_health <= opponent_total_health * 0.8 and opponent_phase == 1:
                            opponent_phase = 2
                            opponent_name = opponent_name_phase2
                        if opponent_phase == 1:
                            opponent_idle_image = opponent_idle_image_phase1
                            opponent_attack1_image = opponent_attack1_image_phase1
                            opponent_attack2_image = opponent_attack2_image_phase1
                            opponent_block_image = opponent_block_image_phase1
                        else:  # Phase 2
                            opponent_idle_image = opponent_idle_image_phase2
                            opponent_attack1_image = opponent_attack1_image_phase2
                            opponent_attack2_image = opponent_attack2_image_phase2
                            opponent_block_image = opponent_block_image_phase2

                        # Display sprites
                        if player_attacking and pygame.time.get_ticks() - attack_start_time < attack_duration:
                            if current_player_attack == "attack1":
                                screen.blit(player_attack1_image, (100, HEIGHT // 2 - player_idle_image.get_height() // 2 + sprite_y_offset))
                            elif current_player_attack == "attack2":
                                screen.blit(player_attack2_image, (100, HEIGHT // 2 - player_idle_image.get_height() // 2 + sprite_y_offset))
                        elif player_blocking:
                            screen.blit(player_block_image, (100, HEIGHT // 2 - player_idle_image.get_height() // 2 + sprite_y_offset))
                        else:
                            screen.blit(player_idle_image, (100, HEIGHT // 2 - player_idle_image.get_height() // 2 + sprite_y_offset))

                        if opponent_attacking and pygame.time.get_ticks() - attack_start_time < attack_duration:
                            screen.blit(opponent_attack1_image, (WIDTH - 220, HEIGHT // 2 - opponent_idle_image.get_height() // 2 + sprite_y_offset))
                        elif opponent_blocking:
                            screen.blit(opponent_block_image, (WIDTH - 220, HEIGHT // 2 - opponent_idle_image.get_height() // 2 + sprite_y_offset))
                        else:
                            screen.blit(opponent_idle_image, (WIDTH - 220, HEIGHT // 2 - opponent_idle_image.get_height() // 2 + sprite_y_offset))

                        # Health bars
                        pygame.draw.rect(screen, RED, (50, 50, player_health * 0.5, 20))
                        pygame.draw.rect(screen, RED, (WIDTH - 350, 50, opponent_health * 2.5, 20))

                        # Display Hero's name above the health bar
                        hero_name_text = small_font.render(hero_name, True, WHITE)
                        screen.blit(hero_name_text, (50, 20))

                        # Display Opponent's name above the health bar
                        opponent_name_text = small_font.render(opponent_name, True, WHITE)
                        screen.blit(opponent_name_text, (WIDTH - 320, 20))

                        # Player's turn
                        if turn == "player":
                            text = small_font.render("Good Luck Challenger", True, WHITE)
                            screen.blit(text, (50, HEIGHT - 350))
                            keys = pygame.key.get_pressed()
                            if keys[pygame.K_1]:  # Attack 1
                                opponent_health -= 10
                                current_player_attack = "attack1"
                                player_attacking = True
                                attack_start_time = pygame.time.get_ticks()
                                turn = "opponent"
                            elif keys[pygame.K_2]:  # Attack 2
                                opponent_health -= 15
                                current_player_attack = "attack2"
                                player_attacking = True
                                attack_start_time = pygame.time.get_ticks()
                                turn = "opponent"
                            elif keys[pygame.K_b]:  # Block
                                player_blocking = True
                                attack_start_time = pygame.time.get_ticks()
                                turn = "opponent"
                        # Opponent's turn
                        elif turn == "opponent":
                            text = small_font.render("Opponent's Turn: Wait...", True, BLACK)
                            screen.blit(text, (50, HEIGHT - 50))
                            pygame.time.wait(750)

                            action = random.choices(["attack1", "attack2", "block"], weights=[0.5, 0.3, 0.2])[0]
                            if action == "attack1":
                                player_health -= 10
                                opponent_attacking = True
                                attack_start_time = pygame.time.get_ticks()
                            elif action == "attack2":
                                player_health -= 15
                                opponent_attacking = True
                                attack_start_time = pygame.time.get_ticks()
                            elif action == "block":
                                opponent_blocking = True
                                attack_start_time = pygame.time.get_ticks()
                            turn = "player"

                        # Check for win/lose conditions
                        if player_health <= 0:
                            game_state = "lose"
                        elif opponent_health <= 0:
                            game_state = "win"

                    # Win state
                    elif game_state == "win":
                        screen.fill(BLACK)
                        text = font.render("You Win!", True, PINK)
                        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))

                    # Lose state
                    elif game_state == "lose":
                        screen.fill(BLACK)
                        text = font.render("You Lose!", True, RED)
                        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))

                    pygame.display.flip()
                    clock.tick(30)
run_level_ten()