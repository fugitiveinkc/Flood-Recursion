'''

Objective: Create a function that generates a board to use flood recursion on.

Libraries: pygame, numpy

Notes: Need to learn how to utilize 3D arrays

'''
import numpy as np

#Primitive board.  Will update to include possible walls.

def board(x_dim, y_dim, color): #board accepts int, int and (r, g, b)
    new_board = np.zeros((x_dim, y_dim, 3), dtype=np.int)
    new_board[:] = color
    return new_board

