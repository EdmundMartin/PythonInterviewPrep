"""
Sort Stack:
Write a program to sort a stack that the smallest elements on top.
You can use an additional temporary stack, but you may not copy the elements
into any other data structure.
"""


class SimpleStack:

    def __init__(self):
        self.stack = []

    def push(self, value: int) -> None:
        self.stack.append(value)

    def pop(self) -> int:
        if len(self.stack) == 0:
            raise ValueError("Empty stack")
        value, self.stack = self.stack[-1], self.stack[:-1]
        return value

    def peek(self) -> int:
        return self.stack[-1]

    def __len__(self):
        return len(self.stack)

    def __str__(self):
        return str(self.stack)


def sort_stack(stack: SimpleStack) -> SimpleStack:
    replacement = SimpleStack()
    while len(stack) > 0:
        tmp = stack.pop()
        while len(replacement) > 0 and replacement.peek() > tmp:
            stack.push(replacement.pop())
        replacement.push(tmp)

    while len(replacement) > 0:
        stack.push(replacement.pop())
    return stack


if __name__ == '__main__':
    test_array = [8, 1, 4, 7, 6, 5, 11, 18, 8]
    s = SimpleStack()
    s.stack = test_array
    sort_stack(s)
    print(s)