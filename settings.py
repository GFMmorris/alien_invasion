class Settings:
    """A class to store all settings for Alie Invasion"""

    def __init__(self):
        """Init game settings
        # Screen Settings"""
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (166, 166, 166)

        # ship settings
        self.ship_speed = 1.5

        # bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

