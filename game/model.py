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


def reset_sprites():
    '''
    Removes all sprites from the groups
    :return:
    '''
    all_sprites.empty()
    enemies.empty()
    moving_enemies.empty()
    coins.empty()
    level_exit.empty()
    return

def find_end(letter, grid):
    '''
    Finds the ending position for the moving enemy
    :param letter: uppercase letter
    :param grid: list of strings
    :return: ending position
    '''
    y = -BLOCK_HEIGHT
    for row in grid:
        x = -BLOCK_WIDTH
        for character in row:
            if character == letter:
                print(f'character: {character}')
                # found end postion
                end = Position(x=x, y=y)
                return end
            x += BLOCK_WIDTH
        y += BLOCK_HEIGHT
    print("Couldn't find end for enemy!")  # TODO: Make this an error


def draw_level(level, velocity_dict, xchange, ychange):
    '''
    Creates current level by parsing a list of strings. The grid starts outside of the screen to make it so the player
    can't leave the screen.
    :param moving_enemies: dict
    :param level: list
    :param xchange: int
    :param ychange: int
    :return: none
    '''
    print(moving_enemies)
    y = -BLOCK_HEIGHT
    for row in level:
        x = -BLOCK_WIDTH
        for letter in row:
            if letter == 'W':
                wall = Wall(x=x, y=y)
                walls.append(wall)
            elif letter == 'E':
                enemy = Enemy(x=x, y=y)
                all_sprites.add(enemy)
                enemies.add(enemy)
            elif letter == 'C':
                coin = Coin(x=x, y=y)
                all_sprites.add(coin)
                coins.add(coin)
            elif letter == 'X':
                exit_gate = Gate(x=x, y=y)
                all_sprites.add(exit_gate)
            elif letter == 'P':
                player.starting_position(x=x, y=y)
            elif (letter != ' ') and (letter.islower()):
                path_start = letter           # lowercase letter is start of enemy path
                path_end = letter.upper()     # uppercase letter is end of enemy path

                start = Position(x=x, y=y)
                end = find_end(letter=path_end, grid=level)
                velocity = velocity_dict[letter]
                enemy = MovingEnemy(start=start, end=end,  velocity=velocity)
                moving_enemies.add(enemy)
                enemies.add(enemy)
                all_sprites.add(enemy)

            x += xchange
        y += ychange
    all_sprites.add(player)
    return

def main():
    # pygame.mixer.music.load('background-music.wav')
    # pygame.mixer.music.play(-1)
    score = 0
    current_level = level2()

    draw_level(level=current_level[0], velocity_dict=current_level[1], xchange=BLOCK_WIDTH, ychange=BLOCK_HEIGHT)
    print(moving_enemies)


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
            reset_sprites()
            main()

        # Check to see if player made it to the end
        win = pygame.sprite.spritecollide(sprite=player, group=level_exit, dokill=False)
        if win:
            print('You win!')

        # Keeps moving enemies in action
        for enemy in moving_enemies:
            print(enemy.rect.x)
            enemy.move()

        for wall in walls:
            pygame.draw.rect(display, PURPLE, wall.rect)

        if pygame.sprite.spritecollide(sprite=player, group=coins, dokill=True):
            score += 1

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
