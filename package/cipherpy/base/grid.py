import string
import numpy as np
from math import sqrt

# Playfair helper functions

# Make a grid from an alphabet

def create_grid(alphabet=string.ascii_lowercase.replace('j','')):
    grid_size = sqrt(len(alphabet))
    if grid_size % 1 != 0:
        raise Exception(f"Length, {len(alphabet)}, of given alphabet is not a square number " + 
                            "so a grid cannot be made")
    if len(set(list(alphabet))) != len(alphabet):
        raise Exception("Duplicate characters found in given alphabet.")
    grid_size = int(grid_size)
    grid = np.array(list(alphabet)).reshape((grid_size, grid_size))
    return grid

# Take a digram and encrypt it with playfair rules using a grid

def playfair_digram_encode(digram, grid):
    if len(digram) != 2:
        raise Exception(f"Input, {digram}, not two characters long.")
    grid_size = grid.shape[0]
    if grid.ndim != 2 or grid_size != grid.shape[1]:
        raise Exception(f"Given grid with dimensions {grid.shape} is not of equal dimensions.")
    if digram[0] not in grid or digram[1] not in grid:
        raise Exception(f"One or both of the characters in input {digram} not found in the given grid.")
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
