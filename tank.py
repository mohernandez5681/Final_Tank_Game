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

bullet_img = pygame.image.load('images/bullet.png').convert_alpha()
bullet_group = pygame.sprite.Group()


class Tank(pygame.sprite.Sprite):
    def __init__(self, images, x, y, speed, ammo):
        pygame.sprite.Sprite.__init__(self)
        self.alive = True
        self.speed = speed  # How fast the tank moves
        self.shoot_cooldown = 0
        self.ammo = ammo
        self.health = 100
        self.direction = 1  # Where the tank is
        self.flip = False  # Flip the sprite art
        img = pygame.image.load(images)
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.check_alive()
        # update cooldown
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1

    def move_1(self, moving_left, moving_right, moving_up, moving_down):
        dx = 0
        dy = 0
        # assign movement variables if moving left or right
        if moving_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1
        if moving_right:
            dx = self.speed
            self.flip = False
            self.direction = 1
        if moving_up:
            dy = -self.speed
            self.flip = False
            self.direction = -1
        if moving_down:
            dy = self.speed
            self.flip = False
            self.direction = 1

        # update rectangle position
        self.rect.x += dx
        self.rect.y += dy

    def move_2(self, moving_left_2, moving_right_2, moving_up_2, moving_down_2):
        dx = 0
        dy = 0
        # assign movement variables if moving left or right
        if moving_left_2:
            dx = -self.speed
            self.flip = False
            self.direction = -1
        if moving_right_2:
            dx = self.speed
            self.flip = True
            self.direction = 1
        if moving_up_2:
            dy = -self.speed
            self.flip = False
            self.direction = -1
        if moving_down_2:
            dy = self.speed
            self.flip = False
            self.direction = 1

        # update rectangle position
        self.rect.x += dx
        self.rect.y += dy

    def shoot(self):
        if self.shoot_cooldown == 0 and self.ammo > 0:
            self.shoot_cooldown = 20
            bullet = Bullet(self.rect.centerx + (0.6 * self.rect.size[0] * self.direction), self.rect.centery,
                            self.direction)
            bullet_group.add(bullet)
            # reduce ammo
            self.ammo -= 1

    def check_alive(self):
        if self.health <= 0:
            self.health = 0
            self.speed = 0
            self.alive = False

    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)


BlueTank = Tank('images/tankblue.png', 30, 500, 1, 10)
RedTank = Tank('images/tankred.png', 670, 500, 1, 10)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        direction = 1
        self.direction = direction
        self.speed = 1
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        # move bullet
        self.rect.x += (self.direction * self.speed)
        # check if bullet has gone offscreen
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


#     # def update_1(self):
#     dx = 0
#     dy = 0
#     # Get keypresses
#     key = pygame.key.get_pressed()
#     if key[pygame.K_LEFT]:
#         dx -= 1
#     if key[pygame.K_RIGHT]:
#         dx += 1
#     if key[pygame.K_DOWN]:
#         dy += 1
#     if key[pygame.K_UP]:
#         dy -= 1
#
#     # check for collison
#
#     # update tank coordinates
#     self.rect.x += dx
#     self.rect.y += dy
#
#     # draw tank onto screen
#     screen.blit(self.image, self.rect)
#
#     # Sets the X bounds for the Tank
#     if self.rect.x <= 0:
#         self.rect.x = 0
#     elif self.rect.x >= 290:
#         self.rect.x = 290
#     # Sets the Y bounds for the Tank
#     if self.rect.y <= 390:
#         self.rect.y = 390
#     elif self.rect.y >= 550:
#         self.rect.y = 550
#
# def update_2(self):
#     dx = 0
#     dy = 0
#     # Get keypresses
#     key = pygame.key.get_pressed()
#     if key[pygame.K_a]:
#         dx -= 1
#     if key[pygame.K_d]:
#         dx += 1
#     if key[pygame.K_w]:
#         dy -= 1
#     if key[pygame.K_s]:
#         dy += 1
#
#     # check for collison
#
#     # update tank coordinates
#     self.rect.x += dx
#     self.rect.y += dy
#
#     # draw tank onto screen
#     screen.blit(self.image, self.rect)
#
#     # Sets the X bounds for the Tank
#     if self.rect.x <= 320:
#         self.rect.x = 320
#     elif self.rect.x >= 645:
#         self.rect.x = 645
#
#     # Sets the Y bounds for the Tank
#     if self.rect.y <= 390:
#         self.rect.y = 390
#     elif self.rect.y >= 550:
#         self.rect.y = 550
