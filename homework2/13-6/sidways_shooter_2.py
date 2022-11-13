import sys
import pygame
from random import random
from alien import Alien
from pygame.sprite import Sprite
from game_stats import GameStats


class Bullet(Sprite):
    """A class to manage bullets from the ship"""

    def __init__(self, ai_game):
        """Create a bullet object at the ships """
        super().__init__()
        self.screen = ai_game.screen
        self.color = (60, 60, 60)

        # Create a bullet rext at (0,0) and then set correct position.
        self.rect = pygame.Rect(0, 0, 15, 3)
        self.rect.midright = ai_game.ship.rect.midright

        # store the bullets position as a decimal value
        self.x = float(self.rect.x)

    def update(self):
        """Move the bullet up the screen."""
        # update the decimal position of the bullet
        self.x += 5.5
        # update the rect position
        self.rect.x = self.x

    def draw_bullet(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)


class Ship:
    """ A class to manage the player ship."""

    def __init__(self, ai_game):
        """Init the ship and set its starting position."""
        self.screen = ai_game.screen

        self.screen_rect = ai_game.screen.get_rect()

        # load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.image = pygame.transform.rotate(self.image, 270)

        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midleft = self.screen_rect.midleft

        # store a decimal value for the ships horizontal position

        self.y = float(self.rect.y)

        # Movements flag
        self.moving_top = False
        self.moving_bottom = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        # Update the ship's x value not the rect value.

        if self.moving_top and self.rect.top > self.screen_rect.top:
            self.y -= 1.5
        if self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.y += 1.5

        # update rect object from self.x and self.y
        self.rect.y = self.y

    def center_ship(self):
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)

    def blitme(self):
        """Draw the ship att its current location."""
        self.screen.blit(self.image, self.rect)


class SidewaysShooter:

    def __init__(self):
        """Initialize the game, and create game resources."""
        # (1)
        pygame.init()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height
        self.bg_color = (230, 230, 230)
        pygame.display.set_caption("SidewaysShooter")

        self.stats = GameStats(self)

        self.alien_frequency = 0.008

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

    def run_game(self):
        while True:
            # Watch the keyboard and mouse events.
            # (4)
            self._check_events()
            if self.stats.game_active:
                self._create_alien()

                self.ship.update()
                self._update_bullets()
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
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to key presses."""

        if event.key == pygame.K_UP:
            self.ship.moving_top = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_bottom = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """respond to key releases"""
        if event.key == pygame.K_UP:
            self.ship.moving_top = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_bottom = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullet group"""
        if len(self.bullets) < 3:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """update position of bullets and get rid of old bullets."""
        # update bullets position
        self.bullets.update()

        # get rid of bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.left >= self.screen_width:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

    def _create_alien(self):
        if random() < self.alien_frequency:
            alien = Alien(self)
            self.aliens.add(alien)
            print(len(self.aliens))

    def _update_aliens(self):
        """Update alien positions, and look for collisions with ship."""
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Look for aliens that have hit the left edge of the screen.
        self._check_aliens_left_edge()

    def _check_aliens_left_edge(self):
        for alien in self.aliens.sprites():
            if alien.rect.left < 0:
                self._ship_hit()
                break

    def _ship_hit(self):
        """Respond to an alien hitting the ship."""
        if self.stats.ships_left > 0:
            # Decrement ships left.
            self.stats.ships_left -= 1

            # Get rid of any remaining aliens and bullets.
            self.aliens.empty()
            self.bullets.empty()

            # Center the ship.
            self.ship.center_ship()
        else:
            self.stats.game_active = False

    def _update_screen(self):
        """Update images on te screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.bg_color)
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)
        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    # make a game instance and run the game.
    ai = SidewaysShooter()
    ai.run_game()
