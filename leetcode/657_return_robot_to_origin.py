
class Position:

    def __init__(self):
        self.x = 0
        self.y = 0

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Solution:
    def judgeCircle(self, moves: str) -> bool:
        start = Position()
        pos = Position()
        for move in moves:
            if move == "U":
                pos.y += 1
            elif move == "D":
                pos.y -= 1
            elif move == "L":
                pos.x -= 1
            else:
                pos.x += 1
        return pos == start
