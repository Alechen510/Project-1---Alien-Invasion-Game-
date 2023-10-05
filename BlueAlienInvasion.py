import sys

import pygame

from time import sleep

from bluesettings import Bluesettings

from bluealienship import Bluealienship

from alienshipbullet import Alienshipbullet

from bluealien import Bluealien

from bluegamestats import Bluegamestats

from playbutton import Playbutton

class BlueAlienInvasion:
    """Blue Alieninvasion class with all assets"""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        # importing settings from Bluesettings
        self.clock = pygame.time.Clock()
        self.settings = Bluesettings()
        # importing modes
        self.screen = self.settings.screen

        # Create an instance of the game stats: 
        self.stats = Bluegamestats(self)

        # importing dogeship
        self.ship = Bluealienship(self)
        # import alien bullets
        self.bullets = pygame.sprite.Group()
        #Adding left and right bullet firing positions
        self.x_left_bullet_offset = 55
        self.x_right_bullet_offset = 0
        self.y_left_bullet_offset = -100
        self.y_right_bullet_offset = -100
        self.middle_bullet_x = 25
        self.middle_bellet_y = -100

        #setting up the alien class
        self.aliens = pygame.sprite.Group()
        #creating the alien fleets
        self._create_fleet()

        #make a play button
        self.play_button = Playbutton(self, 'Start Game!')

        #start game in active state
        self.game_active = False

    def run_game(self):
        """ "Starting the main loop for the game."""
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
                
                
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypress or movement on computer"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

            elif event.type  == pygame.MOUSEBUTTONDOWN: 
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
            
            

    def _check_keydown_events(self, event):
        """ "Ship Reponses to keydown events"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key==pygame.K_p:
            self.game_active = True
        elif event.key == pygame.K_ESCAPE:
            sys.exit()

    def _check_keyup_events(self, event):
        """Ship Response to keyup events"""

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False

    def _fire_bullet(self):
        """Response keydown event to fire bullets"""
        # Creating new bullets from both sides with offsets positions 

        new_bullet_left = Alienshipbullet(self, self.x_left_bullet_offset,self.y_left_bullet_offset)
        new_bullet_right = Alienshipbullet(self, -self.x_right_bullet_offset,self.y_right_bullet_offset)
        new_middle_bullet = Alienshipbullet(self, self.middle_bullet_x,self.middle_bellet_y)

        # Add both bullets to the bullets group
        self.bullets.add(new_bullet_left, new_bullet_right, new_middle_bullet)
    
    def _create_alien(self,x_position,y_position):
        """create a new alien to add to the group"""
        new_alien = Bluealien(self)
        new_alien.x= x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _create_fleet(self):
        """Create a fleet of aliens"""
        #Create an alien fleet and keep adding aliens until there isn't anymore room left
        #setting up the alien width
        alien = Bluealien(self)
        alien_width, alien_height = alien.rect.size
        current_x, current_y = alien_width, alien_height

        #while loop creating the aliens fleets
        # Outter while loop focus on y axis 
        while current_y <= (self.settings.screen_height/3):
            #inner while loop focus on x axis
            while current_x <=(self.settings.screen_width - 2* alien_width): 
                self._create_alien(current_x,current_y)
                current_x += alien_width * 2
            # finished a row; reset the x position, and increment y position
            current_x = alien_width
            current_y += 2* alien_height

    def _check_fleet_edges(self):
        """Respond to alien hitting the edge of the screen"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    
    def _change_fleet_direction(self):
        """Changing the alien fleet's direction"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.alien_fleet_drop_speed
        self.settings.alien_fleet_direction *= -1

    def _update_aliens(self):
        """Update the aliens position """
        self._check_fleet_edges()
        self.aliens.update()

        for alien in self.aliens.copy(): 
            if alien.rect.bottom >= self.settings.screen_height:
                self.aliens.remove(alien)

         # looking for alien hitting ths hip        

        if pygame.sprite.spritecollideany(self.ship,self.aliens): 
            self._ship_hit()

        #look for alien hitting the bottom of the screen

        self._check_aliens_bottom()

    def _update_bullets(self):
        """Update Position of bullets and get rid of old bullets."""
        self.bullets.update()

        "updating the bullets, and removing off the screen bullets"
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        
        #print(len(self.bullets))

        #Check for the any bullets hittings the aliens
        self._check_bullet_alien_collisions()
         
    def _check_bullet_alien_collisions(self):
        """respond to bullet hitting the alien"""
        collision = pygame.sprite.groupcollide(
            self.bullets,self.aliens,True,True)
        
        if not self.aliens:
            #Destroy exisitn bullets and create new alien fleet
            self.bullets.empty()
            self._create_fleet()
        

    def _ship_hit(self): 
        """Respsonse when ship got hit by an alien"""
        if self.stats.ship_lives > 0: 
            
            #Decrease ship's life 
            self.stats.ship_lives -= 1

            #Reset aliens and bullets
            self.bullets.empty()
            self.aliens.empty()


            #Create new aliens and recenter the ship on the screen
            self._create_fleet()
            self.ship._center_ship()

            #Pause for a few seconds
            sleep(3.0)


            #Print out a message showing how many ships left
            print("Ship hit!!")
            print(f"\nYour have {self.stats.ship_lives} ships left.")

        else:
            self.game_active = False
            pygame.mouse.set_visible(True)

    
    def _check_aliens_bottom(self):
        """ Check if any aliens have reach the bottome of the screen"""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height: 
                self.ship_hit()
                break

    
    def _check_play_button(self,mouse_pos):
        """Check if play button is pressed"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)

        if button_clicked and not self.game_active: 
            #reset the game statisitic 
            self.stats.reset_stats()
            self.game_active = True 

            #get rid of any remainning bullets and aliens 
            self.bullets.empty() 
            self.aliens.empty()

            #create a new fleet of alien 
            self._create_fleet()
            self.ship._center_ship()

            #make mouse cursor not visible when game is active
            pygame.mouse.set_visible(False)

    def _update_screen(self):
        """Update images on screen and flip to the new screen"""
        # display blue color of the screen
        self.screen.fill(self.settings.bg_color)
        self.screen.blit(self.settings.background_image,(0,0))


        # showing the bullets
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # drawing the aliens
        for alien in self.aliens.sprites():
            alien.draw_alien()
       
        # draw the ship itself
        self.ship.blitme()

        # show the play buttons
        if not self.game_active: 
            self.play_button.draw_button()
            self.aliens.empty()
            self._create_fleet()
            self.ship._center_ship()

        # make the most recent drawn screen visible
        pygame.display.flip()




if __name__ == "__main__":
    # make a game instance and run game
    blue_ai = BlueAlienInvasion()
    blue_ai.run_game()

