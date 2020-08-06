class Settings:
    """Store all static game settings"""

    def __init__(self):
        """Static settings"""
        self.bg_color = (255, 255, 255)

    def initialize_dynamic_settings(self):
        """Settings that can change"""
        self.helicopter_speed = 2