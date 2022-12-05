import pygame
import time
import math
from tank import Tank
from pygame import mixer



# Initialize the pygame
pygame.init()

# Create the screen
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Tank Attack')


BlueTank = Tank('images/tankblue.png', 10, 500)
RedTank = Tank('images/tankred.png', 600, 500)


# Plays a song in the Background of the game
mixer.music.load('background.wav')
mixer.music.play(-1)



# Load Background Image
background = pygame.image.load('images/desert.png').convert_alpha()

# function for drawing background
def draw_bg():
    scaled_background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_background, (0, 0))





# Game loop
running = True
while running:
    draw_bg()
    BlueTank.update_1()
    RedTank.update_2()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    pygame.display.update()
