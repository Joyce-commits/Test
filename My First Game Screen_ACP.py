import pygame

#Initialize Pygame and screen dimension
pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500

# Initialize display surface and set title
display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def game_loop():
	
	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
    

if __name__ == '__main__':
    game_loop()