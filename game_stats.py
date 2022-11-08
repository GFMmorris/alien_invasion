# Game Stats class
class GameStats:
    """Tracks stats for alien invasion"""

    def __init__(self, ai_game):
        """Init stats"""
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Init stats that can change during the game"""
        self.ships_left = self.settings.ship_limit
