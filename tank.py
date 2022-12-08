import pygame
import time
import sys

pygame.init()

# Create the screen
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Tank Attack')

moving_left = False
moving_right = False
moving_up = False
moving_down = False


class Tank(pygame.sprite.Sprite):
    def __init__(self, images, x, y, speed, direction):
        pygame.sprite.Sprite.__init__(self)
        self.alive = True
        self.speed = speed  # How fast the tank moves
        self.direction = direction  # Where the tank is
        img = pygame.image.load(images)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def move_1(self, moving_left, moving_right, moving_up, moving_down):
        dx = 0
        dy = 0
        # assign movement variables if moving left or right
        if moving_left:
            dx = -self.speed
        if moving_right:
            dx = self.speed
            self.direction = 1
        if moving_up:
            dy = -self.speed
            # self.direction = -1
        if moving_down:
            dy = self.speed
            # self.direction = 1
        # update rectangle position
        self.rect.x += dx
        self.rect.y += dy
        # Sets the X bounds for the Tank
        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.x >= 290:
            self.rect.x = 290
        # Sets the Y bounds for the Tank
        if self.rect.y <= 390:
            self.rect.y = 390
        elif self.rect.y >= 550:
            self.rect.y = 550

    def move_2(self, moving_left_2, moving_right_2, moving_up_2, moving_down_2):
        dx = 0
        dy = 0
        # assign movement variables if moving left or right
        if moving_left_2:
            dx = -self.speed
            self.direction = -1
        if moving_right_2:
            dx = self.speed
        if moving_up_2:
            dy = -self.speed
        if moving_down_2:
            dy = self.speed
        # update rectangle position
        self.rect.x += dx
        self.rect.y += dy

        if self.rect.x <= 320:
            self.rect.x = 320
        elif self.rect.x >= 645:
            self.rect.x = 645

        # Sets the Y bounds for the Tank
        if self.rect.y <= 390:
            self.rect.y = 390
        elif self.rect.y >= 550:
            self.rect.y = 550

    def draw(self):
        screen.blit(pygame.transform.flip(self.image, False, False), self.rect)
