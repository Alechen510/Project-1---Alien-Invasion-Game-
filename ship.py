import pygame

class Ship: 
    """" A Class to mange the ship."""

    def __init__(self,ai_game): 
        """Initialize the ship and set it starting position."""
        self.screen = ai_game.screen 
        self.settings = ai_game.settings 
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load ('/Users/alexchen/Desktop/Python Crash Course /Python Crash Course Solution/chapter_12/adding_ship_image/images/ship.bmp')
        self.rect = self.image.get_rect()

        #start each new ship at the bottom center of the screen 
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a float for the ship's exact horitzontal position.
        self.x = float(self.rect.x)
        #Movement flag: Start witnh a ship that's not moving 
        self.moving_right = False
        self.moving_left = False

    def update(self): 
        """Update the ship's position based on the movement flag"""
        # Update the ship's x value, not the rect.

        if self.moving_right and self.rect.right <self.screen_rect.right: 
            self.x += self.settings.ship_speed
        if self.moving_left and  self.rect.left > 0: 
            self.x -= self.settings.ship_speed
        
        # Update rect object from self.x.
        self.rect.x = self.x


    def blitme(self): 
        """ Draw the shio at it current location."""
        self.screen.blit(self.image,self.rect)
        
        