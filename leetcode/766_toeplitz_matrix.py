from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        groups = {}

        for row, rov_vals in enumerate(matrix):
            for col, val in enumerate(rov_vals):
                diag = row - col
                if diag not in groups:
                    groups[diag] = val
                else:
                    if groups[diag] != matrix[row][col]:
                        return False
        return True


if __name__ == '__main__':
    test_matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
    result = Solution().isToeplitzMatrix(test_matrix)
    assert result is True
