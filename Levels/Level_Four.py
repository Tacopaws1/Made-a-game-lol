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

# Game variables (Global)
player_x = 150
player_y = 300
opponent_x = 500
opponent_y = 300

pygame_icon = pygame.image.load(get_asset_path('game_icon.webp'))
pygame.display.set_icon(pygame_icon)

# Initialize Pygame
pygame.init()
small_font = pygame.font.Font(None, 40)

# Screen dimensions
WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Level 4")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
PINK = (255, 192, 203)
BLACK = (0, 0, 0)

# Clock
clock = pygame.time.Clock()

# Load images
background_turn = pygame.image.load(get_asset_path("background_turn.jpg"))
background_turn = pygame.transform.scale(background_turn, (WIDTH, HEIGHT))

player_idle_image = pygame.image.load(get_asset_path("Protag_side.png"))
player_attack_image = pygame.image.load(get_asset_path("Hero_attack_1.png"))
player_alt_attack_image = pygame.image.load(get_asset_path("Hero_attack_2.png"))  # Alternate attack image

opponent_idle_image = pygame.image.load(get_asset_path("Penelopina.png"))
opponent_attack_image = pygame.image.load(get_asset_path("Penelopina_attack1.png"))
opponent_alt_attack_image = pygame.image.load(get_asset_path("Penelopina_attack_2.png"))  # Alternate attack image

# Health bars
player_health = 100
opponent_health = 100
font = pygame.font.Font(None, 30)
controls_text = [
    "Press SPACE for Normal Attack (-10 HP)",
    "Press D for Alternate Attack (-20 HP)",
]

# Attack durations
attack_duration = 500

# State variables
player_attacking = False
player_attack_type = None  # "normal" or "alternate"
opponent_attacking = False
opponent_attack_type = None  # "normal" or "alternate"
attack_start_time = 0
turn = "player"

# Offsets
sprite_y_offset = 50

# Function to run level four
def run_level_four():
    global player_health, opponent_health, player_attacking, player_attack_type, opponent_attacking, opponent_attack_type, turn, attack_start_time
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Get key presses
        keys = pygame.key.get_pressed()

        # Player Turn
        if turn == "player":
            text = small_font.render("Your Turn: Press Space, D, or B", True, BLACK)
            screen.blit(text, (100, HEIGHT - 100))

            # Check for attacks
            if not player_attacking:
                if keys[pygame.K_SPACE]:  # Normal attack
                    player_attacking = True
                    player_attack_type = "normal"
                    attack_start_time = pygame.time.get_ticks()
                    opponent_health -= 10
                    turn = "opponent"
                elif keys[pygame.K_d]:  # Alternate attack
                    player_attacking = True
                    player_attack_type = "alternate"
                    attack_start_time = pygame.time.get_ticks()
                    opponent_health -= 20  # Alternate attack deals more damage
                    turn = "opponent"

        # Opponent Turn
        if turn == "opponent" and not opponent_attacking:
            pygame.time.wait(1000)  # Simulate delay for opponent action
            opponent_attacking = True
            opponent_attack_type = random.choice(["normal", "alternate"])  # Random attack type
            attack_start_time = pygame.time.get_ticks()
            if opponent_attack_type == "normal":
                player_health -= 10
            else:
                player_health -= 15  # Alternate attack deals more damage
            turn = "player"

        # Clear screen and background
        screen.blit(background_turn, (0, 0))

        # Draw health bars
        pygame.draw.rect(screen, GREEN, (50, 50, player_health * 2, 20))
        pygame.draw.rect(screen, GREEN, (WIDTH - 250, 50, opponent_health * 2, 20))
        screen.blit(font.render("Hero", True, WHITE), (50, 20))
        screen.blit(font.render("Penelopina The Mystical", True, PINK), (WIDTH - 250, 20))

        # Draw controls instructions
        y_offset = HEIGHT - 100  # Position instructions near the bottom
        for i, line in enumerate(controls_text):
            control_surface = small_font.render(line, True, WHITE)
            screen.blit(control_surface, (50, y_offset-300 + i * 30))

        # Render player sprite and attack animation
        if player_attacking:
            if pygame.time.get_ticks() - attack_start_time < attack_duration:
                if player_attack_type == "normal":
                    screen.blit(player_attack_image, (player_x, player_y))
                elif player_attack_type == "alternate":
                    screen.blit(player_alt_attack_image, (player_x, player_y))
            else:
                player_attacking = False
        else:
            screen.blit(player_idle_image, (player_x, player_y))

        # Render opponent sprite and attack animation
        if opponent_attacking:
            if pygame.time.get_ticks() - attack_start_time < attack_duration:
                if opponent_attack_type == "normal":
                    screen.blit(opponent_attack_image, (opponent_x, opponent_y))
                elif opponent_attack_type == "alternate":
                    screen.blit(opponent_alt_attack_image, (opponent_x, opponent_y))
            else:
                opponent_attacking = False
        else:
            screen.blit(opponent_idle_image, (opponent_x, opponent_y))

        # Display winner text
        if player_health <= 0:
            screen.fill(BLACK)
            winner_text = font.render("Opponent Wins!", True, WHITE)
            screen.blit(winner_text, (WIDTH // 2 - winner_text.get_width() // 2, HEIGHT // 2))
            pygame.time.wait(2000)
            return
        elif opponent_health <= 0:
            screen.fill(BLACK)
            winner_text = font.render("Player Wins!", True, WHITE)
            screen.blit(winner_text, (WIDTH // 2 - winner_text.get_width() // 2, HEIGHT // 2))
            pygame.time.wait(2000)
            return

        pygame.display.flip()
        clock.tick(30)

# Run the level
run_level_four()
