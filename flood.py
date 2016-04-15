"""Perform flood algorithms on numpy arrays."""
import numpy


def flood_fill(array, start_pos, fill_value):
    """Fill contiguous region of an array with a new value"""
    for row, col in flood_select(array, start_pos):
        array[row][col] = fill_value


def _valid_neighbors(array, position):
    """Return neighbors of a position that are inside the array."""
    row, col = position
    num_rows, num_cols = array.shape[:2]
    neighbors = []
    for row_delta, col_delta in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
        new_row, new_col = row + row_delta, col + col_delta
        if new_row >= 0 and new_row < num_rows:
            if new_col >= 0 and new_col < num_cols:
                neighbors.append((new_row, new_col))
    return neighbors


def recursive_flood_select(array, start_pos, selected=None):
    """Return list of positions in order that they will be flood-filled

    This implementation is recursive so it will be extremely limited!
    """
    if selected is None:
        selected = [[False for _ in array[0]] for _ in array]

    num_rows = len(array)
    num_cols = len(array[0])
    row, col = start_pos
    selected[row][col] = True
    rest = []
    for delta_row, delta_col in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        new_row = row + delta_row
        new_col = col + delta_col
        in_array = (new_row >= 0 and new_row < num_rows and
                    new_col >= 0 and new_col < num_cols)
        # Is this a valid, unvisited neighbor?
        if in_array and not(selected[new_row][new_col]):
            # Does the neighbor have the same value?
            if array[row][col].all() == array[new_row][new_col].all():
                new_pos = (new_row, new_col)
                rest.extend(recursive_flood_select(array, new_pos, selected))
    return [start_pos] + rest


def flood_select(array, start_pos):
    """Return list of positions in order that they will be flood-filled

    Stack-based implementation- keep track of which locations still need to be
    processed on a stack.
    """
    stack = [start_pos]
    target_color = array[start_pos]
    selection = []
    visited = numpy.zeros(array.shape[:2], dtype=numpy.bool8)

    # Pop from stack and push neighbors on until it's empty
    while stack:
        #print "stack: {}".format(stack)
        current_pos = stack.pop()
        color_matches = (array[current_pos] == target_color).all()
        if color_matches and not(visited[current_pos]):
            selection.append(current_pos)
            stack.extend(_valid_neighbors(array, current_pos))
        visited[current_pos] = True
    return selection


def test_recursive_iterative_flood_select():
    """Make sure recursive and iterative flood select have the same results"""
    pass
