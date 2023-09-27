import pygame


class Bluealienship:
    """A class to mange the dogeship."""

    def __init__(self, blue_ai_game):
        """Initialize the dogeship and set it starting position."""
        self.screen = blue_ai_game.screen
        self.settings = blue_ai_game.settings
        self.screen_rect = blue_ai_game.screen.get_rect()

        # Load the ship image and ge it rect
        self.image = pygame.image.load(
            "/Users/alexchen/Desktop/Python Crash Course /Image/spiked ship 3. small.blue_.PNG"
        )
        # Loading ship size
        self.new_size = blue_ai_game.settings.ship_size
        self.resized_image = pygame.transform.scale(self.image, self.new_size)
        self.rect = self.resized_image.get_rect()
        self.rect.midtop = self.screen_rect.midtop

        # start each new dogeship at the bottom of th center
        self.rect.midbottom = self.screen_rect.midbottom

        # Smoother movement by change the speed to float.
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # setting up moving flags
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update the ship movement based the moving flags"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.settings.screen_height:
            self.y += self.settings.ship_speed

        # Update Rect object from self.x
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Draw the dogeship at the current location"""
        self.screen.blit(self.resized_image, self.rect)
