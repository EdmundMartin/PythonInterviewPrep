from typing import List


class Solution:
    def find_rook_captures(self, board, rook_pos, direction) -> int:
        row, col = rook_pos
        while 0 <= row < 8 and 0 <= col < 8:
            if board[row][col] == "p":
                return 1
            if board[row][col] != "R" and board[row][col] != ".":
                return 0
            row += direction[0]
            col += direction[1]
        return 0

    def numRookCaptures(self, board: List[List[str]]) -> int:
        rook_pos = None
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "R":
                    rook_pos = (row, col)
                    break
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        return sum([self.find_rook_captures(board, rook_pos, d) for d in directions])


if __name__ == "__main__":
    board = [
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", "p", ".", ".", ".", "."],
        [".", ".", ".", "R", ".", ".", ".", "p"],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", "p", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
    ]
    result = Solution().numRookCaptures(board)
    assert result == 3

    board = [
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", "p", "p", "p", "p", "p", ".", "."],
        [".", "p", "p", "B", "p", "p", ".", "."],
        [".", "p", "B", "R", "B", "p", ".", "."],
        [".", "p", "p", "B", "p", "p", ".", "."],
        [".", "p", "p", "p", "p", "p", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
    ]
    result = Solution().numRookCaptures(board)
    assert result == 0

    board = [
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", "p", ".", ".", ".", "."],
        [".", ".", ".", "p", ".", ".", ".", "."],
        ["p", "p", ".", "R", ".", "p", "B", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", "B", ".", ".", ".", "."],
        [".", ".", ".", "p", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
    ]
    result = Solution().numRookCaptures(board)
    assert result == 3
