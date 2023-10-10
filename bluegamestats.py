class Bluegamestats: 
    """"Tracking the statistics of the bluealien game."""

    def __init__(self,blue_ai):
        """initalizes the statistics"""
        self.settings = blue_ai.settings
        self.reset_stats()

    def reset_stats(self):
        """Reset statisitc during game."""
        self.ship_lives = self.settings.ship_lives
        self.score = 0