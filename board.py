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


def single_color_board_with_random_blocks(x_dim, y_dim, color):
    """Takes an x dimension and y dimension along with a
    RGB tuple and returns a numpy array with the 3rd dimension
    set to the RGB tuple and random placements of block of a different color.
    """
    pass


def single_color_board_with_square_outline(x_dim, y_dim, color):
    """Same as single_color_board but also places an outline of a circle
    with a different color than background color."""
    pass


def striped_board(x_dim, y_dim, colors):
    """Same is single_color_board but takes a lists of potential RGB tuples
    and creates a numpy array (image) with those colors are stripes in the image.
    """
    pass   
