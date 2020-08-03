import sys
import pygame
from settings import Settings
from ship import Ship

import game_functions as gf
from pygame.sprite import Group

def run_game():
    pygame.init()
    #screen=pygame.display.set_mode((1200.800))
    #pygame.display.set_caption("Alien Carlos")
    #bg_color=(230,230,230)
    ai_settings=Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption(ai_settings.name)
    #we generate a object of the Ship class
    ship = Ship(screen)
    bullets = Group()


    while True:
        gf.check_events_I(ai_settings, screen,ship, bullets)

        ship.update()

        bullets.update()
        gf.deleting_bullets(bullets)
        gf.update_screen(ai_settings, screen,ship, bullets)



run_game()