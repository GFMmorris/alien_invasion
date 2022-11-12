import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """initialize alien and set its start position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # load the alien image and set its rect attribute
        self.image = pygame.image.load('images/rain.png')
        self.rect = self.image.get_rect()

        # start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the exact horizontal position of alien
        self.y = float(self.rect.y)

    def update(self):
        """Move the alien to the right or left"""
        self.y += self.settings.alien_speed
        self.rect.y = self.y