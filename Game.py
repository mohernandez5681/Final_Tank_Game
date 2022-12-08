import pygame
import time
from tank import Tank
from pygame import mixer
from bullet import Bullet
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
moving_up = False
moving_down = False
shoot = False

moving_left_2 = False
moving_right_2 = False
moving_up_2 = False
moving_down_2 = False
shoot_2 = False

# Creates the tank
BlueTank = Tank('images/tankblue.png', 30, 500, 1, 1)
RedTank = Tank('images/tankred.png', 670, 500, 1, -1)

tank_group = pygame.sprite.Group()
tank_group.add(BlueTank)
tank_group.add(RedTank)

bullet_group = pygame.sprite.Group()

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


# Loads start and exit images
start_img = pygame.image.load('images/start.png').convert_alpha()
exit_img = pygame.image.load('images/quit.png').convert_alpha()
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
        # update and draw groups
        tank_group.update()
        tank_group.draw(screen)
        bullet_group.update()
        bullet_group.draw(screen)


        if BlueTank.alive == True:
            # shoot bullets
            if shoot:
                bullet_1 = Bullet('images/bullet.png', BlueTank.rect.centerx + 23, BlueTank.rect.centery,
                                  BlueTank.direction)
                bullet_group.add(bullet_1)
                if pygame.sprite.spritecollide(RedTank, bullet_group, True):
                    bullet_1.kill()
                    RedTank.remove(tank_group)
                    RedTank.alive = False
            else:
                BlueTank.move_1(moving_left, moving_right, moving_up, moving_down)


        if RedTank.alive == True:
            # shoot bullets
            if shoot_2:
                bullet_2 = Bullet('images/bullet left.png', RedTank.rect.centerx -20, RedTank.rect.centery,
                                  RedTank.direction)
                bullet_group.add(bullet_2)
                if pygame.sprite.spritecollide(BlueTank, bullet_group, True):
                    bullet_2.kill()
                    BlueTank.remove(tank_group)
                    BlueTank.alive = False

            else:
                RedTank.move_2(moving_left_2, moving_right_2, moving_up_2, moving_down_2)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Keyboard presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moving_left = True
            if event.key == pygame.K_RIGHT:
                moving_right = True
            if event.key == pygame.K_DOWN:
                moving_down = True
            if event.key == pygame.K_UP:
                moving_up = True
            if event.key == pygame.K_SPACE:
                shoot = True

            if event.key == pygame.K_a:
                moving_left_2 = True
            if event.key == pygame.K_d:
                moving_right_2 = True
            if event.key == pygame.K_s:
                moving_down_2 = True
            if event.key == pygame.K_w:
                moving_up_2 = True
            if event.key == pygame.K_p:
                shoot_2 = True

            if event.key == pygame.K_ESCAPE:
                running = False

        # Keyboard released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moving_left = False
            if event.key == pygame.K_RIGHT:
                moving_right = False
            if event.key == pygame.K_DOWN:
                moving_down = False
            if event.key == pygame.K_UP:
                moving_up = False
            if event.key == pygame.K_SPACE:
                shoot = False

            if event.key == pygame.K_a:
                moving_left_2 = False
            if event.key == pygame.K_d:
                moving_right_2 = False
            if event.key == pygame.K_s:
                moving_down_2 = False
            if event.key == pygame.K_w:
                moving_up_2 = False
            if event.key == pygame.K_p:
                shoot_2 = False

    pygame.display.update()
pygame.quit()
