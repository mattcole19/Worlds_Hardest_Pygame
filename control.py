import pygame
from collections import namedtuple
import time


''' START GLOBAL VARIABLES '''
# Some namedtuples that will be used to clear things up
Color = namedtuple('Color', ['red', 'green', 'blue'])
Position = namedtuple('Position', ['x', 'y'])
Size = namedtuple('Size', ['width', 'height'])

# Some colors
WHITE = Color(red=255, green=255, blue=255)
BLACK = Color(red=0, green=0, blue=0)
RED = Color(red=255, green=0, blue=0)
BLUE = Color(red=0, green=0, blue=255)

# Screen Settings
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = (800, 700)
FPS = 60

# Start and End Settings
START_SIZE = END_SIZE = Size(width=100, height=100)
GATE_SIZE = START_SIZE
''' END GLOBAL VARIABLES '''


''' START SPRITE CLASSES '''
class Player(pygame.sprite.Sprite):
    color = RED
    width = 50
    height = 50

    def __init__(self):
        super().__init__()

        # Create an image of the player
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(color=self.color)

        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()

        # How fast the player can move
        self.velocity = 10

    def move(self, direction):
        '''
        Moves player on screen.  Have to enforce boundaries so player can't leave the screen.
        :param direction: LEFT, RIGHT, UP, or DOWN
        :return:
        '''

        if direction == 'LEFT':
            # Make sure player doesn't leave screen
            if (self.rect.x - self.velocity) > 0:
                self.rect.x -= self.velocity
            # Set the position so it hits the wall
            else:
                self.rect.x = 0
        if direction == 'RIGHT':
            if (self.rect.x + self.width + self.velocity) < SCREEN_WIDTH:
                self.rect.x += self.velocity
            else:
                self.rect.x = SCREEN_WIDTH - self.width
        # TODO: Fix top boundary
        if direction == 'UP':
            if (self.rect.y + self.velocity) > 0:
                self.rect.y -= self.velocity
            else:
                self.rect.y = 0
        if direction == 'DOWN':
            if (self.rect.y + self.height + self.velocity) < SCREEN_HEIGHT:
                self.rect.y += self.velocity
            else:
                self.rect.y = SCREEN_HEIGHT - self.height

        return

    def starting_position(self, x, y):
        '''
        Sets the starting position of the player
        :param x: starting x
        :param y: starting y
        :return:
        '''
        self.rect.x = x
        self.rect.y = y
        return


class Enemy(pygame.sprite.Sprite):
    color = BLUE
    width = 25
    height = 25

    def __init__(self):
        super().__init__()

        # Create an image of the player
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(color=self.color)

        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()

    # TODO: Use getters and setters ?
    def set_position(self, x, y):
        '''
        This defines where the enemies will start in a level
        :param x: x position of the screen
        :param y: y position of the screen
        :return: none
        '''
        self.rect.x = x
        self.rect.y = y
        return


class Gate(pygame.sprite.Sprite):
    '''
    Exit and Entrance to level
    '''
    width = GATE_SIZE.width
    height = GATE_SIZE.height

    def __init__(self, x, y):
        super().__init__()

        # Create the image for the gate
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(color=WHITE)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
''' END SPRITE CLASSES '''


def main():
    # Initialize pygame display
    pygame.init()
    display = pygame.display.set_mode(SCREEN_SIZE)
    pygame.display.set_caption('Welcome!')

    # Create a clock for the game
    clock = pygame.time.Clock()

    # List of sprite groups
    all_sprites = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    level_exit = pygame.sprite.Group()

    # Initialize a player
    player_start = Position(x=0, y=0)
    player = Player()
    player.starting_position(x=player_start.x, y=player_start.y)

    # Initialize some enemies
    enemy1 = Enemy()
    enemy1.set_position(400, 300)
    enemy2 = Enemy()
    enemy2.set_position(200, 200)

    # Add sprites to their corresponding groups
    all_sprites.add(enemy1, enemy2)
    enemies.add(enemy1, enemy2)

    # hard coding the start position for now to the bottom right corner (levels will be different)
    end_position = Position(x=SCREEN_WIDTH - END_SIZE.width, y=SCREEN_HEIGHT - END_SIZE.height)
    start_position = Position(x=0, y=0)

    # Start and end gates for the level
    start_gate = Gate(x=start_position.x, y=start_position.y)
    end_gate = Gate(x=end_position.x, y=end_position.y)
    all_sprites.add(start_gate, end_gate)
    level_exit.add(end_gate)

    all_sprites.add(player)  # this has to be the last sprite added in order to take priority

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

        # Draw all sprites
        all_sprites.draw(display)

        # Update the display
        pygame.display.flip()

        # 60 frames per second
        clock.tick(FPS)

    # Quit out of pygame when it crashes
    pygame.quit()
    quit()

if __name__ == '__main__':
    main()

