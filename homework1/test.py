import pygame
from time import sleep

pygame.init()
pygame.display.set_mode((100, 100))
pygame.display.flip()

while True:
    moment = pygame.event.get()
    print(moment)
    sleep(2)