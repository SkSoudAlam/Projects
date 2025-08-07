import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Alien Invasion")
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        
        # Create the screen surface
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        
        self.ship = Ship(self)  # Pass the AlienInvasion instance to the Ship
        
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()
            pygame.display.flip()
            self.clock.tick(60)
            
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
