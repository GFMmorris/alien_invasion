# Start to the pygame file/window

import sys

import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game, and create game resources."""
        # (1)
        pygame.init()
        self.settings = Settings()

        # (2)
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game."""
        # (3)
        while True:
            # Watch the keyboard and mouse events.
            # (4)
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        """Respond to key presses and mouse events."""
        for event in pygame.event.get():
            # (5)
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            # move the ship to the right
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # move the ship to the left
            self.ship.moving_left = True

    def _check_keyup_events(self, event):
        """respond to key releases"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            # stopping move the ship to the left
            self.ship.moving_left = False

    def _update_screen(self):
        """Update images on te screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    # make a game instance and run the game.
    ai = AlienInvasion()
    ai.run_game()
