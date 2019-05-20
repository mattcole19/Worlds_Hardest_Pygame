import sys
import time
from game import display, clock
from game.objects import *
from game.levels import *

# List of sprite groups
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
moving_enemies = pygame.sprite.Group()
level_exit = pygame.sprite.Group()
coins = pygame.sprite.Group()

# Size of display window
DISPLAY_DIMENSIONS = display.get_size()
DISPLAY_WIDTH, DISPLAY_HEIGHT = DISPLAY_DIMENSIONS


# Initialize player and walls
player = Player()


def draw_level(level, xchange, ychange):
    '''
    Creates current level by parsing a list of strings. The grid starts outside of the screen to make it so the player
    can't leave the screen.
    :param level: list
    :param xchange: int
    :param ychange: int
    :return: none
    '''
    y = -BLOCK_HEIGHT
    for row in level:
        x = -BLOCK_WIDTH
        for block in row:
            if block == 'W':
                wall = Wall(x=x, y=y)
                walls.append(wall)
            elif block == 'E':
                enemy = Enemy(x=x, y=y)
                all_sprites.add(enemy)
                enemies.add(enemy)
            elif block == 'C':
                coin = Coin(x=x, y=y)
                all_sprites.add(coin)
                coins.add(coin)
            elif block == 'X':
                exit_gate = Gate(x=x, y=y)
                all_sprites.add(exit_gate)
            elif block == 'P':
                player.starting_position(x=x, y=y)
            x += xchange
        y += ychange
    all_sprites.add(player)
    return


def main():
    current_level = level1()

    draw_level(level=current_level, xchange=BLOCK_WIDTH, ychange=BLOCK_HEIGHT)

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
            #player.starting_position(x=10, y=20)
            main()

        # Check to see if player made it to the end
        win = pygame.sprite.spritecollide(sprite=player, group=level_exit, dokill=False)
        if win:
            print('You win!')

        # Keeps moving enemies in action
        for enemy in moving_enemies:
            enemy.move()

        for wall in walls:
            pygame.draw.rect(display, PURPLE, wall.rect)
            # if player.rect.colliderect(wall.rect):
            #     print('collision')
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


main()