import pygame.font

class Scoreboard: 
    """"A class to report scoring information"""

    def __init__(self, ai_game):
        """A Class to report scoring information"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Font settings for scoring information 
        self.font = pygame.font.SysFont(None, 24)
        self.text_color = (255, 255, 255)

        # Prepare the initial score image
        self.prep_score() 

    def prep_score(self):
        """Turn the Score into a rendered image"""
        score_str = str(self.stats.score)
        self.score_image= self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Display the score at the top right of the screen. 
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20 
        self.score_rect.top = 20

    def show_score(self): 
        """Draw Score to the screen"""
        self.screen.blit(self.score_image, self.score_rect)

        