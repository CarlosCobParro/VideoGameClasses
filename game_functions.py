import sys
import pygame
from bullet import Bullet
from ship import Ship

from pygame.sprite import Group
dash=0

def check_events_I(ai_settings, screen,ship, bullets):

 #Respond to keypresses and mouse events#
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        right_left(event,ship)
        Up_Down(event,ship)
        fire(event,bullets,ai_settings,screen,ship)








def update_screen(ai_settings, screen,ship, bullets):

    screen.fill(ai_settings.bg_color)
    ship.blitme()

    for bullet in bullets.sprites():
        bullet.draw_bullet()
    pygame.display.flip()


def right_left(event,ship):
    keys = pygame.key.get_pressed()

    if event.type == pygame.KEYDOWN:

        if keys[pygame.K_d] == 1:
            ship.moving_right = True

        elif keys[pygame.K_a] == 1:
            ship.moving_left = True

        if keys[pygame.K_p] == 1:
            ship.boost = True

    keys = pygame.key.get_pressed()
    if event.type == pygame.KEYUP:

        if keys[pygame.K_d] == 0:
            ship.moving_right = False

        if keys[pygame.K_a] == 0:
            ship.moving_left = False

        if keys[pygame.K_p] ==0:
            ship.boost = False


def Up_Down(event,ship):
    keys = pygame.key.get_pressed()

#pulse key
    if event.type == pygame.KEYDOWN:

        if keys[pygame.K_s] == 1:
            ship.moving_up = True

        elif keys[pygame.K_w] == 1:
            ship.moving_down = True

        if keys[pygame.K_p] == 1:
            ship.boost = True

#unpulse key
    #keys = pygame.key.get_pressed()
    if event.type == pygame.KEYUP:

        if keys[pygame.K_s] == 0:
            ship.moving_up = False

        if keys[pygame.K_w] == 0:
            ship.moving_down = False

        if keys[pygame.K_p] == 0:
            ship.boost=False

def fire(event,bullets,ai_settings,screen,ship):

    keys = pygame.key.get_pressed()
    if event.type == pygame.KEYDOWN:
        if keys[pygame.K_SPACE]==1:
            new_bullet=Bullet(ai_settings,screen,ship)
            bullets.add(new_bullet)

def deleting_bullets(bullets):
    for bullet in bullets.copy():

        if bullet.rect.bottom <= 0:

            bullets.remove(bullet)