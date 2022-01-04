from typing import List


def search_in_sorted_matrix(grid: List[List[int]], target: int) -> List[int]:
    row = 0
    col = len(grid[0]) - 1

    while row < len(grid) and col >= 0:
        current_value = matrix[row][col]
        if current_value > target:
            col -= 1
        elif current_value < target:
            row += 1
        else:
            return [row, col]
    return [-1, -1]


if __name__ == "__main__":
    test_target = 44
    matrix = [
        [1, 4, 7, 12, 15, 1000],
        [2, 5, 19, 31, 32, 1001],
        [3, 8, 24, 33, 35, 1002],
        [40, 41, 42, 44, 45, 1003],
        [99, 100, 103, 106, 128, 1004],
    ]
    result = search_in_sorted_matrix(matrix, test_target)
    assert result == [3, 3]
