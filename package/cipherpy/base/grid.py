import string
import numpy as np
from math import sqrt

# Playfair helper functions

# Make a grid from an alphabet

def create_grid(alphabet=string.ascii_lowercase.replace('j','')):
    grid_size = int(sqrt(len(alphabet)))
    grid = np.array(list(alphabet)).reshape((grid_size, grid_size))
    return grid

# Take a digram and encrypt it with playfair rules using a grid

def playfair_digram_encode(digram, new_txt, grid):
    grid_size = grid.shape[0]
    (y1,x1) = [int(v) for v in np.where(grid==digram[0])]
    (y2,x2) = [int(v) for v in np.where(grid==digram[1])]
    new_x1, new_x2, new_y1, new_y2 = x1,x2,y1,y2
    if x1==x2 and y1==y2:
        new_x1 = (x1 + 1) % grid_size
        new_x2 = new_x1
        new_y1 = (y1 + 1) % grid_size
        new_y2 = new_y1
    elif x1==x2:
        new_y1 = (y1 + 1) % grid_size
        new_y2 = (y2 + 1) % grid_size
    elif y1==y2:
        new_x1 = (x1 + 1) % grid_size
        new_x2 = (x2 + 1) % grid_size
    else:
        new_x1 = x2
        new_x2 = x1
    
    return str(grid[new_y1][new_x1]) + str(grid[new_y2][new_x2])
