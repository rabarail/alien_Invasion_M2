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
        self.ship_speed = 6
        #Bullet
        self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'laserBlast.png'
        self.laser_sound = Path.cwd() / 'Assets' / 'sound' / 'laser.mp3'
        self.bullet_speed = 15
        self.bullet_w = 25
        self.bullet_h = 80
        self.bullet_amount = 6

