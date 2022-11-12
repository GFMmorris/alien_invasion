# Start to the pygame file/window

import sys

import pygame
from random import randint
from settings import Settings

from alien import Alien


class AlienInvasion:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize the game, and create game resources."""
        # (1)
        pygame.init()
        self.settings = Settings()

        # (2)
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Raindrops")

        self.aliens = pygame.sprite.Group()

        self._create_fleet()


    def run_game(self):
        """Start the main loop for the game."""
        # (3)
        while True:
            # Watch the keyboard and mouse events.
            # (4)
            self._check_events()

            self.aliens.update()
            self._update_screen()

    def _check_events(self):
        """Respond to key presses and mouse events."""
        for event in pygame.event.get():
            # (5)
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_q:
            sys.exit()

    def _check_bottom_alien_collisions(self):
        """Responds to bullet-alien collisions."""
        # Removes any bullets and aliens that have collided.
        collisions = pygame.sprite.groupcollide(self.screen.rect.bottom, self.aliens, True, True)
    #
    #     if not self.aliens:
    #         # destroy existing bullets and create a new fleet
    #         self.bullets.empty()
    #         self._create_fleet()

    def _update_aliens(self):
        """Update the alien position"""
        self.aliens.update()

        # look for aliens hitting the bottom of the screen.
        # self._check_aliens_bottom()

    def _create_fleet(self):
        """Create the fleet of aliens."""
        # make aliens
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # Determine the number of rows of aliens that fit on the screen.
        available_space_y = (self.settings.screen_height - (2 * alien_height))
        number_rows = available_space_y // (2 * alien_height)

        # Create one row of aliens.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                if randint(0, 100) >= 90:
                    self._create_alien(alien_number, row_number)

        print(alien_width, alien_height, number_aliens_x)

    def _create_alien(self, alien_number, row_number):
        # create an alien and place it in the row.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

    # def _check_fleet_edges(self):
    #     """Respond appropriately should you bump into a wall with a spaceship-"""
    #     for alien in self.aliens.sprites():
    #         if alien.check_edges():
    #             self._change_fleet_direction()
    #             break
    #
    # def _check_aliens_bottom(self):
    #     """Check if any aliens have reached the bottom of the screen."""
    #     screen_rect = self.screen.get_rect()
    #
    # def _change_fleet_direction(self):
    #     # drop the entire fleet's direction
    #     for alien in self.aliens.sprites():
    #         alien.rect.y += self.settings.alien_speed
    #
    #     # this line right here is imparative if you want the fleet to change directions.
    #
    #     self.settings.fleet_direction *= -1

    def _update_screen(self):
        """Update images on te screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)
        self.aliens.draw(self.screen)

        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    # make a game instance and run the game.
    ai = AlienInvasion()
    ai.run_game()