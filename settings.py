import sys
import pygame

speed = 1


class Settings():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.name = "Alien_invasor"

        #bullet settings
        self.bullet_speed_factor=4.5
        self.bullet_width=3
        self.bullet_height=15
        self.bullet_color=60,60,60



