class Settings:
    "A class to store all settings for Alien Invasion."

    def __init__(self):
        """Initialize the game's static settings 
        """
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (220, 100, 100)

        # Ship settings
        self.ship_speed = 4

        # Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3