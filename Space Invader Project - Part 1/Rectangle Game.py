import pygame
import random
import math

# Initialize pygame
pygame.init()

# Screen settings
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rocket vs UFO")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Clock
clock = pygame.time.Clock()

# Rocket
rocket_width = 50
rocket_height = 40
rocket_x = WIDTH // 2
rocket_y = HEIGHT - 60
rocket_speed = 7

# Bullet
bullet_width = 5
bullet_height = 15
bullet_x = 0
bullet_y = rocket_y
bullet_speed = 10
bullet_state = "ready"  # ready or fire

# UFO
ufo_width = 50
ufo_height = 40
ufo_x = random.randint(0, WIDTH - ufo_width)
ufo_y = 0
ufo_speed = 3

# Font
font = pygame.font.SysFont(None, 48)

# Game Over text
def game_over():
    text = font.render("GAME OVER", True, RED)
    screen.blit(text, (WIDTH // 2 - 120, HEIGHT // 2 - 30))

# Collision detection
def is_collision(x1, y1, x2, y2):
    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return distance < 30

# Main game loop
running = True
game_over_flag = False

while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Key press
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and bullet_state == "ready":
                bullet_x = rocket_x + rocket_width // 2
                bullet_y = rocket_y
                bullet_state = "fire"

    keys = pygame.key.get_pressed()

    # Rocket movement
    if keys[pygame.K_LEFT] and rocket_x > 0:
        rocket_x -= rocket_speed
    if keys[pygame.K_RIGHT] and rocket_x < WIDTH - rocket_width:
        rocket_x += rocket_speed

    # UFO movement
    ufo_y += ufo_speed
    if ufo_y > HEIGHT:
        game_over_flag = True

    # Bullet movement
    if bullet_state == "fire":
        pygame.draw.rect(screen, RED, (bullet_x, bullet_y, bullet_width, bullet_height))
        bullet_y -= bullet_speed
        if bullet_y < 0:
            bullet_state = "ready"

    # Collision
    collision = is_collision(ufo_x, ufo_y, bullet_x, bullet_y)
    if collision:
        bullet_state = "ready"
        ufo_x = random.randint(0, WIDTH - ufo_width)
        ufo_y = 0

    # Draw rocket and UFO
    pygame.draw.rect(screen, (0, 0, 255), (rocket_x, rocket_y, rocket_width, rocket_height))
    pygame.draw.rect(screen, (0, 255, 0), (ufo_x, ufo_y, ufo_width, ufo_height))

    # Game Over
    if game_over_flag:
        game_over()
        pygame.display.update()
        pygame.time.delay(3000)
        break

    pygame.display.update()
    clock.tick(60)

pygame.quit()
