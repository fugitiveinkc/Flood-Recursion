"""A set of functions that generate different types of images.  The format is in 3D numpy arrays where the 3rd dimension is an RGB coordinate"""
import numpy as np


def single_color_board(x_dim, y_dim, color):
    """Takes an x dimension and y dimension along with a 
    RGB tuple and returns a numpy array with the 3rd dimension
    set to the RGB tuple.
    """
    new_board = np.zeros((x_dim, y_dim, 3), dtype=np.int)
    new_board[:] = color
    return new_board


def single_color_board_with_tiles(x_dim, y_dim, color):
    """Takes an x dimension and y dimension along with a
    RGB tuple and returns a numpy array with the 3rd dimension
    set to the RGB tuple and random placements of block of a different color.
    """
    #0) Create board
    new_board = np.zeros((x_dim, y_dim, 3), dtype=np.int)
    new_board[:] = color
    
    #1) Create mask
    mask = np.zeros((x_dim/8,y_dim/8), dtype = np.int)
    mask[0:(x_dim/16),0:(y_dim/16)] = 1
    mask = np.tile(mask, (9, 9))
    
    #2) Loop through mask and change those colors
    for row in range(x_dim):
        for col in range(y_dim):
            if mask[row, col] == 1:
                new_board[row, col] = ((color[0]-255)%255, (color[1]-255)%255, (color[2]-255)%255)

    #3) Return board
    return new_board


def single_color_board_with_square_outline(x_dim, y_dim, color):
    """Same as single_color_board but also places an outline of a circle
    with a different color than background color."""
    pass


def striped_board(x_dim, y_dim, colors):
    """Same is single_color_board but takes a lists of potential RGB tuples
    and creates a numpy array (image) with those colors are stripes in the image.
    """
    pass   
