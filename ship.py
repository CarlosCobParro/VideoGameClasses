import sys
import pygame


class Ship():
    def __init__(self, screen):
        self.screen = screen

        # load the ship image and get its rect.
        self.image = pygame.image.load('/home/carlos/Desktop/pythongame/images/ship.bmp')
        # to acces the surface is rect
        self.rect = self.image.get_rect()

        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.rect.bottom = self.screen_rect.bottom

        # Movement sets
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.boost = False
        self.speed=1





    def blitme(self):
        # draw the ship in the screen where self.rect specified.
        self.screen.blit(self.image, self.rect)

    def update(self):
        # move the ship
        if ((self.rect.right < self.screen_rect.right) and (self.rect.left > self.screen_rect.left)) and (
                (self.rect.top > self.screen_rect.top) and (self.rect.bottom < self.screen_rect.bottom)):
            # right and left
            if (self.moving_right == True) and (self.boost == False):
                self.rect.centerx += 2 * self.speed
            elif (self.moving_right == True) and (self.boost == True):
                self.rect.centerx += 4 * self.speed

            if (self.moving_left == True) and (self.boost == False):
                self.rect.centerx -= 2 * self.speed
            elif (self.moving_left == True) and (self.boost == True):
                self.rect.centerx -= 4 * self.speed

            # up and down
            if (self.moving_up == True) and (self.boost == False):
                self.rect.centery += 2 * self.speed
            elif (self.moving_up == True) and (self.boost == True):
                self.rect.centery += (4 * self.speed)

            if (self.moving_down == True) and (self.boost == False):
                self.rect.centery -= 2 * self.speed
            elif (self.moving_down == True) and (self.boost == True):
                self.rect.centery -= 4 * self.speed

        # boundirings
        elif self.rect.right >= self.screen_rect.right:
            self.rect.right = self.screen_rect.right - 1
        elif self.rect.left <= self.screen_rect.left:
            self.rect.left = self.screen_rect.left + 1
        elif self.rect.top <= self.screen_rect.top:
            self.rect.top = self.screen_rect.top + 1
        elif self.rect.bottom >= self.screen_rect.bottom:
            self.rect.bottom = self.screen_rect.bottom - 1


