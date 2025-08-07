import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
PLAYER_SIZE = 50
PROJECTILE_SIZE = 30
PLAYER_SPEED = 8
PROJECTILE_SPEED = 5
SPAWN_RATE = 30  # Lower number means more frequent spawns

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Set up the game window
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Block Dodge")
clock = pygame.time.Clock()

class Player:
    def __init__(self):
        self.width = PLAYER_SIZE
        self.height = PLAYER_SIZE
        self.x = WINDOW_WIDTH // 2 - self.width // 2
        self.y = WINDOW_HEIGHT - self.height - 10
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.speed = PLAYER_SPEED

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < WINDOW_WIDTH:
            self.rect.x += self.speed

    def draw(self):
        pygame.draw.rect(screen, BLUE, self.rect)

class Projectile:
    def __init__(self):
        self.width = PROJECTILE_SIZE
        self.height = PROJECTILE_SIZE
        self.x = random.randint(0, WINDOW_WIDTH - self.width)
        self.y = -self.height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.speed = PROJECTILE_SPEED

    def move(self):
        self.rect.y += self.speed

    def draw(self):
        pygame.draw.rect(screen, RED, self.rect)

def main():
    player = Player()
    projectiles = []
    score = 0
    font = pygame.font.Font(None, 36)
    
    running = True
    while running:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

        # Get keyboard input
        keys = pygame.key.get_pressed()
        player.move(keys)

        # Spawn new projectiles
        if random.randint(1, SPAWN_RATE) == 1:
            projectiles.append(Projectile())

        # Update projectiles
        for projectile in projectiles[:]:
            projectile.move()
            # Remove projectiles that are off screen
            if projectile.rect.top > WINDOW_HEIGHT:
                projectiles.remove(projectile)
                score += 1
            # Check collision with player
            if projectile.rect.colliderect(player.rect):
                running = False

        # Draw everything
        screen.fill(BLACK)
        player.draw()
        for projectile in projectiles:
            projectile.draw()

        # Draw score
        score_text = font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(60)

    # Game Over screen
    screen.fill(BLACK)
    game_over_text = font.render(f"Game Over! Final Score: {score}", True, WHITE)
    restart_text = font.render("Press SPACE to play again or ESC to quit", True, WHITE)
    screen.blit(game_over_text, (WINDOW_WIDTH//2 - game_over_text.get_width()//2, WINDOW_HEIGHT//2 - 50))
    screen.blit(restart_text, (WINDOW_WIDTH//2 - restart_text.get_width()//2, WINDOW_HEIGHT//2 + 50))
    pygame.display.flip()

    # Wait for player input after game over
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    main()  # Restart the game
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

if __name__ == "__main__":
    main() 