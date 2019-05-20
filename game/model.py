''' This will hold everything the user sees '''

import pygame
import sys
import time
from game import display
from game.objects import *
from game.levels import *


# List of sprite groups
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
moving_enemies = pygame.sprite.Group()
level_exit = pygame.sprite.Group()
coins = pygame.sprite.Group()

# Initialize player and walls
player = Player()
walls = []


current_level = level1()
y = 0
for row in current_level:
    x = 0
    for block in row:
        if block == 'W':
            wall = Wall(x=x, y=y)
            walls.append(wall)
        x += 50
    y += 50


# Run game until it crashes
crashed = False
while not crashed:
    display.fill(color=BLACK)

    # Check for any event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Key Movement for player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move(direction='LEFT')
    if keys[pygame.K_RIGHT]:
        player.move(direction='RIGHT')
    if keys[pygame.K_UP]:
        player.move(direction='UP')
    if keys[pygame.K_DOWN]:
        player.move(direction='DOWN')

    # Check for collision between the player and the enemies
    collision = pygame.sprite.spritecollide(sprite=player, group=enemies, dokill=False)
    if collision:
        time.sleep(.5)
        player.starting_position(x=10, y=20)

    # Check to see if player made it to the end
    win = pygame.sprite.spritecollide(sprite=player, group=level_exit, dokill=False)
    if win:
        print('You win!')

    # Keeps moving enemies in action
    for enemy in moving_enemies:
        enemy.move()

    for wall in walls:
        pygame.draw.rect(display, PURPLE, wall.rect)

    collect_coins = pygame.sprite.spritecollide(sprite=player, group=coins, dokill=True)

    # Draw all sprites
    all_sprites.draw(display)

    # Update the display
    pygame.display.flip()

    # 60 frames per second
    clock.tick(FPS)

# Quit out of pygame when it crashes
pygame.quit()
sys.exit()


