'''
This file contains all objects in the game such as Player, Enemy, and all collectibles
'''

import pygame





class Player(pygame.sprite.Sprite):

    def __init__(self, width, height):
        super().__init__()

        # Create an image of the player
        self.image = pygame.Surface((width, height))
        self.image.fill(color=0)

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
