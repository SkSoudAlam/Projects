import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
width = 900
height = 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simple Game")

# Set up game variables
player_size = 50
player_x = width // 2 - player_size // 2
player_y = height - player_size
player_speed = 6
bullet_size = 10
bullet_speed = 10
bullets = []
enemy_size = 50
enemy_count = 9
enemies = []
for _ in range(enemy_count):
    enemy_x = random.randint(0, width - enemy_size)
    enemy_y = 0
    enemy_speed = random.choice([3, 5])
    enemies.append((enemy_x, enemy_y, enemy_speed))
score = 0
game_over = False

# Variables to track player movement
move_left = False
move_right = False
move_up = False
move_down = False

# Game loop
clock = pygame.time.Clock()

while not game_over:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet_x = player_x + player_size // 2 - bullet_size // 2
                bullet_y = player_y
                bullets.append((bullet_x, bullet_y))
            elif event.key == pygame.K_a:
                move_left = True
            elif event.key == pygame.K_d:
                move_right = True
            elif event.key == pygame.K_w:
                move_up = True
            elif event.key == pygame.K_s:
                move_down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                move_left = False
            elif event.key == pygame.K_d:
                move_right = False
            elif event.key == pygame.K_w:
                move_up = False
            elif event.key == pygame.K_s:
                move_down = False

    # Update player position based on movement variables
    if move_left:
        player_x -= player_speed
    if move_right:
        player_x += player_speed
    if move_up:
        player_y -= player_speed
    if move_down:
        player_y += player_speed

    # Keep the player inside the game window
    player_x = max(0, min(player_x, width - player_size))
    player_y = max(0, min(player_y, height - player_size))

    # Move the bullets
    for i, bullet in enumerate(bullets):
        bullet_x, bullet_y = bullet
        bullet_y -= bullet_speed
        bullets[i] = (bullet_x, bullet_y)

        # Check for bullet collision with enemies
        for j, enemy in enumerate(enemies):
            enemy_x, enemy_y, _ = enemy
            if (
                bullet_x < enemy_x + enemy_size
                and bullet_x + bullet_size > enemy_x
                and bullet_y < enemy_y + enemy_size
                and bullet_y + bullet_size > enemy_y
            ):
                enemies.pop(j)
                score += 1

        # Remove bullets that go out of screen
        if bullet_y < 0:
            bullets.pop(i)

    # Move the enemies
    for i, enemy in enumerate(enemies):
        enemy_x, enemy_y, enemy_speed = enemy
        enemy_y += enemy_speed
        enemies[i] = (enemy_x, enemy_y, enemy_speed)

        # Check for collision
        if (
                player_x < enemy_x + enemy_size
                and player_x + player_size > enemy_x
                and player_y < enemy_y + enemy_size
                and player_y + player_size > enemy_y
        ):
            game_over = True

        # Check if enemy reaches the bottom
        if enemy_y > height:
            enemy_x = random.randint(0, width - enemy_size)
            enemy_y = 0
            enemy_speed = random.choice([3, 5])
            enemies[i] = (enemy_x, enemy_y, enemy_speed)

    # If all enemies are eliminated, add a new enemy
    if not enemies:
        enemy_x = random.randint(0, width - enemy_size)
        enemy_y = 0
        enemy_speed = random.choice([3, 5])
        enemies.append((enemy_x, enemy_y, enemy_speed))

    # Draw game objects
    window.fill((0, 0, 0))  # Black background
    for enemy in enemies:
        enemy_x, enemy_y, _ = enemy
        pygame.draw.rect(window, (255, 0, 0), (enemy_x, enemy_y, enemy_size, enemy_size))  # Red enemy

    for bullet in bullets:
        bullet_x, bullet_y = bullet
        pygame.draw.rect(window, (0, 255, 0), (bullet_x, bullet_y, bullet_size, bullet_size))  # Green bullet

    pygame.draw.rect(window, (0, 255, 0), (player_x, player_y, player_size, player_size))  # Green player

    # Display the score
    font = pygame.font.Font(None, 29)
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    window.blit(score_text, (10, 10))

    pygame.display.update()
    clock.tick(60)

# Quit the game
pygame.quit()
