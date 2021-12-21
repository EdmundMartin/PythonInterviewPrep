from typing import List


def remove_islands(matrix: List[List[int]]) -> List[List[int]]:
    connected_to_border = [[False for col in matrix[0]] for row in matrix]

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            row_is_border = row == 0 or row == len(matrix) - 1
            col_is_border = col == 0 or col == len(matrix[row]) - 1
            is_border = row_is_border or col_is_border

            # Only check if row/col if is border - we search out from the borders marking neighbors
            if not is_border:
                continue
            if matrix[row][col] != 1:
                continue

            find_locations_connected_to_border(matrix, row, col, connected_to_border)

    for row in range(1, len(matrix) - 1):
        for col in range(1, len(matrix[row]) - 1):
            if connected_to_border[row][col]:
                continue
            matrix[row][col] = 0

    return matrix


def find_locations_connected_to_border(matrix, start_row, start_col, connected_to_border):
    stack = [(start_row, start_col)]

    while len(stack) > 0:
        current_position = stack.pop()
        current_row, current_col = current_position

        already_visited = connected_to_border[current_row][current_col]
        if already_visited:
            continue

        connected_to_border[current_row][current_col] = True

        neighbors = get_neighbors(matrix, current_row, current_col)
        for neighbor in neighbors:
            row, col = neighbor

            if matrix[row][col] != 1:
                continue

            stack.append(neighbor)


def get_neighbors(matrix, row, col):
    neighbors = []
    num_rows = len(matrix)
    num_cols = len(matrix[row])

    if row - 1 >= 0:  # UP
        neighbors.append((row - 1, col))
    if row + 1 < num_rows:  # DOWN
        neighbors.append((row + 1, col))
    if col - 1 >= 0:  # LEFT
        neighbors.append((row, col - 1))
    if col + 1 < num_cols:  # RIGHT
        neighbors.append((row, col + 1))

    return neighbors


if __name__ == '__main__':
    test_array = [
        [1, 0, 0, 0, 0, 0],
        [0, 1, 0, 1, 1, 1],
        [0, 0, 1, 0, 1, 0],
        [1, 1, 0, 0, 1, 0],
        [1, 0, 1, 1, 0, 0],
        [1, 0, 0, 0, 0, 1]
    ]
    result = remove_islands(test_array)
    expected = [
        [1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1],
        [0, 0, 0, 0, 1, 0],
        [1, 1, 0, 0, 1, 0],
        [1, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 1],
    ]
    assert result == expected