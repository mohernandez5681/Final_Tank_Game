import pygame
import time
import sys

pygame.init()

# Create the screen
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Tank Attack')


class Tank:
    def __init__(self, images, x, y):
        img = pygame.image.load(images)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update_1(self):
        dx = 0
        dy = 0
        # Get keypresses
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            dx -= 1
        if key[pygame.K_RIGHT]:
            dx += 1
        if key[pygame.K_DOWN]:
            dy += 1
        if key[pygame.K_UP]:
            dy -= 1

        # check for collison

        # update tank coordinates
        self.rect.x += dx
        self.rect.y += dy

        # draw tank onto screen
        screen.blit(self.image, (self.rect.x, self.rect.y))

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

    def update_2(self):
        dx = 0
        dy = 0
        # Get keypresses
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            dx -= 1
        if key[pygame.K_d]:
            dx += 1
        if key[pygame.K_w]:
            dy -= 1
        if key[pygame.K_s]:
            dy += 1

        # check for collison

        # update tank coordinates
        self.rect.x += dx
        self.rect.y += dy

        # draw tank onto screen
        screen.blit(self.image, (self.rect.x, self.rect.y))

        # Sets the X bounds for the Tank
        if self.rect.x <= 320:
            self.rect.x = 320
        elif self.rect.x >= 645:
            self.rect.x = 645

        # Sets the Y bounds for the Tank
        if self.rect.y <= 390:
            self.rect.y = 390
        elif self.rect.y >= 550:
            self.rect.y = 550
