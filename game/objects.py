'''
This file will be the backbone of the game. It will basically hold everything that
all the levels will need (player, enemies, obstacles, etc.)
'''


from game import display, clock
import pygame
from game.globals import *


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

    def __init__(self, start):
        super().__init__()

        # Create an image of the player
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(color=self.color)

        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()

        self.rect.x = start.x
        self.rect.y = start.y


class MovingEnemy(Enemy):
    '''
    This allows some enemies to move
    '''
    def __init__(self, start, end, velocity, direction):
        super().__init__(start)
        self.velocity = velocity
        self.direction = direction
        self.start = start
        self.end = end

    def move(self):
        ''' Only allows sideways movement at the time being '''
        if self.velocity > 0:
            if self.rect.x + self.velocity < self.end.x:
                self.rect.x += self.velocity
            else:
                self.velocity *= -1
        else:
            if self.rect.x + self.velocity > self.start.x:
                self.rect.x += self.velocity
            else:
                self.velocity *= -1


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


class Collectible(pygame.sprite.Sprite):
    '''
    Collectible items
    '''
    def __init__(self):
        super().__init__()


class Coin(Collectible):
    '''
    All coins must be collected to pass a level. Currently takes a hitbox of a rectangle, could switch it later
    '''
    width = 25
    height = 25

    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(color=BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # draws a circle for the coin
        pygame.draw.ellipse(self.image, YELLOW, (0, 0, self.width, self.height))


class Wall:
    '''
    Creates walls in the level
    '''
    width = 50
    height = 50

    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, self.width, self.height)




