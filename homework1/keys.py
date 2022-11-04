import sys

import pygame


class Rocket:

    def __init__(self):
        """Initialize the game, and create game resources."""
        # (1)
        pygame.init()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_width = 1000
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        pygame.display.set_caption("Rocket")

    def run_game(self):
        while True:
            # Watch the keyboard and mouse events.
            # (4)
            self._check_events()
            self._update_screen()

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            # move the ship to the right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # move the ship to the left
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_top = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_bottom = True
        elif event.key == pygame.K_q:
            sys.exit()
