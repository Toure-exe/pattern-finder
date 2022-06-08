# Project by Lorenzo Camilleri - Giulio Taralli - Ismaila Toure

import numpy as np

# Method which rotates the pattern by 90 degree.
def rotate_pattern90(pattern):
    return np.rot90(pattern)

# Method which rotates the pattern by 90 degree twice (since a rot180 doesn't exist)
def rotate_pattern180(pattern):
    return np.rot90(pattern, 2)

# Method which rotates the pattern by 90 degree three times (since a rot270 doesn't exist)
def rotate_pattern270(pattern):
    return np.rot90(pattern, 3)

