import pygame
import time
from tank import Tank
from pygame import mixer

# Initialize the pygame
pygame.init()

# Create the screen
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Tank Attack')

# set framrate
clock = pygame.time.Clock()
FPS = 60

moving_left = False
moving_right = False


BlueTank = Tank('images/tankblue.png', 30, 500, 1)
RedTank = Tank('images/tankred.png', 670, 500, 1)

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
    clock.tick(FPS)
    draw_bg()

    # BlueTank.update_1()
    # RedTank.update_2()
    BlueTank.draw()
    BlueTank.update(moving_left,moving_right)
    RedTank.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Keyboard presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moving_left = True
            if event.key == pygame.K_RIGHT:
                moving_right = True
            if event.key == pygame.K_ESCAPE:
                running = False

        # Keyboard released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moving_left = False
            if event.key == pygame.K_RIGHT:
                moving_right = False

    pygame.display.update()
