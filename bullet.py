import sys
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):

    def __init__(self, ai_settings, screen, ship):

        super(Bullet,self).__init__()
        self.screen=screen
        self.image_bullet=pygame.image.load('/home/carlos/Desktop/pythongame/images/bullet.png')
        #self.rect= pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect=self.image_bullet.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = ship.rect.centerx
        self.rect.centery=ship.rect.centery
        self.rect.top = ship.rect.top

        self.y = float(self.rect.y)

        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        self.y-=self.speed_factor
        self.rect.y=self.y

    def draw_bullet(self):
        self.screen.blit(self.image_bullet, self.rect)

