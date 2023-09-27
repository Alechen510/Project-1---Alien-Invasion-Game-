import pygame
import sys
from rainsetting import Rainsettings

pygame.init()
settings = Rainsettings()
screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    
    pygame.display.flip()