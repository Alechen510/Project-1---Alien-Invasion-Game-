import pygame.font

class Bluescoreboard:
    """"A Simple class for scoreboard."""

    def __init__(self, blue_ai): 
        """Initialize the scoreboard"""
        self.screen = blue_ai.screen
        self.screen_rect = blue_ai.screen.get_rect()
        self.settings = blue_ai.settings
        self.stats = blue_ai.stats

        # Font settings for scoring information 
        self.font = pygame.font.SysFont(None, 48) 
        self.text_color = (255,255,255)

        # Prepare the initial score image 
        self.prep_score() 

    def prep_score(self): 
        """"Turn the Score into rendered image"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        #Display the score at the top right of the screen 
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right= self.screen_rect.right - 20
        self.score_rect.top = 20
    
    def show_score(self): 
        """Draw Score to the screem"""
        self.screen.blit(self.score_image, self.score_rect)