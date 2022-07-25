class Settings:
    """A class that stores all setting for Alien Invasion"""

    def __init__(self):
        """Initialize the game settings"""
        # Screen settings

        # display size
        self.screen_width = 1200
        self.screen_height = 800

        # initial background colour
        self.bg_color = (224, 238, 238)

        # ship settings
        self.ship_speed = 3

        # bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 8
