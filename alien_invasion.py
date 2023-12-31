import sys

from time import sleep

import pygame

from settings import Settings

from gamestats import Gamestats

from ship import Ship

from bullet import Bullet

from alien import Alien 

from star import Star

from button import Button

from scoreboard import Scoreboard

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

        # Create an instance to store game statisitic. 
        self.stats = Gamestats(self) 
        self.scoreboard = Scoreboard(self)


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
        #self._create_stars()

         #Make the play button.

        self.play_button = Button(self,'Start Game')

        #start alien invasion in an inactive state
        self.game_active = False

       

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if self.game_active:
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

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

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
                
            self._check_bullet_alien_collision()


    def _check_bullet_alien_collision(self):
        """heck for any bullets that have hit the aliens"""
        collisions = pygame.sprite.groupcollide(
            self.bullets,self.aliens,True,True)
        
        if collisions: 
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points *len(aliens)
            self.scoreboard.prep_score()
            self.scoreboard.prep_highest_score()
        
        if not self.aliens:
            # Destroy exisiting bullets and create new fleet
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

        

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

        while current_y < (self.settings.screen_height/2):
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

        # Look for alien-ship collisions
        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            self._ship_hit()
        
        #look for aliens hitting the bottom of the screen
        self._check_aliens_bottom()

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
        
    def _ship_hit(self): 
        """Respond to the ship being hit by an alien."""
        if self.stats.ship_limit> 0:
            #decreament ship_left.
            self.stats.ship_limit -= 1
            self.scoreboard.prep_ships()

            # getrid of any remaining bullets and aliens: 
            self.bullets.empty()
            self.aliens.empty()
             
            #pause 
            sleep(3.0)

            print(f"Your ship got hit you have  {self.stats.ship_limit} ship left.")

            #create a new fleet of aliens and recenter ship 
            self._create_fleet()
            self.ship.center_ship()

        else: 
            self.game_active = False
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self): 
        """Check if any aliens have reached the bottom of the screen."""
        for alien in self.aliens.sprites(): 
            if alien.rect.bottom >= self.settings.screen_height: 
                #Treat this the same as if the ship got hit 
                self._ship_hit()
                break


    def _check_play_button(self,mouse_pos):
        """start a new game when the player clicks play."""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)

        if button_clicked and not self.game_active:
            #Reset game settings.
            self.settings.initialize_dynamic_settings()

            #reset the game statistic. 
            self.stats.reset_stats()
            self.scoreboard.prep_score()
            self.scoreboard.prep_ships()
            self.game_active = True

            # Get rid of any remaining bullets and aliens. 
            self.bullets.empty()
            self.aliens.empty()

            #create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            # Hide the mouse cursor. 
            pygame.mouse.set_visible(False)


    def _update_screen(self):
        """Update images on screen and flip to the new screen"""
        self.screen.fill(self.settings.bg_color)

        #Draw the scoreboard information 
        self.scoreboard.show_score() 
    

        #Draws the bullets
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        
        #Draws the aliens
        self.aliens.draw(self.screen)

        #draws the stars
        self.stars.draw(self.screen)

        # showing ship new position
        self.ship.blitme()

        # Draw out the play button 
        if not self.game_active:
            self.play_button.draw_button()

        # Make the most recently drawn screen visible
        pygame.display.flip()
        # controlling frame rate



if __name__ == "__main__":
    # Make a game instance, and run game.
    ai = AlienInvasion()
    ai.run_game()
