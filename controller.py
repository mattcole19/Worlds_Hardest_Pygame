import pygame
from collections import namedtuple


# Some colors that will be used
Color = namedtuple('Color', ['red', 'green', 'blue'])
WHITE = Color(red=255, green=255, blue=255)
BLACK = Color(red=0, green=0, blue=0)
RED = Color(red=255, green=0, blue=0)


class Player(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
        super().__init__()

        # Create an image of the player
        self.image = pygame.Surface((width, height))
        self.image.fill(color=color)

        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()


    def starting_position(self, x, y):
        '''
        This defines where the palyer will start in a level
        :param x: x position of the screen
        :param y: y position of the screen
        :return: none
        '''
        player.rect.x = x
        player.rect.y = y
        return



# Initialize Pygame
pygame.init()

# Display settings
screen_size = screen_width, screen_height = (800, 600)
display = pygame.display.set_mode(screen_size)
display.fill(color=BLACK)
pygame.display.set_caption('Welcome!')

# Create a clock for the game
clock = pygame.time.Clock()

# This is a list of all sprites in the game
all_sprites_list = pygame.sprite.Group()

# Initialize a player
player = Player(color=RED, width=50, height=50)
all_sprites_list.add(player)

player.starting_position(x=10, y=20)
# Run game until it crashes
crashed = False
while not crashed:

    # Check for any event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
            break

        # Key Movement
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                pass
            if event.key == pygame.K_RIGHT:
                pass
            if event.key == pygame.K_UP:
                pass
            if event.key == pygame.K_DOWN:
                pass

    # Draw all sprites
    all_sprites_list.draw(display)

    # Update the display
    pygame.display.update()

    # 60 frames per second
    clock.tick(60)

# Quit out of Pygame when it crashes
pygame.quit()
