from typing import List


# Runtime: 4068 ms, faster than 93.01% of Python3 online submissions for Word Search.
# Memory Usage: 14.5 MB, less than 15.40% of Python3 online submissions for Word Search.
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        max_rows = len(board)
        max_cols = len(board[0])

        for row in range(max_rows):
            for col in range(max_cols):
                if board[row][col] == word[0]:
                    if self.depth_first_search(board, word, (row, col)):
                        return True
        return False

    def depth_first_search(self, board, current_str, cords):
        if len(current_str) == 1:
            return True

        num_rows = len(board)
        num_cols = len(board[0])

        row, col = cords
        board[row][col] = "#"
        if (row - 1) >= 0 and board[row - 1][col] == current_str[1]:
            if self.depth_first_search(board, current_str[1:], (row - 1, col)):
                return True
        if (row + 1) < num_rows and board[row + 1][col] == current_str[1]:
            if self.depth_first_search(board, current_str[1:], (row + 1, col)):
                return True
        if (col - 1) >= 0 and board[row][col - 1] == current_str[1]:
            if self.depth_first_search(board, current_str[1:], (row, col - 1)):
                return True
        if (col + 1) < num_cols and board[row][col + 1] == current_str[1]:
            if self.depth_first_search(board, current_str[1:], (row, col + 1)):
                return True

        board[row][col] = current_str[0]

        return False
