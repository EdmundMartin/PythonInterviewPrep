# Runtime: 56 ms, faster than 91.18% of Python3 online submissions for Min Stack.
# Memory Usage: 18.4 MB, less than 27.29% of Python3 online submissions for Min Stack.


class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            new_min = val
        else:
            top, current_min = self.stack[-1]
            new_min = min(val, current_min)
        self.stack.append((val, new_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        top, current_min = self.stack[-1]
        return top

    def getMin(self) -> int:
        top, current_min = self.stack[-1]
        return current_min
