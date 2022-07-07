import sys
import pygame


class AlienInvasion:
    """Overall class to manage game assets and behaviour"""

    def __init__(self):
        """Initalize the game, and create game resources"""
        pygame.init()

        # display size
        self.screen = pygame.display.set_mode((1200, 800))

        # title at the top
        pygame.display.set_caption("Alien Invasion")

        # initial background colour
        self.bg_colour = (153, 153, 153)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            # watch for keyboard and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # fill the background with a choosen colour once the game runs
            self.screen.fill(self.bg_colour)

            # make the most recent drawn screen visible
            pygame.display.flip()


if __name__ == '__main__':
    # make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
