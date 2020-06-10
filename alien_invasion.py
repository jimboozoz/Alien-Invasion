import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Overall Class to manager game assets and behavior"""

    def __init__(self):
        """Initialize game and create resources"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))


        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

        # Set background color
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """Start main loop for game"""
        while True:
            # Wath keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the scree during each pass throguh the loop.
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            "Make the most recently drawn screen visible"
            pygame.display.flip()


if __name__ == '__main__':
    """Make a game instance and run the game."""
    ai = AlienInvasion()
    ai.run_game()
