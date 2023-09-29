class Settings:
    """A class to store all setting for Alien Invasion."""

    def __init__(self):
        """Initialize the game's setting"""
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        black = (0, 0, 0)
        white = (255, 255, 255)
        Gray = (128, 128, 128)
        self.bg_color = black
        

        # Ship settings
        self.ship_speed = 1.5

        # Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        #fleet_direction of 1 represent right: -1 represents left 
        self.fleet_direction = 1
    