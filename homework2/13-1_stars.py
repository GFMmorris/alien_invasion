import pygame
from pygame.sprite import Sprite

class Start(Sprite):
    """Star class"""

    def __intit__(self, ai_game):
        super.__init__()
        self.screen = ai_game.screen

        self.image = pygame.image.load('images/gold_star.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)




