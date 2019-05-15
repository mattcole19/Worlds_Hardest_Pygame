import pygame
from collections import namedtuple
import time



# Some colors that will be used
Color = namedtuple('Color', ['red', 'green', 'blue'])
WHITE = Color(red=255, green=255, blue=255)
BLACK = Color(red=0, green=0, blue=0)
RED = Color(red=255, green=0, blue=0)
BLUE = Color(red=0, green=0, blue=255)



class Player(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()

        # Create an image of the player
        self.image = pygame.Surface((width, height))
        self.image.fill(color=color)

        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()

        # How fast the player can move
        self.velocity = 10

    # TODO: Use getters and setters ?
    def set_position(self, x, y):
        '''
        This defines where the player will start in a level
        :param x: x position of the screen
        :param y: y position of the screen
        :return: none
        '''
        self.rect.x = x
        self.rect.y = y
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

# Display settings
screen_size = screen_width, screen_height = (800, 700)
display = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Welcome!')
FPS = 60

# Create a clock for the game
clock = pygame.time.Clock()

# This is a list of all sprites in the game
all_sprites_list = pygame.sprite.Group()

# List of enemies
enemies = pygame.sprite.Group()

# Initialize a player
player = Player(color=RED, width=50, height=50)
all_sprites_list.add(player)
player.set_position(x=10, y=20)

# Initialize some enemies
enemy1 = Enemy()
enemy1.set_position(100, 100)
enemy2 = Enemy()
enemy2.set_position(200, 200)

all_sprites_list.add(enemy1, enemy2)  # May not even need this
enemies.add(enemy1, enemy2)

# Run game until it crashes
crashed = False
while not crashed:
    display.fill(color=BLACK)

    # Check for any event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
            break

    # Key Movement for player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.rect.x -= player.velocity
    if keys[pygame.K_RIGHT]:
        player.rect.x += player.velocity
    if keys[pygame.K_UP]:
        player.rect.y -= player.velocity
    if keys[pygame.K_DOWN]:
        player.rect.y += player.velocity


    # Check for collison
    collison = pygame.sprite.spritecollide(sprite=player, group=enemies, dokill=False)
    if collison:
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
