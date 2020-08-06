import pygame

class Helicopter():
    """A class to manage the helicopter"""

    def __init__(self, hf_game):
        """Create the helicopter and it's starting position"""
        super().__init__()
        self.screen = hf_game.screen
        self.screen_rect = hf_game.screen.get_rect()
        self.settings = hf_game.settings
        
        # load the helicopter and its rect
        self.image = pygame.image.load("part2_projects\project1_alien_invasion\TRY\images\player.bmp")
        self.rect = self.image.get_rect()

        # Start a new ship on the center of the screen
        self.rect.center = self.screen_rect.center

        # Store a decimal value for the helicopter's position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Movement flags
        self.moving_up = False
        self.moving_right = False
        self.moving_down = False
        self.moving_left = False
        self.orientation = "Left"

   
    def update(self):
        """Update the helicopter's position based on movement"""
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.helicopter_speed
        elif self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.helicopter_speed
        elif self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.helicopter_speed
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.settings.helicopter_speed
        
        self.rect.x = self.x
        self.rect.y = self.y


    def blit_me(self):
        """Draw the helicopter at its current position"""
        if self.orientation == "Left":
            self.screen.blit(self.image, self.rect)
        elif self.orientation == "Right":
            self.screen.blit(pygame.transform.flip(self.image, True, False), self.rect)
