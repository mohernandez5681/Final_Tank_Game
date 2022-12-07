import pygame
import time
from tank import Tank
from pygame import mixer
from tank import Bullet
import button

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

# define player action variables
moving_left = False
moving_right = False
shoot = False
# Creates the tank
BlueTank = Tank('images/tankblue.png', 30, 500, 1, 10)
RedTank = Tank('images/tankred.png', 670, 500, 1, 10)

# load bullet image
bullet_img = pygame.image.load('images/bullet.png').convert_alpha()
bullet_group = Bullet(30,500,1)

start_img = pygame.image.load('images/start.png').convert_alpha()
exit_img = pygame.image.load('images/quit.png').convert_alpha()
# Plays a song in the Background of the game
mixer.music.load('background.wav')
mixer.music.play(-1)

# Load Background Image
background = pygame.image.load('images/desert.png').convert_alpha()

# Define game variables
start_game = False


# function for drawing background
def draw_bg():
    scaled_background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_background, (0, 0))


# Create buttons
exit_button = button.Button(130, 300, exit_img, 1)
start_button = button.Button(130, 40, start_img, 1)

# Game loop
running = True
while running:
    clock.tick(FPS)

    if start_game == False:
        # draw menu
        screen.fill((255, 255, 255))

        # add buttons
        if start_button.draw(screen):
            start_game = True
        if exit_button.draw(screen):
            running = False


    else:

        draw_bg()

        BlueTank.draw()
        BlueTank.move(moving_left, moving_right)
        RedTank.draw()
        # update and draw groups


    if BlueTank.alive:
        # shoot bullets
        if shoot:
            BlueTank.shoot()
        BlueTank.move(moving_left, moving_right)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Keyboard presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moving_left = True
            if event.key == pygame.K_RIGHT:
                moving_right = True
            if event.key == pygame.K_SPACE:
                shoot = True
            if event.key == pygame.K_ESCAPE:
                running = False

        # Keyboard released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moving_left = False
            if event.key == pygame.K_RIGHT:
                moving_right = False
            if event.key == pygame.K_SPACE:
                shoot = False
    pygame.display.update()
