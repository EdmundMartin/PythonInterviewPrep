from typing import List


# Runtime: 100 ms, faster than 99.95% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.
# Memory Usage: 15.2 MB, less than 46.88% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        n_rows = len(grid) - 1
        n_cols = len(grid[0])

        row, col = n_rows, 0
        count = 0
        while row >= 0 and col < n_cols:
            if grid[row][col] < 0:
                negative_count = n_cols - col
                count += negative_count
                row -= 1
            else:
                col += 1
        return count


if __name__ == "__main__":
    test_input = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
    result = Solution().countNegatives(test_input)
    print(result)
