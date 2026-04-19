import pygame
from bullet import Bullet
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    
"""Manages the collection of bullets fired by the player ship."""
class Arsenal:
    def __init__(self, game:'AlienInvasion') -> None:

        """Initialize the arsenal with an empty bullet group.
 
        Args:
            game: The main AlienInvasion game instance.
        """
        self.game = game
        self.settings = game.settings

        self.bullets = pygame.sprite.Group()

    def update_arsenal(self):
        """Move all bullets and remove any that have left the screen."""
        
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.left > self.game.settings.screen_w: 
                self.bullets.remove(bullet)
        

            
    def draw_arsenal(self):
        """Draw all active bullets to the screen."""
        for bullet in self.bullets:
            bullet.draw_bullet()

    def fire_bullet(self):
        """Create and add a new bullet if under the bullet limit.
 
        Returns:
            True if a bullet was fired, False if the limit was reached.
        """
        if len(self.bullets) < self.settings.bullet_amount:
            new_bullet = Bullet(self.game)
            self.bullets.add(new_bullet)
            return True
        return False
        

