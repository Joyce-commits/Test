import pygame
import random

# Initialize Pygame
pygame.init()

# --- Global Variables and Constants ---
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
SCREEN_TITLE = "Sprite Color Change Custom Event"
FPS = 60

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
COLORS = [RED, GREEN, BLUE, (255, 255, 0), (0, 255, 255), (255, 0, 255)] # A list of colors

# Custom Event Declaration
# USEREVENT + 1 is a safe range for custom events
CHANGE_SPRITE_COLOR_EVENT = pygame.USEREVENT + 1

# --- Sprite Class ---
class ColorSprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x, y):
        """
        Constructor for the ColorSprite class.
        """
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Create an image of the block and fill it with a color.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)

        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

        # Set the position of the sprite
        self.rect.x = x
        self.rect.y = y
        
        self.original_color = color

    def change_color(self):
        """
        Changes the color of the sprite randomly.
        """
        new_color = random.choice(COLORS)
        # Update the surface color
        self.image.fill(new_color)
        

# --- Main Program Function ---
def main():
    # Set up the drawing window
    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    pygame.display.set_caption(SCREEN_TITLE)

    # Create the sprites
    sprite_one = ColorSprite(RED, 50, 50, 100, 200)
    sprite_two = ColorSprite(BLUE, 50, 50, 400, 200)

    # Create a group to hold all sprites
    all_sprites_list = pygame.sprite.Group()
    all_sprites_list.add(sprite_one)
    all_sprites_list.add(sprite_two)

    # Set a timer to post the custom event every 1000 milliseconds (1 second)
    pygame.time.set_timer(CHANGE_SPRITE_COLOR_EVENT, 1000)

    # Run until the user asks to quit
    running = True
    clock = pygame.time.Clock()

    while running:
        # --- Event Handling ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == CHANGE_SPRITE_COLOR_EVENT:
                # Handle the custom event
                print("Custom event triggered: Changing sprite colors!")
                for sprite in all_sprites_list:
                    sprite.change_color()

        # --- Game Logic ---
        # No additional game logic needed for this example, the event handles the change.
        all_sprites_list.update()

        # --- Drawing ---
        screen.fill(WHITE)

        # Draw all the sprites
        all_sprites_list.draw(screen)

        # Flip the display to show the new drawing
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

    # Quit Pygame
    pygame.quit()

if __name__ == "__main__":
    main()