"""Settings module — stores all configuration values for Alien Invasion."""

from pathlib import Path


class Settings:
    """Stores all settings for the Alien Invasion game."""

    def __init__(self) -> None:
        """Initialize the game's static settings."""

        # Screen
        self.name: str = 'Alien Invasion'
        self.screen_w: int = 1200
        self.screen_h: int = 800
        self.FPS: int = 60

        # Assets
        self.bg_file: Path = Path.cwd() / 'Assets' / 'images' / 'Starbasesnow.png'
        self.ship_file: Path = Path.cwd() / 'Assets' / 'images' / 'ship2.png'
        self.bullet_file: Path = Path.cwd() / 'Assets' / 'images' / 'laserBlast.png'
        self.laser_sound: Path = Path.cwd() / 'Assets' / 'sound' / 'laser.mp3'
        self.alien_file: Path = Path.cwd() / 'Assets' / 'images' / 'enemy_4.png'

        # Ship
        self.ship_w: int = 40
        self.ship_h: int = 60
        self.ship_limit: int = 3

        # Bullet
        self.bullet_w: int = 25
        self.bullet_h: int = 80
        self.bullet_amount: int = 6

        # Alien
        self.alien_w: int = 40
        self.alien_h: int = 40

        # Difficulty scaling
        self.speedup_scale: float = 1.1
        self.score_scale: float = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self) -> None:
        """Initialize settings that change throughout the game."""
        self.ship_speed: float = 6.0
        self.bullet_speed: float = 15.0
        self.alien_speed: float = 1.5
        self.alien_points: int = 50

    def increase_speed(self) -> None:
        """Increases  speed settings and alien point values each level."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)