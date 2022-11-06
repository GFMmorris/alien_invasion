import sys
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bulltets from the ship"""

    def __init__(self, ai_game):
        """Create a bullet object at the ships """
        super().__init__()
        self.screen = ai_game.screen
        self.color = (60,60,60)

        # Create a bullet rext at (0,0_ and then set correct position.
        self.rect = pygame.Rect(0, 0, 15, 3)
        self.rect.midright = ai_game.ship.rect.midright

        # store the bullets position as a decimal value
        self.x = float(self.rect.x)

    def update(self):
        """Move the bullet up the screen."""
        #update the decimal position of the bullet
        self.x += 1.0
        #update the rect position
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
            self.y -= 2.5
        if self.moving_bottom and self.rect.bottom < self.screen_rect.bottom:
            self.y += 2.5

        # update rect object from self.x and self.y
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship att its current location."""
        self.screen.blit(self.image, self.rect)

class SidewaysShooter:

    def __init__(self):
        """Initialize the game, and create game resources."""
        # (1)
        pygame.init()

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_width = 1000
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        pygame.display.set_caption("SidewaysShooter")

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        while True:
            # Watch the keyboard and mouse events.
            # (4)
            self._check_events()
            self.ship.update()
            self._update_bullets()
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
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_screen(self):
        """Update images on te screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.bg_color)
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # Make the most recently drawn screen visible.
        pygame.display.flip()



if __name__ == '__main__':
    # make a game instance and run the game.
    ai = SidewaysShooter()
    ai.run_game()
