"""
Course Number: ENGR 13300
Semester:  Fall 2024

Description:
A 10 level turn based game that increases in difficulty over time

Assignment Information:
    Assignment:     Independant project
    Team ID:        011-30
    Author:         Jase Gable, gable8@purdue
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
from asset_manager import get_asset_path
pygame.init()

game_icon = pygame.image.load(get_asset_path("game_icon.webp"))

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Level One")
pygame_icon = game_icon
pygame.display.set_icon(pygame_icon)


def run_level_one(screen):
    pygame.display.set_caption("Level One")


    # Colors
    bg_color = (0, 0, 0)
    character_color = (255, 192, 203)
    goal_color = (0, 255, 0)

    # Player and goal
    player_rect = pygame.Rect(100, 250, 50, 50)
    goal_rect = pygame.Rect(600, 0, 200, 600)

    # Clock for frame rate
    clock = pygame.time.Clock()
    level_complete = False

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Player movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            player_rect.x -= 5
        elif keys[pygame.K_RIGHT]:
            print("invalid key press w, a, s, or d.")
        if keys[pygame.K_d]:
            player_rect.x += 5
        elif keys[pygame.K_LEFT]:
           print("invalid key press w, a, s, or d.")
        if keys[pygame.K_w]:
            player_rect.y -= 5
        elif keys[pygame.K_UP]:
            print("invalid key press w, a, s, or d.")
        if keys[pygame.K_s]:
            player_rect.y += 5
        elif keys[pygame.K_DOWN]:
          print("invalid key press w, a, s, or d.")

        # Check for goal collision
        if not level_complete and player_rect.colliderect(goal_rect):
            level_complete = True
   

        # Drawing
        screen.fill(bg_color)
        if level_complete:
            font = pygame.font.Font(None, 74)
            text = font.render("Level Complete!", True, character_color)
            screen.blit(text, (800 // 2 - text.get_width() // 2, 600 // 2 - text.get_height() // 2))
            pygame.display.flip()
            pygame.time.wait(2000)  # Wait 2 seconds
  
            return  # Exit level
        else:
            pygame.draw.rect(screen, character_color, player_rect)
            pygame.draw.rect(screen, goal_color, goal_rect)

        pygame.display.flip()
        clock.tick(30)
run_level_one(screen)