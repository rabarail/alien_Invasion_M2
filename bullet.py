import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    
class Bullet(Sprite):
    """Represents a laser bullet fired horizontally from the ship."""

    def __init__(self, game:'AlienInvasion'):
        """Initializes the bullet at the tip of the ship."""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load(self.settings.bullet_file)
        self.image = pygame.transform.scale(self.image, 
            (self.settings.bullet_w, self.settings.bullet_h))
        self.image = pygame.transform.rotate(self.image, 90)
        
        self.rect =self.image.get_rect()
        self.rect.midleft = game.ship.rect.midright
        self.x = float(self.rect.x)

    def update(self):
        """Move the bullet horizontally to the right each frame."""
        self.x += self.settings.bullet_speed
        self.rect.x = self.x

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        self.screen.blit(self.image, self.rect)

       