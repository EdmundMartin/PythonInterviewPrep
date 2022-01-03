from dataclasses import dataclass
from typing import List, Union


@dataclass
class PlaceHolder:
    value: int
    min: Union[int, float]


class StackWithMin:
    def __init__(self):
        self.stack: List[PlaceHolder] = []

    def push(self, value: int) -> None:
        old_min = float("inf") if len(self.stack) == 0 else self.stack[-1].min
        self.stack.append(PlaceHolder(value, min(old_min, value)))

    def pop(self) -> int:
        if len(self.stack) == 0:
            raise ValueError("Empty stack")
        placeholder, self.stack = self.stack[-1], self.stack[:-1]
        return placeholder.value

    def peek(self) -> int:
        return self.stack[-1].value

    def min(self) -> int:
        return self.stack[-1].min
