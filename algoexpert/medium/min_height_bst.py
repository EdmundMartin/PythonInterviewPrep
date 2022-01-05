from typing import Optional, List


class BST:
    def __init__(self, value: int):
        self.value = value
        self.left: Optional['BST'] = None
        self.right: Optional['BST'] = None

    def insert(self, value: int):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)


def construct_min_height_bst(array: List[int], start_idx: int, end_idx: int) -> Optional[BST]:
    if end_idx < start_idx:
        return
    middle_idx = (start_idx + end_idx) // 2
    bst = BST(array[middle_idx])
    bst.left = construct_min_height_bst(array, start_idx, middle_idx - 1)
    bst.right = construct_min_height_bst(array, middle_idx + 1, end_idx)
    return bst


def min_height_bst(array: List[int]) -> BST:
    return construct_min_height_bst(array, 0, len(array) - 1)