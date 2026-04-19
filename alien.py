import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING
 
if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Alien(Sprite):

    def  __init__(self, game: 'AlienInvasion') -> None:

        self.screen = game.screen
        self.settings = game.settings
       
        # Loads and scales alien image
        self.image = pygame.image.load(self.settings.alien_file)

        self.image = pygame.transform.scale(self.image, 
                        (self.settings.alien_w, self.settings.alien_h))
        

        self.rect = self.image.get_rect()

        # Store position as float for smooth movement
        self.x = float(self.rect.x)

        def update(self) -> None:
            """Move the alien left each frame."""
            self.x -= self.settings.alien_speed
            self.rect.x = self.x

        def check_edges(self)-> bool:
            """Check if the alien has reached the left edge of the screen.
 
        Returns:
            True if the alien has reached the left edge, False otherwise.
        """
            return self.rect.left <= 0
        

