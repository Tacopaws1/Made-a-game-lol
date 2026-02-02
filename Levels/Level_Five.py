"""
Course Number: ENGR 13300
Semester:  Fall 2024

Description:
A 10 level turn based game that increases in difficulty over time

Assignment Information:
    Assignment:     Independant project
    Team ID:        011-30
    Author:         Jase Gable, gable8@purdue.edu
    Date:           11/28/2024

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

pygame_icon = pygame.image.load(get_asset_path('game_icon.webp'))
pygame.display.set_icon(pygame_icon)

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Level 5")
small_font = pygame.font.Font(None, 40)
# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
PINK = (255, 192, 203)
# Clock
clock = pygame.time.Clock()

# Load images
background_image = pygame.image.load(get_asset_path("background_turn.jpg"))
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

player_idle_image = pygame.image.load(get_asset_path("protag_side.png"))
player_attack_image = pygame.image.load(get_asset_path("Hero_attack_1.png"))
player_alt_attack_image = pygame.image.load(get_asset_path("Hero_attack_2.png"))
player_block_image = pygame.image.load(get_asset_path("Hero_block.png"))

opponent_idle_image = pygame.image.load(get_asset_path("GoLiath.png"))
opponent_attack_image = pygame.image.load(get_asset_path("GoLiath_attack_1.png"))
opponent_alt_attack_image = pygame.image.load(get_asset_path("GoLiath_attack_2.png"))
opponent_block_image = pygame.image.load(get_asset_path("GoLiath_Block.png"))

# Character positions
player_x, player_y = 50, 300
opponent_x, opponent_y = 500, 250

# Health bars
player_health = 110
opponent_health = 100
health_bar_width = 200
health_bar_height = 20

# Font
font = pygame.font.Font(None, 36)

# States
turn = "player"  # Whose turn it is: "player" or "opponent"
player_attacking = False
opponent_attacking = False
player_blocking = False
opponent_blocking = False
attack_start_time = 0
attack_duration = 500
player_attack_type = "normal"
opponent_attack_type = "normal"
damage_reduction = 0.5  # 50% damage is taken when blocking
game_over = False  # Tracks if the game is over
winner = None  # Tracks the winner ("player" or "opponent")

# Function to run level five
def run_level_five():
    global player_health, opponent_health, player_attacking, player_attack_type, opponent_attacking, opponent_attack_type, turn, attack_start_time, game_over, winner, opponent_blocking  # Add global variables

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if game_over:
            # Display win/lose screen
            screen.fill(BLACK)
            if winner == "player":
                win_text = font.render("You Win!", True, GREEN)
                pygame.time.wait(2000)
                return
            else:
                win_text = font.render("You Lose!", True, RED)
            screen.blit(win_text, (WIDTH // 2 - win_text.get_width() // 2, HEIGHT // 2))
            pygame.display.flip()
            pygame.time.wait(2000)
            return
            continue

        # Get key presses
        keys = pygame.key.get_pressed()

        # Player's turn
        if turn == "player":
            if keys[pygame.K_SPACE]:  # Normal attack
                if not player_attacking and not player_blocking:
                    player_attacking = True
                    player_attack_type = "normal"
                    attack_start_time = pygame.time.get_ticks()
            elif keys[pygame.K_d]:  # Alternate attack
                if not player_attacking and not player_blocking:
                    player_attacking = True
                    player_attack_type = "alternate"
                    attack_start_time = pygame.time.get_ticks()
            elif keys[pygame.K_b]:  # Block
                player_blocking = True
            else:
                player_blocking = False

            # Resolve player actions
            if player_attacking and pygame.time.get_ticks() - attack_start_time >= attack_duration:
                damage = 10 if player_attack_type == "normal" else 15  # Damage values
                if opponent_blocking:
                    opponent_health -= int(damage * damage_reduction)  # Reduced damage
                else:
                    opponent_health -= damage  # Full damage
                player_attacking = False
                turn = "opponent"  # Switch to opponent's turn
            if not player_attacking and not player_blocking:
                turn = "opponent"
            turn = "opponent"

        # Opponent's turn
        elif turn == "opponent":
            if not opponent_attacking and not opponent_blocking:
                # Randomly decide action
                pygame.time.wait(100)  # Simulate delay for opponent action
                actions = (["attack", "alternate_attack", "block"])
                weights = [0.6, 0.3, 0.1]  # Adjust these to balance the opponent's behavior
                action = random.choices(actions, weights=weights, k=1)[0]
                if action == "attack":
                    opponent_attacking = True
                    opponent_attack_type = "normal"
                    attack_start_time = pygame.time.get_ticks()
                elif action == "alternate_attack":
                    opponent_attacking = True
                    opponent_attack_type = "alternate"
                    attack_start_time = pygame.time.get_ticks()
                elif action == "block":
                    opponent_blocking = True
                attack_start_time = pygame.time.get_ticks()

            # Resolve opponent actions
            if opponent_attacking and pygame.time.get_ticks() - attack_start_time >= attack_duration:
                damage = 10 if opponent_attack_type == "normal" else 15  # Damage values
                if player_blocking:
                    player_health -= int(damage * damage_reduction)  # Reduced damage
                else:
                    player_health -= damage  # Full damage
                opponent_attacking = False
                turn = "player"  # Switch to player's turn
            elif opponent_blocking and pygame.time.get_ticks() - attack_start_time >= attack_duration:
                opponent_blocking = False  # Reset opponent block state
                turn = "player"  # Switch to player's turn
            turn = "player"

        # Check for game over
        if player_health <= 0:
            game_over = True
            winner = "opponent"
        elif opponent_health <= 0:
            game_over = True
            winner = "player"

        # Drawing
        screen.blit(background_image, (0, 0))

        # Health bars
        pygame.draw.rect(screen, GREEN, (50, 50, int((player_health / 100) * health_bar_width), health_bar_height))
        pygame.draw.rect(screen, GREEN, (450, 50, int((opponent_health / 100) * 300), health_bar_height))
        screen.blit(font.render("Hero", True, WHITE), (50, 20))
        screen.blit(font.render("Cave Dweller GoLiath", True, WHITE), (500, 20))
        text = small_font.render("Press Space, D, or B", True, BLACK)
        screen.blit(text, (100, HEIGHT - 400))
        
        # Draw player
        if player_attacking:
            if pygame.time.get_ticks() - attack_start_time < attack_duration:
                if player_attack_type == "normal":
                    screen.blit(player_attack_image, (player_x, player_y))
                elif player_attack_type == "alternate":
                    screen.blit(player_alt_attack_image, (player_x, player_y))
        elif player_blocking:
            screen.blit(player_block_image, (player_x, player_y))
        else:
            screen.blit(player_idle_image, (player_x, player_y))

        # Draw opponent
        if opponent_attacking:
            if pygame.time.get_ticks() - attack_start_time < attack_duration:
                if opponent_attack_type == "normal":
                    screen.blit(opponent_attack_image, (opponent_x, opponent_y))
                elif opponent_attack_type == "alternate":
                    screen.blit(opponent_alt_attack_image, (opponent_x, opponent_y))
        elif opponent_blocking:
            screen.blit(opponent_block_image, (opponent_x, opponent_y))
        else:
            screen.blit(opponent_idle_image, (opponent_x, opponent_y))

        pygame.display.flip()
        clock.tick(30)

run_level_five()
