from typing import List


class StackItem:
    def __init__(self, val, max):
        self.val = val
        self.max = max


class MaxStack:

    def __init__(self):
        self.stack: List[StackItem] = []

    def push(self, x: int) -> None:
        if len(self.stack) == 0:
            self.stack.append(StackItem(x, x))
        else:
            last_max = self.stack[-1].max
            self.stack.append(StackItem(x, max(x, last_max)))

    def pop(self) -> int:
        stack_item = self.stack.pop()
        return stack_item.val

    def top(self) -> int:
        stack_item = self.stack[-1]
        return stack_item.val

    def peekMax(self) -> int:
        stack_item = self.stack[-1]
        return stack_item.max

    def popMax(self) -> int:
        current_max = self.stack[-1].max
        tmp = []
        while self.top() != current_max:
            tmp.append(self.pop())
        return_value = self.stack.pop()
        while tmp:
            self.push(tmp.pop())
        return return_value.val