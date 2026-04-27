from pathlib import Path

"""Stores all settings for the Alien Invasion game."""
class Settings: 

    def __init__(self) -> None:
        """Initialize the game settings with default values."""
 
        self.name: str = 'Alien Invasion'
        self.screen_w = 1200
        self.screen_h = 800
        self.FPS = 60
        self.bg_file = Path.cwd() / 'Assets' / 'images' / 'Starbasesnow.png'
        #Ship
        self.ship_file = Path.cwd() / 'Assets' / 'images' / 'ship2.png'
        self.ship_w = 40
        self.ship_h = 60
        def initialize_dynamic_settings(self) -> None:
            self.ship_speed = 6
            self.bullet_speed: float = 15.0
            self.alien_speed: float = 1.5


        self.alien_points: int = 50 #scoring  
        self.ship_limit = 3 # number of lives


        #Bullet
        self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'laserBlast.png'
        self.laser_sound = Path.cwd() / 'Assets' / 'sound' / 'laser.mp3'
        self.bullet_w = 25
        self.bullet_h = 80
        self.bullet_amount = 6
        # Aliens
        self.alien_file: Path = Path.cwd() / 'Assets' / 'images' / 'enemy_4.png'
        self.alien_w: int = 40
        self.alien_h: int = 40

        #game play
        self.speedup_scale: float = 1.0

        self.score_scale: float = 1.5
        self.initialize_dynamic_settings()





