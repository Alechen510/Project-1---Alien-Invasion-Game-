import pygame.font
from pygame.sprite import Group

from ship import Ship

class Scoreboard: 
    """"A class to report scoring information"""

    def __init__(self, ai_game):
        """A Class to report scoring information"""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Font settings for scoring information 
        self.font = pygame.font.SysFont(None, 24)
        self.text_color = (255, 255, 255)

        # Prepare the initial score image
        self.prep_score() 
        self.prep_highest_score()

        # Prepare the ship lives image 
        self.prep_ships()

    def prep_score(self):
        """Turn the Score into a rendered image"""
        rounded_score = round(self.stats.score, -1)
        score_str = f"Current Score: {rounded_score:,}"
        self.score_image= self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Display the score at the top right of the screen. 
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20 
        self.score_rect.top = 20

    def prep_highest_score(self): 
        """function hat shows highest score of all time"""
        highest_score = round(self.stats.highest_score, -1)
        highest_score_str = f"Highest Score: {highest_score:,}"
        self.highest_score_image = self.font.render(highest_score_str, True, self.text_color, self.settings.bg_color)

        # Display the score at the top middle of the screen
        self.highest_score_rect = self.highest_score_image.get_rect()
        self.highest_score_rect.midtop = self.screen_rect.midtop
        self.highest_score_rect.top = 20

    def check_highest_score(self): 
        """Check to see if there's a new high score."""
        if self.stats.score > self.stats.highest_score:
            self.stats.higest_score = self.stats.score 
            self.prep_highest_score()
        

    def prep_ships(self): 
        """Show how many ships are left"""
        self.ships = Group()
        for ship_number in range(self.stats.ship_limit): 
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number*ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def show_score(self): 
        """Draw Score to the screen"""
        self.screen.blit(self.score_image, self.score_rect)
        self.check_highest_score()
        self.screen.blit(self.highest_score_image, self.highest_score_rect)
        self.ships.draw(self.screen)

        