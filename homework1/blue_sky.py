import pygame
from time import sleep

pygame.init()
screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Blu_Sky")
bg_color = (50, 50, 150)
screen.fill(bg_color)
pygame.display.flip()

sleep(10)
