import sys

import pygame


class AlienInvasion:
    """Manage game assets and behavior"""

    def __init__(self):
        """Initialize game, create resources"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Start main loop"""
        while True:
            # Keyboard and mouse
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Make most recently drawn screen
            pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance
    ai = AlienInvasion()
    ai.run_game()
