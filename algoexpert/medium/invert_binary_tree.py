from typing import List, Optional

from algoexpert.utils.binary_tree import BinaryTree


def invert_binary_tree(tree: Optional[BinaryTree]) -> None:
    queue = [tree]
    while queue:
        current = queue.pop(0)
        if current is None:
            continue
        current.left, current.right = current.right, current.left
        queue.append(current.left)
        queue.append(current.right)


def invert_binary_tree_recursive(tree: Optional[BinaryTree]) -> None:
    if tree is None:
        return
    tree.left, tree.right = tree.right, tree.left
    invert_binary_tree_recursive(tree.left)
    invert_binary_tree_recursive(tree.right)


def _in_order_traverse(tree: BinaryTree, values: List[int]) -> None:
    if tree is None:
        return
    _in_order_traverse(tree.left, values)
    values.append(tree.value)
    _in_order_traverse(tree.right, values)


if __name__ == "__main__":
    tree = BinaryTree(10)
    tree.left = BinaryTree(7)
    tree.right = BinaryTree(12)
    invert_binary_tree(tree)
    new_order = []
    _in_order_traverse(tree, new_order)
    assert new_order == [12, 10, 7]
