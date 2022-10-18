# Start to the pygame file/window

import sys

import pygame

from settings import Settings


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

    def run_game(self):
        """Start the main loop for the game."""
        # (3)
        while True:
            # Watch the keyboard and mouse events.
            # (4)
            for event in pygame.event.get():
                # (5)
                if event.type == pygame.QUIT:
                    sys.exit()

                # Redraw the screen during each pass through the loop.
                self.screen.fill(self.settings.bg_color)

                # Make the most recently drawn screen visible.
                # (6)
                pygame.display.flip()


if __name__ == '__main__':
    # make a game instance and run the game.
    ai = AlienInvasion()
    ai.run_game()
