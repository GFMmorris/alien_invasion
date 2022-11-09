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
