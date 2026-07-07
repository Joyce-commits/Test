import math
import random
import pygame

# Initialize Pygame
pygame.init()

# Create Screen
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# title of the screen
pygame.display.set_caption("Space Invader")

# Background
bg_load = pygame.image.load("background.png").convert()
background = pygame.transform.scale(bg_load, (SCREEN_WIDTH, SCREEN_HEIGHT))

#--------------------------------------------------------------------------------
# player
player_width = 150
player_height = 150
PLAYER_START_X = 300
PLAYER_START_Y = 400
playerX = PLAYER_START_X
playerY = PLAYER_START_Y
playerX_change = 0
player = pygame.image.load("player.png").convert_alpha()
playerImage = pygame.transform.scale(player, (player_width, player_height))

# method to place the player
def player(x, y):
    # Draw the player on the screen
    screen.blit(playerImage, (x, y))

#----------------------------------------------------------------------------------
# Bullet
BULLET_SPEED_Y = 5
bullet_width = 50
bullet_heigth = 50
bullet = pygame.image.load("bullet.png").convert_alpha()
bulletImg = pygame.transform.scale(bullet, (bullet_width, bullet_heigth))
bulletX = 0
bulletY = PLAYER_START_Y
bulletX_change = 0
bulletY_change = BULLET_SPEED_Y
bullet_state = "ready"

# method to fire the bullet
def fire_bullet(x, y):
    # Fire a bullet from the player's position
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 40, y + 10))
#-----------------------------------------------------------------------------------------

# Enemy
enemy_width = 50
enemy_heigh = 50
enemyload = pygame.image.load('enemy.png').convert_alpha()
enemy= pygame.transform.scale(enemyload, (enemy_width,enemy_heigh))
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 5
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 4

for _i in range(num_of_enemies):
    enemyImg.append(enemy)
    enemyX.append(random.randint(0, SCREEN_WIDTH - 20))  # 64 is the size of the enemy
    enemyY.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)

def enemy(x, y, i):
    # Draw an enemy on the screen
    screen.blit(enemyImg[i], (x, y))


   
#-----------------------------------------------------------------------------------------

# Game Over Text
over_font = pygame.font.Font('freesansbold.ttf', 64)

def game_over_text():
    # Display the game over text
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))
    
#---------------------------------------------------------------------------------------

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10



def show_score(x, y):
    # Display the current score on the screen.
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))
    
#--------------------------------------------------------------------------------------
COLLISION_DISTANCE = 27

def isCollision(enemyX, enemyY, bulletX, bulletY):
    # Check if there is a collision between the enemy and a bullet
    distance = math.sqrt((enemyX - bulletX) ** 2 + (enemyY - bulletY) ** 2)
    return distance < COLLISION_DISTANCE

#-------------------------------------------------------------------------------------
running = True
while running:
    
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    
    # Key press event
    
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
            
    # fire the bullet
    if bulletY <= 0:
        bulletY = PLAYER_START_Y
        bullet_state = "ready"
    elif bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
    
    #Enemy Movement
    for i in range(num_of_enemies):
        if enemyY[i] > 340:  # Game Over Condition
            for j in range(num_of_enemies):
                enemyY[j] = 1500
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0 or enemyX[i] >= SCREEN_WIDTH - 64:
            enemyX_change[i] *= -1
            enemyY[i] += enemyY_change[i]
            
        # Collision Check
        if isCollision(enemyX[i], enemyY[i], bulletX, bulletY):
            bulletY = PLAYER_START_Y
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0, SCREEN_WIDTH - 64)
            enemyY[i] = random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX)
            
            
        enemy(enemyX[i], enemyY[i], i)
        
        
    # Player Movement
    playerX += playerX_change
    playerX = max(0, min(playerX, SCREEN_WIDTH - 64))  # 64 is the size of the player
    
    player(playerX, playerY)
    show_score(textX, textY)

    pygame.display.update()
