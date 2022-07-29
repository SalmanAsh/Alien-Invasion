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

    def update(self):
        """Move alien to the right"""
        self.x += self.settings.alien_speed
        self.rect.x = self.x
