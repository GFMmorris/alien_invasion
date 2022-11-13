import pygame
from random import randint
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """initialize alien and set its start position"""
        super().__init__()
        self.screen = ai_game.screen

        # Alien settings.
        #  alien_frequency controls how often a new alien appear.s
        #    Higher values -> more frequent aliens. Max = 1.0.
        self.alien_frequency = 0.015
        self.alien_speed = 1.5

        # load the alien image and set its rect attribute
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # start each new alien near the top left of the screen
        self.rect.left = self.screen.get_rect().right

        alien_top_max = self.screen.get_rect().height - self.rect.height
        self.rect.top = randint(0, alien_top_max)


        # store the exact horizontal position of alien
        self.x = float(self.rect.x)


    def update(self):
        """Move the alien to the right or left"""
        self.x -= self.alien_speed
        self.rect.x = self.x
