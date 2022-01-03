from typing import Optional


class BST:
    def __init__(self, value: int):
        self.value = value
        self.left: Optional["BST"] = None
        self.right: Optional["BST"] = None


def find_closest(target: int, original: int, new_value: int) -> int:
    if abs(target - original) < abs(target - new_value):
        return original
    return new_value


def find_closest_value(root: BST, target: int) -> int:
    closest = root.value
    node = root
    while node:
        if node.value == target:
            return target
        if target < node.value:
            closest = find_closest(target, closest, node.value)
            node = node.left
        elif target > node.value:
            closest = find_closest(target, closest, node.value)
            node = node.right
    return closest
