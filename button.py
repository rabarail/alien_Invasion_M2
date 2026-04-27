"""Button module — represents clickable buttons and labels for the game UI."""

import pygame.font


class Button:
    """Represents a clickable button displayed on the game screen."""

    def __init__(self, game, msg: str) -> None:
        """Initialize button attributes.

        Args:
            game: The main AlienInvasion game instance.
            msg: The text to display on the button.
        """
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.settings = game.settings

        self.font = pygame.font.Font(
            self.settings.font_file,
            self.settings.button_font_size
        )

        self.rect = pygame.Rect(0, 0, self.settings.button_w, self.settings.button_h)
        self.rect.center = self.boundaries.center
        self._prep_msg(msg)

    def _prep_msg(self, msg: str) -> None:
        """Render the message into an image and center it on the button.

        Args:
            msg: The text to display on the button.
        """
        self.msg_image = self.font.render(
            msg, True, self.settings.button_text_color, None
        )
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw(self) -> None:
        """Draw the button and its message to the screen."""
        self.screen.fill(self.settings.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def check_click(self, mouse_pos: tuple) -> bool:
        """Check if the button was clicked.

        Args:
            mouse_pos: The current mouse position as (x, y).

        Returns:
            True if the mouse position is within the button, False otherwise.
        """
        return self.rect.collidepoint(mouse_pos)


class GameOverLabel:
    """Displays a Game Over label above the play button."""

    def __init__(self, game) -> None:
        """Initialize the game over label.

        Args:
            game: The main AlienInvasion game instance.
        """
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.font = pygame.font.Font(
            game.settings.font_file,
            game.settings.button_font_size
        )
        self.image = self.font.render('Game Over', True, (255, 0, 0), None)
        self.rect = self.image.get_rect()
        self.rect.centerx = self.boundaries.centerx
        self.rect.centery = self.boundaries.centery - 80

    def draw(self) -> None:
        """Draw the Game Over label to the screen."""
        self.screen.blit(self.image, self.rect)