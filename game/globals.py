from collections import namedtuple
from game import display

# Some namedtuples that will be used to clear things up
Color = namedtuple('Color', ['red', 'green', 'blue'])
Position = namedtuple('Position', ['x', 'y'])
Size = namedtuple('Size', ['width', 'height'])

# Some colors
WHITE = Color(red=255, green=255, blue=255)
BLACK = Color(red=0, green=0, blue=0)
RED = Color(red=255, green=0, blue=0)
BLUE = Color(red=0, green=0, blue=255)
YELLOW = Color(red=255, green=255, blue=0)
PURPLE = Color(red=255, green=0, blue=255)

# Screen Settings
FPS = 60

# Start and End Settings
START_SIZE = END_SIZE = Size(width=100, height=100)
GATE_SIZE = START_SIZE


# This determines the 'grid layout' for each level
blocks_per_row = 20
blocks_per_column = 20
DISPLAY_WIDTH, DISPLAY_HEIGHT = display.get_size()
BLOCK_WIDTH = DISPLAY_WIDTH / blocks_per_row
BLOCK_HEIGHT = DISPLAY_HEIGHT / blocks_per_column

walls = []



