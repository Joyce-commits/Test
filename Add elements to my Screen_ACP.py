import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Create the game screen (surface)
# The screen size can be adjusted via a command-line interface on your system
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pygame Elements Example")

# --- Adding Elements ---

# 1. Add Text
font = pygame.font.SysFont('Arial', 40, bold=True)
  
# Render the text into a surface
text_surface = font.render("Welcome to Pygame!", True, WHITE)
text_rect = text_surface.get_rect(center=(SCREEN_WIDTH // 2, 50))

# 2. Define Rectangle properties
rect_width = 200
rect_height = 100
# Position the center of the rectangle
rect_x = (SCREEN_WIDTH // 2) - (rect_width // 2)
rect_y = (SCREEN_HEIGHT // 2) - (rect_height // 2)
# Create a Rect object using the coordinates and dimensions
rectangle = pygame.Rect(rect_x, rect_y, rect_width, rect_height)


# --- Game Loop ---
# This loop handles events and keeps the screen open

running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a background color first (e.g., BLACK)
    screen.fill(BLACK)

    # Draw the rectangle onto the screen surface
    pygame.draw.rect(screen, BLUE, rectangle)

    # Blit (copy) the text surface onto the main screen surface at its defined position
    screen.blit(text_surface, text_rect)

    # Update the display
    # This makes everything we've drawn visible
    pygame.display.flip()

# Quit Pygame once the loop finishes
pygame.quit()