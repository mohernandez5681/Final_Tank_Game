import pygame
from tank import Tank
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
bullet_img = pygame.image.load('images/bullet.png')

# class Bullet:
#     def __init__(self, images, x, y):
#         img = pygame.image.load(images)
#         self.image = img
#         self.rect = self.image.get_rect()
#         self.speed = 10
#         self.rect.center = (x,y)
#         self.direction = 1
#
#
#
#
#     def update(self):

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 10
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = direction

    def update(self):
        # move bullet
        self.rect.x += (self.direction * self.speed)
        # check if bullet has gone off screen
        if self.rect.right < 0 or self.rect.left > SCREEN_WIDTH:
            self.kill()

        # check collision with characters
        if pygame.sprite.spritecollide(BlueTank, bullet_group, False):
            if BlueTank.alive:
                BlueTank.health -= 5
                self.kill()
        if pygame.sprite.spritecollide(RedTank, bullet_group, False):
            if RedTank.alive:
                RedTank.health -= 25
                self.kill()

bullet_group = pygame.sprite.Group()


BlueTank = Tank('images/tankblue.png', 30, 500, 1)
RedTank = Tank('images/tankred.png', 670, 500, 1)