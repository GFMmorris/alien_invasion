import pygame
import sys
from pygame.sprite import Sprite


class Stars:

    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Stars")

        self.stars = pygame.sprite.Group()

    def _check_events(self):
        """Respond to key presses and mouse events."""
        for event in pygame.event.get():
            # (5)
            if event.type == pygame.QUIT:
                sys.exit()

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_q:
            sys.exit()

    def run_game(self):

        while True:
            self._check_events()
            self._update_screen()

    def _update_screen(self):
        self.screen.fill((230, 230, 230))
        self.stars.draw(self.screen)

        pygame.display.flip()


class Star(Sprite):
    """Star class"""

    def __intit__(self, ai_game):
        super.__init__()
        self.screen = ai_game.screen

        self.image = pygame.image.load('images/gold_star.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)


if __name__ == '__main__':
    # make a game instance and run the game.
    ai = Stars()
    ai.run_game()
