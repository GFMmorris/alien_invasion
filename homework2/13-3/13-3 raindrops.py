# Raindrop game file

import sys

import pygame
from random import randint
from settings import Settings
from rain import Rain

class Raindrops:

    def __init(self):

        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Rain shower")

        self.rain = pygame.sprite.Group()

    def run_game(self):
        while True:
            self._check_events()
            self._update_rain()
            self._update_screen()

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

    def _drop_rain_row(self):
        """Create a new row of drops and add it to the bullet group"""
        # if len(self.bullets) < self.settings.bullets_allowed:
        #     new_bullet = Bullet(self)
        #     self.bullets.add(new_bullet)

    def _update_bullets(self):

        # """update position of rows and get rid of old rows."""
        # # update bullets position
        # self.bullets.update()
        #
        # # get rid of bullets that have disappeared
        # for bullet in self.bullets.copy():
        #     if bullet.rect.bottom <= 0:
        #         self.bullets.remove(bullet)
        #
        # self._check_bullet_alien_collisions()
        #
        # # get rid of bullets that have hit aliens
        # #   if so, get rid of the bullet and the alien.

    def _create_rain_sheet(self):

        star = Rain(self)

        available_space_x = self.screen_width - (2 * rain_width)
        number_stars_x = available_space_x // (2 * star_width)

        available_space_y = (self.screen_height - (3 * star_height))
        number_rows = available_space_y // (2 * star_height)

        for row_number in range(number_rows):
            for star_number in range(number_stars_x):
                if randint(0, 100) >= 90:
                    self._create_star(star_number, row_number)

