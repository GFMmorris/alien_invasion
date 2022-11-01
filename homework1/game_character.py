import pygame


class Chara():
    def __init__(self, screen, image_address):

        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = pygame.image.load(image_address)
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center

