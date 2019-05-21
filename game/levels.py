'''
This file holds drawings for each level
W = Wall
P = Start
X = Exit
C = Coin
E = Stationary Enemy
any lowercase letter = Moving enemy start position
any other uppercase letter = Moving enemy end position (if there is no end, it will hit the wall and bounce back)

This probably isn't the best way to create levels (especially for moving enemies, but it will have to due for now)
Base Level with walls keeping player in screen:
    "WWWWWWWWWWWWWWWWWWWWWW",
    "W                    W",
    "W                    W",
    "W                    W",
    "W                    W",
    "W                    W",
    "W                    W",
    "W                    W",
    "W                    W",
    "W                    W",
    "W                    W",
    "W                    W",
    "W                    W",
    "W                    W",
    "W                    W",
    "W                    W",
    "W                    W",
    "W                    W",
    "W                    W",
    "W                    W",
    "W                    W",
    "WWWWWWWWWWWWWWWWWWWWWW",
'''



def level1() -> tuple:
    velocity_dict = {'a': 10, 'b': 5} # This dictionary keeps track of the velocity of the enemy
    level = [
    "WWWWWWWWWWWWWWWWWWWWWW",
    "WP                   W",
    "W         a    C    AW",
    "WWWWWWWWWWWWWWWWWWWW W",
    "Wb            C     BW",
    "W    C        C      W",
    "W  WWWWWWWWWWWWWWWWWWW",
    "W                   EW",
    "W                    W",
    "WWWWWWWWWWWWWWWWWWW  W",
    "W                    W",
    "W                    W",
    "W  WWWWWWWWWWWWWWWWWWW",
    "W                    W",
    "W                    W",
    "WWWWWWWWWWWWWWWWWWW  W",
    "WE                   W",
    "W                    W",
    "W  WWWWWWWWWWWWWWWWWWW",
    "W                    W",
    "W                   XW",
    "WWWWWWWWWWWWWWWWWWWWWW",
    ]
    return level, velocity_dict


