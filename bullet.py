import pygame

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Bullet:
    def __init__(self, images, x, y):
        img = pygame.image.load(images)
        self.image = img
        self.rect = self.image.get_rect()
        self.speed = 10
        self.rect.center = (x,y)
        self.direction = 1




    def update(self):
