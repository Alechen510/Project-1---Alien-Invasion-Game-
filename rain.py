import pygame
from pygame.sprite import Sprite

class Rain(Sprite):
    """ A class to represent raindrop effect."""

    def __init__(self,r_game):
        """Initialize the rain."""
        super().__init__()
        self.screen = r_game.screen
        self.settings = r_game.settings

        # Load the image 
        self.image = pygame.image.load("//Users/alexchen/Desktop/Python Crash Course /Python Crash Course Solution/solution_files/chapter_13/ex_13_3_raindrops/images/raindrop.png")
        self.rect = self.image.get_rect()

        # starting positon of the rain 
        self.rect.x, self.rect.y = self.rect.width, self.rect.height

        self.y = float(self.rect.y)

    def update(self): 
        self.y += self.settings.raindrop_speed
        self.rect.y = self.y