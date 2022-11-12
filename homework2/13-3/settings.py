class Settings:
    """A class to store all settings for Alie Invasion"""

    def __init__(self):
        """Init game settings
        # Screen Settings"""
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Alien settings
        self.alien_speed = 1
        self.fleet_drop_speed = 10

