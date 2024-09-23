import pygame 
import random
import time
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Title and icon
pygame.display.set_caption("This is a game i guess? :)")
icon = pygame.image.load('meme.png')
pygame.display.set_icon(icon)

# Player
PlayerImg = pygame.image.load('spaceship.png')
Scenery = pygame.image.load('meme.png')
X = 350
Y = 470
X_Change = 0
Y_Change = 0

# Enemy
EnemyImg = pygame.image.load('enemy.png')
X_ = 350
Y_ = 200
X__Change = random.randint(-3, 3)
Y__Change = random.randint(-3, 3)

def player(x, y): # Call this in the game loop
    screen.blit(PlayerImg, (x, y))

def enemy(x, y): # Call this in the game loop
    screen.blit(EnemyImg, (x, y))

def scen():
    screen.blit(Scenery, (0, 0))

# Game loop
running = True
while running:

    # RGB - Red, Green, Blue
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            print('Pressed')
            if event.key == pygame.K_LEFT:
                print('Left')
                X_Change = -6
            if event.key == pygame.K_RIGHT:
                print('Right')
                X_Change = 6
            if event.key == pygame.K_UP:
                print('Up')
                Y_Change = -6
            if event.key == pygame.K_DOWN:
                print('Down')
                Y_Change = 6

        if event.type == pygame.KEYUP:
            print('Release')
            X_Change = 0
            Y_Change = 0
    X += X_Change
    Y += Y_Change
    if X > 700: X = 700
    if X < 0: X = 0
    if Y > 500: Y = 500
    if Y < 0: Y = 0

#    X__Change = random.randint(-3, 3)
#    Y__Change = random.randint(-3, 3)
    X_ += X__Change
    Y_ += Y__Change
    if X__Change == 0 : X__Change = 1
    if Y__Change == 0 : Y__Change = 1


    if X_ > 700: X__Change = random.randint(-3, -1)
    if X_ < 0: X__Change = random.randint(1, 3)
    if Y_ > 250: Y__Change = random.randint(-3, -1)
    if Y_ < 0: Y__Change = random.randint(1, 3)

    scen()
    player(X, Y) # Put this under the screen.fill() so the computer would draw the screen first
    enemy(X_ , Y_)
    pygame.display.update() # update any change into the game loop