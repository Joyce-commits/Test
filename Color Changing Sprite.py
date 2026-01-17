import pygame

def main():
    pygame.init()
    width, height = 500, 500
    screen = pygame.display.set_mode((width, height))
    
    # Mapping of color names to RGB values
    colors = {
        'red':pygame.Color('red'),
        'green':pygame.Color('green'),
        'blue':pygame.Color('blue'),
        'yellow':pygame.Color('yellow'),
        'white':pygame.Color('white')
    }
    
    current_color = colors['white']
    
    x,y = 30,30
    sprite_w, sprite_h = 60,60
    
    clock = pygame.time.Clock()
    
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT]:
            x = x - 3
        if pressed[pygame.K_RIGHT]:
            x = x + 3
        if pressed[pygame.K_UP]:
            y = y - 3
        if pressed[pygame.K_DOWN]:
            y = y + 3
            
        x = min(max(0, x), width - sprite_w)
        y = min(max(0, y), height - sprite_h)
        
        # Change color based on boundary contact
        if x == 0:
            current_color - colors['white']
        elif x == width - sprite_w:
            current_color = colors['yellow']
        elif y == 0:
            current_color - colors['red']
        elif y == height - sprite_h:
            current_color = colors['green']
        else:
            current_color = colors['white']  
            
        screen.fill((0,0,0))
        pygame.draw.rect(screen, current_color, (x,y, sprite_w, sprite_h))
        
        pygame.display.flip()
        clock.tick(90)
        
    pygame.quit()


if __name__ == "__main__":
    main()
    
        
        
        
            
        
            
        
    