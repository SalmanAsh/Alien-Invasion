import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Overall class to manage game assets and behaviour"""

    def __init__(self):
        """Initalize the game, and create game resources"""
        pygame.init()
        self.settings = Settings()

        # display size
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        # title at the top
        pygame.display.set_caption("Alien Invasion")

        # ship element
        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        """respond to keypresses and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.type == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event_type == pygame.K_LEFT:
                    self.ship.moving_left = True

            elif event.type == pygame.KEYUP:
                if event.type == pygame.K_LEFT:
                    self.ship.moving_right = False
                elif event_type == pygame.K_LEFT:
                    self.ship.moving_left = False

    def _update_screen(self):
        # fill the background with a choosen colour once the game runs
        self.screen.fill(self.settings.bg_colour)

        # positioning the ship
        self.ship.blitme()

        # make the most recent drawn screen visible
        # fill the background with a choosen colour once the game runs
        pygame.display.flip()
        self.screen.fill(self.settings.bg_colour)

        # positioning the ship
        self.ship.blitme()

        # make the most recent drawn screen visible
        pygame.display.flip()


if __name__ == '__main__':
    # make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
