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

def levelx() -> tuple:
    velocity_dict = {}
    level = [
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
    ]
    return level, velocity_dict


def level1() -> tuple:
    velocity_dict = {'a': 10, 'b': 5, 'd': 5} # This dictionary keeps track of the velocity of the enemy
    level = [
    "WWWWWWWWWWWWWWWWWWWWWW",
    "WP                   W",
    "W         a    C    AW",
    "WWWWWWWWWWWWWWWWWWWW W",
    "Wb            C     BW",
    "W    dC       C     DW",
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


def level2() -> tuple:
    velocity_dict = {'a': 10, 'b': 10, 'd': 10, 'f': 10}
    level = [
    "WWWWWWWWWWWWWWWWWWWWWW",
    "WP                   W",
    "Wa                  AW",
    "Wb                  BW",
    "Wd                  DW",
    "Wf                  FW",
    "Wa                  AW",
    "Wb                  BW",
    "Wd                  DW",
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
    "W                   XW",
    "WWWWWWWWWWWWWWWWWWWWWW",
    ]
    return level, velocity_dict



