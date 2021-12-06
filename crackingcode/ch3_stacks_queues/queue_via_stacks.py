"""
Implement an instance of MyQueue which implements a queue using two stacks.
"""
from typing import List


class MyQueue:

    def __init__(self):
        self.oldest: List[int] = []
        self.newest: List[int] = []

    def add(self, value: int):
        self.newest.append(value)

    def peek(self) -> int:
        self._shift_stacks()
        if len(self.oldest) == 0:
            raise ValueError("Empty stacks")
        return self.oldest[-1]

    def pop(self) -> int:
        self._shift_stacks()
        if len(self.oldest) == 0:
            raise ValueError("Empty stacks")
        value, self.oldest = self.oldest[-1], self.oldest[:-1]
        return value

    def _shift_stacks(self):
        if len(self.oldest) == 0:
            while len(self.newest) > 0:
                self.oldest.append(self.newest.pop())

    def __len__(self):
        return len(self.oldest) + len(self.newest)