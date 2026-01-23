import pygame
import sys

# Initialize Pygame
pygame.init()

# --- Configuration ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
BG_COLOR = (30, 30, 30) # Dark gray background

# Create the display screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Sprites & Controls")

# Clock for controlling frame rate
clock = pygame.time.Clock()

# --- Sprite Class ---
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Create a surface for the sprite (width, height)
        self.image = pygame.Surface([50, 50])
        self.image.fill((0, 128, 255)) # Blue color
        # Get the rectangle object that has the dimensions of the image
        self.rect = self.image.get_rect()
        # Set the initial position
        self.rect.center = (SCREEN_WIDTH // 4, SCREEN_HEIGHT // 2)
        self.speed = 5

    def update(self):
        # Get the current state of keyboard presses
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        # Keep sprite within screen bounds
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

class StaticSprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([50, 150])
        self.image.fill((255, 50, 50)) # Red color
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH * 3 // 4, SCREEN_HEIGHT // 2)

# --- Sprite Setup ---
# Create groups to hold sprites
all_sprites_list = pygame.sprite.Group()

# Create the player instance
player_sprite = Player()
all_sprites_list.add(player_sprite)

# Create the static sprite instance
static_sprite = StaticSprite()
all_sprites_list.add(static_sprite)

# --- Main Game Loop ---
running = True
while running:
    # 1. Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2. Game Logic (Update sprite positions, etc.)
    all_sprites_list.update()

    # 3. Drawing
    screen.fill(BG_COLOR) # Clear the screen with background color
    all_sprites_list.draw(screen) # Draw all sprites to the screen

    # 4. Update the display (flip the buffer)
    pygame.display.flip()

    # 5. Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()