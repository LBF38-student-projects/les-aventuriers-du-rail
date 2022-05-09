"""
Projet informatique
@author: Mathis URIEN, Kenza BELAID
"""

# Imports:
import pygame, sys
from Partie import *

pygame.init()
size = width, height = 1920 // 2, 1080 // 2
screen = pygame.display.set_mode(size)
plateau = pygame.image.load("img\carte_usa.jpg")
wagon = pygame.image.load("img\wagon_test.png")
pygame.display.set_caption("Les aventuriers du rail")
size_plateau=plateau.get_size()
# pygame.display.toggle_fullscreen()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill("grey")
    screen.blit(plateau, ((width-size_plateau[0])//2, (height-size_plateau[1])//2))
    # pygame.display.flip()
    screen.blit(wagon,(10,5))
    pygame.display.flip()
    # rect=pygame.Rect(1,1,1,1)
    # pygame.draw.rect(screen,"blue",rect)
    # pygame.display.flip()



















