import pygame
import sys
from pygame.sprite import Sprite

from random import randint


class Star(Sprite):
    """Star class"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen

        self.image = pygame.image.load('images/star.png')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)


class Stars:

    def __init__(self):
        pygame.init()

        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Stars")

        self.stars = pygame.sprite.Group()
        self._create_sky()

    def run_game(self):

        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Respond to key presses and mouse events."""
        for event in pygame.event.get():
            # (5)
            if event.type == pygame.QUIT:
                sys.exit()

    def _check_keydown_events(self, event):
        """Respond to key-presses."""
        if event.key == pygame.K_q:
            sys.exit()

    def _create_sky(self):

        star = Star(self)
        star_width, star_height = star.rect.size
        available_space_x = self.screen_width - (2 * star_width)
        number_stars_x = available_space_x // (2 * star_width)

        available_space_y = (self.screen_height - (3 * star_height))
        number_rows = available_space_y // (2 * star_height)

        for row_number in range(number_rows):
            for star_number in range(number_stars_x):
                if randint(0,100) >= 90:
                    self._create_star(star_number, row_number)

        print(star_width, star_height, number_stars_x, number_rows)

    def _create_star(self, star_number, row_number):

        star = Star(self)
        star_width, star_height = star.rect.size
        star.x = star_width + 2 * star_width * star_number
        star.rect.x = star.x
        star.rect.y = star.rect.height + 2 * star.rect.height * row_number
        self.stars.add(star)

    def _update_screen(self):
        self.screen.fill((1, 1, 1))

        self.stars.draw(self.screen)

        pygame.display.flip()


if __name__ == '__main__':
    # make a game instance and run the game.
    ai = Stars()
    ai.run_game()
