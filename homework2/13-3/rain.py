# Rain class file
import pygame
from pygame.sprite import Sprite


class Rain(Sprite):
    """A class to manage rain falling from the top of the screen"""

    def __init__(self, ai_game):
        """Create a raindrop as an object at top of the screen"""
        super().__init__()
        self. screen = ai_game.screen
        self.settings = ai_game.settings

        # load the alien
        self.image = pygame.image.load('images/rain.png')
        self.rect = self.image.get_rect()

        # Start new drops from top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store individual position of alien
        self.y = float(self.rect.y)

    def check_edges(self):
        # checks for if a raindrop is at the top of bottom of the screen. returns true if the alien is on the edge
        screen_rect = self.screen.get_rect()
        if self.rect.bottom >= screen_rect.bottom or self.rect.top <= 0:
            return True

    def update(self):
        """move the rain down"""
        self.y += self.settings.rain_speed
        self.rect.y = self.y
