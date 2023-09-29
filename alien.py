import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet"""

    def __init__(self, ai_game): 
        """Initalize the alien and set its starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #load the alien image and set its rect attribute
        self.image = pygame.image.load('/Users/alexchen/Desktop/Python Crash Course /Python Crash Course Solution/chapter_13/building_alien_fleet/images/alien.bmp')
        self.rect = self.image.get_rect()

        # start each new alien on top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store the alien's exact horizaontal position
        self.x = float(self.rect.x)
    
    def check_edges(self):
        """Return true if the alien is at the edge of the screen."""
        screen_rect= self.screen.get_rect()
        return(self.rect.right >= screen_rect.right) or (self.rect.left <=0)
    
    def update(self):
        """ Move the alien right or left."""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x 
