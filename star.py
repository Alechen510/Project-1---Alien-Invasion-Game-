import pygame
from pygame.sprite import Sprite

class Star(Sprite):
    """A class to represent a star in the game."""
    def __init__(self, ai_game):
        """Initialize the star object."""
        super().__init__()
        self.screen = ai_game.screen

        #load the star image and set it rect attributes
        self.image = pygame.image.load("/Users/alexchen/Desktop/Python Crash Course /Image/star_4.png")
        # setting the image as get_rect() method
        self.rect = self.image.get_rect()
        #setting the position as rect. x and y attributes
        self.rect.x, self.rect.y = self.rect.size
