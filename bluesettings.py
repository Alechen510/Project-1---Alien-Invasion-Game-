import pygame

class Bluesettings:
    """A Class to store all setting for Blue Alien Invasion."""

    def __init__(self):
        """Initialize the game's setting."""
        # Screen settings
        self.screen_width = 1300
        self.screen_height = 1000
        self.bg_color = (0, 0, 0)
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height)
        )
        #Screen background 
        self.image = pygame.image.load("/Users/alexchen/Desktop/Python Crash Course /Image/spr_stars01.png").convert()
        self.background_image = pygame.transform.smoothscale(self.image, (self.screen_width, self.screen_height))
        
        # Ship settings
        self.ship_speed = 5.5
        self.ship_size = (80, 80)
        self.ship_lives = 3

        # Bullet settings
        self.bullet_width = 4
        self.bullet_height = 10
        self.bullet_size = (100, 100)
        self.bullet_speed = 15.5

        # Alien settings
        self.alien_size = (50, 50)
        self.alien_speed = 1.5
        self.alien_fleet_direction = 1
        self.alien_fleet_drop_speed = 10