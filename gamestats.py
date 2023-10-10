class Gamestats: 
    """Track statistics for Alien invasion."""

    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings
        self.reset_stats() 
        #highest score - this should never be reset
        self.highest_score = 0 

    def reset_stats(self):
        """Reset statistics during game."""
        self.ship_limit = self.settings.ship_limit
        self.score = 0
