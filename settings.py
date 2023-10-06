class Settings:
    """A class to store all setting for Alien Invasion."""

    def __init__(self):
        """Initialize the game's setting"""
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        black = (0, 0, 0)
        white = (255, 255, 255)
        Gray = (230, 230, 230)
        self.bg_color = Gray
        

        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 1

        # Bullet settings
        self.bullet_speed = 2.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255,0, 60)
        self.bullets_allowed = 5

        # alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 1.5
        #fleet_direction of 1 represent right: -1 represents left 
        self.fleet_direction = 1


        # How quick the game speed up 
        self.speedup_scale = 1.1
    
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize dynamic settings that change thorughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 2.5
        self.alien_speed = 1.0

        #fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

    def increase_speed(self): 
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale