"""Project Naming:Alien Invasion
Author:  Rajani Baraili
The purpose of the program:  space shooter game built with Python and 
Pygame where the player controls a ship at the bottom of the screen, moves left and right, and fires lasers to destroy incoming aliens.
Any info about starter code : none
Date: April 12, 2026 """
import sys
import pygame
from pygame import event
from setting import Settings
from ship import Ship
from arsenal import Arsenal 

"""Main class to manage the Alien Invasion game, screen, and loop."""
class AlienInvasion:
 
    def __init__(self) -> None:
        """Initializes the game, screen, settings, sound, and ship."""
        pygame.init()
        self.settings = Settings()
        

        self.screen = pygame.display.set_mode((self.settings.screen_w, self.settings.screen_h))
        pygame.display.set_caption(self.settings.name)

        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg, (self.settings.screen_w, self.settings.screen_h))


        self.running = True
        self.clock = pygame.time.Clock()

        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound(self.settings.laser_sound)
        self.laser_sound.set_volume(0.4)


        self.ship = Ship(self, Arsenal(self))



    def run_game(self) -> None:
        """Start and maintains main game loop."""
        while self.running:
            self._check_events()
            self.ship.update()
            self.ship.arsenal.update_arsenal() 
            self._update_screen()
         
            self.clock.tick(self.settings.FPS)

    def _update_screen(self) -> None:
        """Redraw the background, ship, and bullets each frame."""
        self.screen.blit(self.bg, (0, 0))       
        self.ship.draw()
        self.ship.arsenal.draw_arsenal()
        pygame.display.flip()

    def _check_events(self) -> None:
        """Listen for and respond to keyboard and window events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event) -> None:
        """Handle key press events for ship movement and firing.
         Args:
        event: The keydown event captured by pygame.
    """
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            if self.ship.fire():
                self.laser_sound.play()
                self.laser_sound.fadeout(250)

    def _check_keyup_events(self, event) -> None:
        """Handle key release events to stop ship movement.
        Args:
        event: The keyup event captured by pygame.
    """
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
        elif event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_q:
            self.running = False
            pygame.quit()
            sys.exit()

    








if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()


