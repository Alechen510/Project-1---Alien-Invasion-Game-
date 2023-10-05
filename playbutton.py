import pygame.font

class Playbutton: 
    """Class for play button in Blue alien game."""
    
    def __init__(self,blue_ai,msg): 
        """Initialize the play button attribute."""
        self.screen = blue_ai.screen
        self.screen_rect = self.screen.get_rect()

        #setting the dimnension of the play button 
        self.width,self.height = 200, 50
        self.button_color = (0,135,0)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None, 48)

        #Build the buttos's rect object and center it. 
        self.rect =pygame.Rect(0,0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        #The button message need to be only once 
        self._pre_message (msg)

    def _pre_message (self, msg):
        """Turn message into a rendered image and center text on the button """

        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)

        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self): 
        """Draw the button"""
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)