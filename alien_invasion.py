import sys

import pygame

from settings import Settings

from ship import Ship

from bullet import Bullet

from alien import Alien 

from star import Star

from random import randint 

class AlienInvasion:
    """Over class to manage game assets and behavoir."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        # controlling the frame rate
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        # Full Screen Mode:
        # self.screen  =pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height

        # Standard Screen Mode:
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )  ###

        # displaying the caption
        pygame.display.set_caption("Alien Invasion")

        # Setting up the ship
        self.ship = Ship(self)

        # setting up the bullets class
        self.bullets = pygame.sprite.Group()
        #setting up the aliens class
        self.aliens = pygame.sprite.Group()
        # Create new alien fleet
        self._create_fleet()

        #setting up the star class
        self.stars = pygame.sprite.Group()
        
        #Create new star fleet
        self._create_stars()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()
            self.clock.tick(60)

            # Get rid of bullets that have disappeared.

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Response to keydown event"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Response to keyup event"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        # Update bullet posiition
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        print(len(self.bullets))

    def _create_alien(self, x_position,y_position): 
        """Create a new alien and add it to the aliens group"""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)
    
    def _create_fleet(self):
        """create a new fleet of aliens"""
        #create an alien and keep adding aliens until there's not more room left
        #spacing between each alien with one alien width and one alien height
        alien = Alien(self)
        alien_width,alien_height = alien.rect.size
        current_x,current_y = alien_width, alien_height

        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x <(self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x,current_y)
                current_x += 2 * alien_width

            # Finished a row; reset x value, and icrement y value
            current_x = alien_width
            current_y += 2 * alien_height

    def _check_fleet_edges(self): 
        """respond appropriately if any alien have reached an edge of the screen"""
        for alien in self.aliens.sprites(): 
            if alien.check_edges():
                self._change_fleet_direction()
                break 

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_aliens(self):
        """Update the position of all the aliens in the fleet"""
        self._check_fleet_edges()
        self.aliens.update()
        
        for alien in self.aliens.copy():
            if alien.rect.bottom >= self.settings.screen_height:
                self.aliens.remove(alien)

    def _create_star(self,x_position, y_position):
        """"create a star and add it to the stars group"""
        new_star = Star(self)
        new_star.rect.x, new_star.rect.y = x_position, y_position
        self.stars.add(new_star)
    
    def _create_stars(self): 
        """create multiple stars in a striaght line"""
        for numbers in range (1000): 
            x_position = randint(0, self.settings.screen_width) 
            y_position = randint(0, self.settings.screen_height)

            new_star = Star(self)
            new_star.rect.x, new_star.rect.y = x_position, y_position
            self.stars.add(new_star)
        

    def _update_screen(self):
        """Update images on screen and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)

        #Draws the bullets
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        
        #Draws the aliens
        self.aliens.draw(self.screen)

        #draws the stars
        self.stars.draw(self.screen)

        # showing ship new position
        self.ship.blitme()

        # Make the most recently drawn screen visible
        pygame.display.flip()
        # controlling frame rate


if __name__ == "__main__":
    # Make a game instance, and run game.
    ai = AlienInvasion()
    ai.run_game()
