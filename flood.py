def flood_fill(array, start_pos, fill_value):
    """Fill contiguous region of an array with a new value"""
    for row, col in flood_select(array, start_pos):
        array[row][col] = fill_value


def flood_select(array, start_pos, selected=None):
    """Return list of positions in order that they will be flood-filled"""
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
            if array[row][col] == array[new_row][new_col]:
                new_pos = (new_row, new_col)
                rest.extend(flood_select(array, new_pos, selected))
    return [start_pos] + rest


def test_flood_select():
    array = [[0, 0, 1, 0, 0],
             [0, 1, 1, 1, 0],
             [1, 1, 1, 1, 1],
             [0, 1, 1, 1, 0],
             [0, 0, 1, 0, 0]]

    # start from top middle
    expected = [(0, 2), (1, 2), (1, 3), (2, 3), (2, 4), (3, 3), (3, 2), (2, 2),
                (2, 1), (1, 1), (3, 1), (2, 0), (4, 2)]
    assert flood_select(array, (0, 2)) == expected

    # start from top right
    expected = [(0, 4), (1, 4), (0, 3)]
    assert flood_select(array, (0, 4)) == expected
