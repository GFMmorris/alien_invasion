class GameStats:

    def __init__(self, ai_game):
        self.ship_limit = 3
        self.reset_stats()

        self.game_active = True

    def reset_stats(self):
        self.ships_left = self.ship_limit
