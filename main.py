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
from Levels.Level_One import run_level_one
from Levels.Level_Two import run_level_two
from Levels.Level_Three import run_level_three
from Levels.Level_Four import run_level_four
from Levels.Level_Five import run_level_five
from Levels.Level_Six import run_level_six
from Levels.Level_Seven import run_level_seven
from Levels.Level_Eight import run_level_eight
from Levels.Level_Nine import run_level_nine
from Levels.Level_Ten import run_level_ten
import pygame
import asset_manager
import sys
import os


def main():
    # Initialize Pygame
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Game of the year 2025")
    pygame_icon = pygame.image.load('game_icon.webp')
    pygame.display.set_icon(pygame_icon)
    # Play Level One
    run_level_one(screen)
    #Play Level Two
    run_level_two(screen)
    #Play Level Three
    run_level_three(screen)
    #Play Level Four
    run_level_four(screen)
    #Play Level Five
    run_level_five(screen)
    #Play Level Six
    run_level_six(screen)
    #Play Level Seven
    run_level_seven(screen)
    #Play Level Eight
    run_level_eight(screen)
    #Play Level Nine
    run_level_nine(screen)
    #Play Level Ten
    run_level_ten(screen)








    pygame.quit()

if __name__ == "__main__":
    main()
