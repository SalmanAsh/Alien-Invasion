import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien in the fleet"""

    def __init__(self, ai_game):
        """initialize the alien and set its current position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # load the alien image
        self.image = pygame.image.load("images/alien.png")
        self.rect = self.image.get_rect()

        # start each new alien at the top left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store alien's exact horizonatal position
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien is at the edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """Move alien to the right"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x
