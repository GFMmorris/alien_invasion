import pygame
from time import sleep

pygame.init()
pygame.display.set_mode((800, 600))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            print(event.key)
        else:
            continue
        # moment = pygame.event.key
