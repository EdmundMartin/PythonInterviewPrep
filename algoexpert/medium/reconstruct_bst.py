from typing import List


class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def reconstruct_bst(pre_order_values: List[int]) -> BST:
    ...