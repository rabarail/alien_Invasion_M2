"""Project Naming: Alien Invasion
Author: Rajani Baraili
Purpose: A space shooter game built with Python and Pygame where the player
    controls a ship at the left edge of the screen, moves in all four
    directions, and fires horizontal laser bullets to destroy incoming aliens.
Starter code: None
Date: April 12, 2026
"""

import sys
import pygame
from setting import Settings
from ship import Ship
from arsenal import Arsenal
from alien import Alien
from game_stats import GameStats
from button import Button, GameOverLabel
from scoreboard import Scoreboard


class AlienInvasion:
    """Manages the Alien Invasion game, screen, and main loop."""

    def __init__(self) -> None:
        """Initialize the game, screen, settings, sound, ship, and fleet."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_w, self.settings.screen_h)
        )
        pygame.display.set_caption(self.settings.name)

        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(
            self.bg, (self.settings.screen_w, self.settings.screen_h)
        )

        self.running: bool = True
        self.clock = pygame.time.Clock()

        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound(self.settings.laser_sound)
        self.laser_sound.set_volume(0.4)

        # Stats must be created before ship and fleet
        self.stats = GameStats(self)

        self.ship = Ship(self, Arsenal(self))

        # Alien fleet
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

        # UI elements
        self.play_button = Button(self, 'Play')
        self.game_over_label = GameOverLabel(self)
        self.hud = Scoreboard(self)

        # Game starts inactive — waiting for Play button
        self.stats.game_active = False
        pygame.mouse.set_visible(True)

    def _create_fleet(self) -> None:
        """Create a fleet of aliens on the right side of the screen."""
        alien = Alien(self)
        alien_w = alien.rect.width
        alien_h = alien.rect.height

        available_h = self.settings.screen_h - 2 * alien_h
        num_rows = available_h // (2 * alien_h)

        available_w = self.settings.screen_w // 2
        num_cols = available_w // (2 * alien_w)

        for col in range(num_cols):
            for row in range(num_rows):
                self._create_alien(col, row, alien_w, alien_h)

    def _create_alien(self, col: int, row: int, alien_w: int, alien_h: int) -> None:
        """Create a single alien and place it in the fleet.

        Args:
            col: The column index of the alien in the fleet.
            row: The row index of the alien in the fleet.
            alien_w: The width of a single alien in pixels.
            alien_h: The height of a single alien in pixels.
        """
        alien = Alien(self)
        alien.rect.x = self.settings.screen_w - alien_w - (col * 2 * alien_w)
        alien.rect.y = alien_h + (row * 2 * alien_h)
        alien.x = float(alien.rect.x)
        self.aliens.add(alien)

    def run_game(self) -> None:
        """Start and maintain the main game loop."""
        while self.running:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self.ship.arsenal.update_arsenal()
                self._update_aliens()
                self._check_collisions()
            self._update_screen()
            self.clock.tick(self.settings.FPS)

    def _update_aliens(self) -> None:
        """Move all aliens and check for loss conditions."""
        self.aliens.update()
        for alien in self.aliens:
            if alien.check_edges():
                self._ship_hit()
                break
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

    def _check_collisions(self) -> None:
        """Check for bullet-alien collisions and remove hit aliens."""
        collisions = pygame.sprite.groupcollide(
            self.ship.arsenal.bullets, self.aliens, True, True
        )
        if collisions:
            for aliens_hit in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens_hit)
            if self.stats.score > self.stats.max_score:
                self.stats.max_score = self.stats.score
            if self.stats.score > self.stats.high_score:
                self.stats.high_score = self.stats.score

        if not self.aliens:
            self.ship.arsenal.bullets.empty()
            self._create_fleet()
            self.stats.level += 1
            self.settings.increase_speed()

    def _ship_hit(self) -> None:
        """Respond to ship being hit — lose a life or end game."""
        if self.stats.ships_left > 1:
            self.stats.ships_left -= 1
            self.aliens.empty()
            self.ship.arsenal.bullets.empty()
            self._create_fleet()
            self.ship.rect.midleft = self.screen.get_rect().midleft
            self.ship.x = float(self.ship.rect.x)
            self.ship.y = float(self.ship.rect.y)
            pygame.time.delay(500)
        else:
            self.stats.game_active = False
            self.stats.game_over = True
            pygame.mouse.set_visible(True)

    def _start_game(self) -> None:
        """Start or restart the game."""
        self.stats.reset_stats()
        self.settings.initialize_dynamic_settings()
        self.stats.game_active = True
        self.stats.game_over = False
        self.aliens.empty()
        self.ship.arsenal.bullets.empty()
        self._create_fleet()
        self.ship.rect.midleft = self.screen.get_rect().midleft
        self.ship.x = float(self.ship.rect.x)
        self.ship.y = float(self.ship.rect.y)
        pygame.mouse.set_visible(False)

    def _update_screen(self) -> None:
        """Redraw the background, bullets, aliens, and ship each frame."""
        self.screen.blit(self.bg, (0, 0))

        if self.stats.game_active:
            self.ship.arsenal.draw_arsenal()
            self.aliens.draw(self.screen)
            self.ship.draw()
            self.hud.draw()
        else:
            if self.stats.game_over:
                self.game_over_label.draw()
            self.play_button.draw()

        pygame.display.flip()

    def _check_events(self) -> None:
        """Listen for and respond to keyboard and window events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.play_button.check_click(pygame.mouse.get_pos()):
                    self._start_game()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event: pygame.event.Event) -> None:
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
        elif event.key == pygame.K_q:
            self.running = False
            pygame.quit()
            sys.exit()

    def _check_keyup_events(self, event: pygame.event.Event) -> None:
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


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()