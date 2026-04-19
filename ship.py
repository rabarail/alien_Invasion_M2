import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from arsenal import Arsenal

"""Represents the player ship on the left edge of the screen.
The ship moves in all 4 directions and fires horizontal laser bullets."""
class Ship:

    def __init__(self, game:'AlienInvasion', arsenal: 'Arsenal'):
        """Initialize the ship at the mid-left edge of the screen.
 
        Args:
            game: The main AlienInvasion game instance.
            arsenal: The Arsenal that manages the ship's bullets.
        """
         # Movement flags

        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()
        self.moving_up = False  
        self.moving_down = False
        self.moving_right = False 
        self.moving_left = False  
        
         # Load and transform ship image

        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(self.image, 
            (self.settings.ship_w, self.settings.ship_h))
        self.image = pygame.transform.rotate(self.image, -90)
        


        self.rect = self.image.get_rect()
        self.rect.midbottom = self.boundaries.midbottom
        self.rect.midleft = self.boundaries.midleft
        self.y = float(self.rect.y) 
        self.moving_right = False
        self.moving_left = False
        self.x = float(self.rect.x)

        self.arsenal = arsenal


    def update(self):
        """Update ship position in all 4 directions each frame."""

        if self.moving_up and self.rect.top > self.boundaries.top:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.boundaries.bottom:
            self.y += self.settings.ship_speed
        if self.moving_right and self.rect.right < self.boundaries.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > self.boundaries.left:
            self.x -= self.settings.ship_speed

        self.rect.y = self.y
        self.rect.x = self.x

    def draw(self):
        """Draw the ship and bullets to the screen."""
        self.screen.blit(self.image, self.rect)

    def fire(self):
         """Attempt to fire a bullet through the arsenal. 
        Returns: True if a bullet was fired, False if at the limit.
        """
         return self.arsenal.fire_bullet()
    
        
        
        
