# import necessary modules
import math
import random
import pygame

# Initialize Pygame
pygame.init()

# Create the screen
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Caption and Icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)

# Background
background = pygame.transform.scale(pygame.image.load('background.png').convert(),(SCREEN_WIDTH, SCREEN_HEIGHT ))

# Player
PLAYER_START_X = 370
PLAYER_START_Y = 400
player_width = 150
player_height = 150

player = pygame.image.load('player.png').convert_alpha()
playerImg = pygame.transform.scale(player, (player_width , player_height))

playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0

def player(x, y):
    # Draw the player on the screen
    screen.blit(playerImg, (x, y))


# Bullet
BULLET_SPEED_Y = 5
bullet_width = 50
bullet_heigth = 50
bullet = pygame.image.load('bullet.png').convert_alpha()
bulletImg = pygame.transform.scale(bullet, (bullet_width,bullet_heigth ))
bulletX = 0
bulletY = PLAYER_START_Y
bulletX_change = 0
bulletY_change = BULLET_SPEED_Y
bullet_state = "ready"

def fire_bullet(x, y):
    # Fire a bullet from the player's position
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

#Game loop
running = True
while running:
    screen.blit(background, (0, 0))
       
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          running = False
      if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_LEFT:
              playerX_change = -2
          if event.key == pygame.K_RIGHT:
              playerX_change = 2
          if event.key == pygame.K_SPACE and bullet_state == "ready":
              bulletX = playerX
              fire_bullet(bulletX, bulletY)
              
    if event.type == pygame.KEYUP and event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
        playerX_change = 0

    # Player Movement
    playerX += playerX_change
    playerX = max(0, min(playerX, SCREEN_WIDTH - 64))  # 64 is the size of the player
    
    # Bullet Movement
    if bulletY <= 0:
        bulletY = PLAYER_START_Y
        bullet_state = "ready"
    elif bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

          
    player(playerX, playerY)
    pygame.display.update()