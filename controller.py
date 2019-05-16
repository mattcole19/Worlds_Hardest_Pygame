import pygame
from collections import namedtuple
import time


# Some namedtuples that will be used to clear things up
Color = namedtuple('Color', ['red', 'green', 'blue'])
Position = namedtuple('Position', ['x', 'y'])
Size = namedtuple('Size', ['width', 'height'])

WHITE = Color(red=255, green=255, blue=255)
BLACK = Color(red=0, green=0, blue=0)
RED = Color(red=255, green=0, blue=0)
BLUE = Color(red=0, green=0, blue=255)

# Screen Settings
SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = (800, 700)
FPS = 60

# Start and End Settings
START_SIZE = END_SIZE = Size(width=100, height=100)


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

    def starting_postion(self, x, y):
        '''
        Sets the starting postion of the player
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


# Initialize Pygame
pygame.init()


display = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption('Welcome!')

# Create a clock for the game
clock = pygame.time.Clock()

# This is a list of all sprites in the game
all_sprites_list = pygame.sprite.Group()

# List of enemies
enemies = pygame.sprite.Group()

# Initialize a player
player_start = Position(x=0, y=0)
player = Player()
all_sprites_list.add(player)
player.starting_postion(x=player_start.x, y=player_start.y)

# Initialize some enemies
enemy1 = Enemy()
enemy1.set_position(400, 300)
enemy2 = Enemy()
enemy2.set_position(200, 200)

all_sprites_list.add(enemy1, enemy2)  # May not even need this
enemies.add(enemy1, enemy2)

# hard coding the start position for now to the bottom right corner
end_position = Position(x=SCREEN_WIDTH - END_SIZE.width, y=SCREEN_HEIGHT - END_SIZE.height)
start_position = Position(x=0, y=0)

# Run game until it crashes
crashed = False
while not crashed:
    display.fill(color=BLACK)

    # Draw start and end
    pygame.draw.rect(display, WHITE, (end_position.x, end_position.y, END_SIZE.width, END_SIZE.height))
    pygame.draw.rect(display, WHITE, (start_position.x, start_position.y, START_SIZE.width, START_SIZE.height))

    # Check for any event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
            break

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
        player.starting_postion(x=10, y=20)

    # Draw all sprites
    all_sprites_list.draw(display)

    # Update the display
    pygame.display.flip()

    # 60 frames per second
    clock.tick(FPS)

# Quit out of pygame when it crashes
pygame.quit()
