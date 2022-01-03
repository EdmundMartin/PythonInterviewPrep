from typing import Optional


class BinaryTree:
    def __init__(self, value: int):
        self.value = value
        self.left: Optional["BinaryTree"] = None
        self.right: Optional["BinaryTree"] = None
