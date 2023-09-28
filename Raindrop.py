import sys 
import pygame
from rainsetting import Rainsettings
from rain import Rain


class Raindrop: 
    """Initialize the raindrop object. """
    
    def __init__(self): 
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Rainsettings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Raindrop")

        self.rains = pygame.sprite.Group()
        self._create_raindrops()
    
    def run_game (self): 
        """Run the game. """
        while True: 
            self._check_events()
            self.rains.update()
            self._update_screen()
            self.clock.tick(60)
    
    def _check_events(self):
        """Check for events. """
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE: 
                sys.exit()
    
    def _create_raindrop(self,x_position,y_position): 
        new_raindrop = Rain(self)
        new_raindrop.y = y_position
        new_raindrop.rect.x = x_position
        new_raindrop.rect.y = y_position
        self.rains.add(new_raindrop)
    
  
    def _create_raindrops(self): 
        rain = Rain(self)
        rain_width,rain_height = rain.rect.size 

        current_x, current_y = rain_width,rain_height
        while current_y < (self.settings.screen_height /2 ): 
            while current_x < (self.settings.screen_width): 
                self._create_raindrop(current_x,current_y)
                current_x += 3 * rain_width
            
            # Finihsed a row of raindrops then reset x position. 
            current_x = rain_width 
            current_y += 3 * rain_height


    def _update_screen(self): 

        self.screen.fill(self.settings.bg_color)
        self.rains.draw(self.screen)
        pygame.display.flip()

if __name__ == "__main__": 
    r_game = Raindrop()
    r_game.run_game()

    


