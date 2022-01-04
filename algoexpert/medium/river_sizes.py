from typing import List, Set, Tuple


def get_successors(matrix, row, col) -> List[Tuple[int, int]]:
    max_rows = len(matrix)
    max_cols = len(matrix[row])
    successors = []
    if row + 1 < max_rows:
        successors.append((row + 1, col))
    if row - 1 >= 0:
        successors.append((row - 1, col))
    if col - 1 >= 0:
        successors.append((row, col - 1))
    if col + 1 < max_cols:
        successors.append((row, col + 1))
    return successors


def measure_river_size(
    matrix: List[List[int]], maze_cords: Tuple[int, int], seen: Set
) -> int:
    if maze_cords in seen:
        return -1
    river_size = 0
    seen.add(maze_cords)
    stack = [maze_cords]
    while stack:
        current_cords = stack.pop()
        river_size += 1
        successors = get_successors(matrix, current_cords[0], current_cords[1])
        successors = [s for s in successors if s not in seen]
        for successor in successors:
            if matrix[successor[0]][successor[1]] == 1:
                stack.append(successor)
            seen.add(successor)
    return river_size


def river_sizes(matrix: List[List[int]]) -> List[int]:
    visited = set()
    rivers = []
    for row, col_vals in enumerate(matrix):
        for col in range(len(col_vals)):
            maze_cords = (row, col)
            value = matrix[maze_cords[0]][maze_cords[1]]
            if value == 0:
                visited.add(maze_cords)
            else:
                result = measure_river_size(matrix, maze_cords, visited)
                if result != -1:
                    rivers.append(result)
    return sorted(rivers)


if __name__ == "__main__":
    test_matrix = [
        [1, 0, 0, 1, 0],
        [1, 0, 1, 0, 0],
        [0, 0, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [1, 0, 1, 1, 0],
    ]
    result = river_sizes(test_matrix)
    assert result == [1, 2, 2, 5]
