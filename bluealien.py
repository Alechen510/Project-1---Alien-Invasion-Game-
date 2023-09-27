import pygame
from pygame.sprite import Sprite

class Bluealien(Sprite): 
    """A class for Blue alien"""

    def __init__(self,blue_ai): 
        super().__init__()
        self.screen = blue_ai.screen
        self.settings = blue_ai.settings

        #load the alien image and set its rect attribute
        self.image = pygame.image.load('/Users/alexchen/Desktop/Python Crash Course /Image/bluecargoship.png')
        #reszing the alien image 
        self.new_size = blue_ai.settings.alien_size
        self.resized_alien_image = pygame.transform.scale(self.image,self.new_size)
        
        self.rect = self.resized_alien_image.get_rect()

        #start each new alien on top left of the screen 
        # self.rect.x = self.rect.width
        # self.rect.y = self.rect.height
        self.rect.x, self.rect.y = self.rect.size

        #store the alien's horizontal position
        self.x = float(self.rect.x)

    def draw_alien(self):
        """Draw the alien on the screen"""
        self.screen.blit(self.resized_alien_image,self.rect)
