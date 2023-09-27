import pygame
from pygame.sprite import Sprite


class Alienshipbullet(Sprite):
    """ "A Class for manging alien bullets"""

    def __init__(self, blue_ai,x_offset, y_offset):
        """Create a bullet object at the ship's current position"""
        #inherit from blue_ai class
        super().__init__()
        self.screen = blue_ai.screen
        self.settings = blue_ai.settings

        # Loading up bullet image 
        self.bullet_image = pygame.image.load(
            "/Users/alexchen/Desktop/Python Crash Course /Image/laserBullet.png"
        )
        # Loading bullet size and image size
        self.new_size = blue_ai.settings.bullet_size
        self.resized_bullet_image = pygame.transform.scale(
            self.bullet_image, self.new_size
        )

        # setting up bullet align with spaceship
        self.rect = self.resized_bullet_image.get_rect()

        # Calculate the bullet's position based on the ship
        self.rect.midtop = (blue_ai.ship.rect.midtop[0] + x_offset, blue_ai.ship.rect.midbottom[1]+ y_offset)

        # Store the bullet's position as a float
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen"""
        # Update the exact position of the bullet.
        self.y -= self.settings.bullet_speed
        # Update  the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen"""
        self.screen.blit(self.resized_bullet_image, self.rect)

