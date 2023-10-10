import pygame.font
from pygame.sprite import Group

from bluealienship import Bluealienship

class Bluescoreboard:
    """"A Simple class for scoreboard."""

    def __init__(self, blue_ai): 
        """Initialize the scoreboard"""
        self.blue_ai = blue_ai
        self.screen = blue_ai.screen
        self.screen_rect = blue_ai.screen.get_rect()
        self.settings = blue_ai.settings
        self.stats = blue_ai.stats

        # Font settings for scoring information 
        self.font = pygame.font.SysFont(None, 30) 
        self.text_color = (255,255,255)

        # Prepare the initial score image 
        self.prep_score() 
        self.prep_highest_score()
        self.prep_ships()

    def prep_score(self): 
        """"Turn the Score into rendered image"""
        rounded_score = round(self.stats.score, -1)
        score_str = f"Current Score: {rounded_score:,}"
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        #Display the score at the top right of the screen 
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right= self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_highest_score(self): 
        """Turn highest score into rendered image"""
        highest_rounded_score = round(self.stats.highest_score, -1)
        highest_score_str = f"Highest Score:{highest_rounded_score:,}"
        self.highest_score_image = self.font.render(highest_score_str,True, self.text_color, self.settings.bg_color)
        
        #Display the highest score at the top of the screen
        self.highest_score_rect = self.highest_score_image.get_rect() 
        self.highest_score_rect.midtop= self.screen_rect.midtop 
        self.highest_score_rect.top = 20
    
    def check_highest_score(self):
        """Check to see if there is a highest score"""
        if self.stats.score > self.stats.highest_score:
            self.stats.highest_score = self.stats.score
            self.prep_highest_score()

    def prep_ships(self): 
        """"Show how many ships are left"""
        self.ships = Group()
        for ship_number in range(self.stats.ship_lives):
            ship = Bluealienship(self.blue_ai)
            ship. rect.x = 10 + ship_number * ship.rect.width 
            ship.rect.y = 10

              # Resize the ship life image here
            small_ship_image = pygame.transform.scale(ship.image, (30, 30))  # Replace desired_width and desired_height
            ship.resized_image = small_ship_image
            self.ships.add(ship)



    def show_score(self): 
        """Draw Score to the screem"""
        self.screen.blit(self.score_image, self.score_rect)
        self.check_highest_score()
        self.screen.blit(self.highest_score_image, self.highest_score_rect)
        #self.ships.draw(self.screen)

        for ship in self.ships:
            self.screen.blit(ship.resized_image, ship.rect)

    def reset_score(self): 
        """Reset Score to 0"""
        self.stats.reset_stats()
        self.prep_score() 
        self.prep_ships()
        self.show_score() 
