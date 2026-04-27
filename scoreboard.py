"""Scoreboard module — displays the HUD for the Alien Invasion game."""

import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class Scoreboard:
    """Displays the HUD showing score, high score, level, and lives."""

    def __init__(self, game: 'AlienInvasion') -> None:
        """Initialize the scoreboard with game reference.

        Args:
            game: The main AlienInvasion game instance.
        """
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = game.settings
        self.stats = game.stats

        self.font = pygame.font.Font(
            self.settings.font_file,
            self.settings.HUD_font_size
        )

    def draw(self) -> None:
        """Draw the HUD to the screen."""
        # Score - top right
        score_surf = self.font.render(
            f'Score: {self.stats.score:,}', True, self.settings.text_color
        )
        score_rect = score_surf.get_rect()
        score_rect.right = self.screen_rect.right - 10
        score_rect.top = 10
        self.screen.blit(score_surf, score_rect)

        # High score - top center
        hi_surf = self.font.render(
            f'Hi-Score: {self.stats.high_score:,}', True, self.settings.text_color
        )
        hi_rect = hi_surf.get_rect()
        hi_rect.centerx = self.screen_rect.centerx
        hi_rect.top = 10
        self.screen.blit(hi_surf, hi_rect)

        # Max score - below score
        max_surf = self.font.render(
            f'Max: {self.stats.max_score:,}', True, self.settings.text_color
        )
        max_rect = max_surf.get_rect()
        max_rect.right = self.screen_rect.right - 10
        max_rect.top = score_rect.bottom + 5
        self.screen.blit(max_surf, max_rect)

        # Level - top left
        level_surf = self.font.render(
            f'Level: {self.stats.level}', True, self.settings.text_color
        )
        level_rect = level_surf.get_rect()
        level_rect.left = 10
        level_rect.top = 10
        self.screen.blit(level_surf, level_rect)

        # Lives - ship icons below level
        self._draw_ships()

    def _draw_ships(self) -> None:
        """Draw ship icons representing remaining lives."""
        ship_image = pygame.image.load(self.settings.ship_file)
        ship_image = pygame.transform.scale(
            ship_image, (self.settings.ship_w, self.settings.ship_h)
        )
        ship_image = pygame.transform.rotate(ship_image, -90)
        for i in range(self.stats.ships_left):
            rect = ship_image.get_rect()
            rect.x = 10 + i * (self.settings.ship_w + 5)
            rect.y = 60
            self.screen.blit(ship_image, rect)