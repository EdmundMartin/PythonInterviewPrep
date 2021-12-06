"""
Describe how you could use a single array to implement three stacks
"""
from typing import List


class FixedMultiStack:

    number_of_stacks = 3

    def __init__(self, stack_size: int) -> None:
        self.stack_capacity = stack_size
        self.values: List[int] = [-999 for _ in range(stack_size * self.number_of_stacks)]
        self.sizes: List[int] = [0 for _ in range(self.number_of_stacks)]

    def push(self, stack_number: int, value: int) -> None:
        if self.is_full(stack_number):
            raise ValueError("Stack is full")
        self.sizes[stack_number] += 1
        self.values[self.index_top_of(stack_number)] = value

    def pop(self, stack_number: int):
        if self.is_empty(stack_number):
            raise ValueError("Stack is empty")
        top_index = self.index_top_of(stack_number)
        value = self.values[top_index]
        self.values[top_index] = -999
        self.sizes[stack_number] -= 1
        return value

    def peek(self, stack_number: int):
        if self.is_empty(stack_number):
            raise ValueError("Stack is empty")
        return self.values[self.index_top_of(stack_number)]

    def is_empty(self, stack_number: int):
        return self.sizes[stack_number] == 0

    def is_full(self, stack_number: int):
        return self.sizes[stack_number] == self.stack_capacity

    def index_top_of(self, stack_number: int):
        offset = stack_number * self.stack_capacity
        size = self.sizes[stack_number]
        return offset + size - 1