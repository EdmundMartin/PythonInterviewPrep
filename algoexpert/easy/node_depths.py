from typing import Optional

from algoexpert.utils.binary_tree import BinaryTree


def node_depths(root: Optional[BinaryTree], depth: int) -> int:
    if root is None:
        return 0
    return (
        depth + node_depths(root.left, depth + 1) + node_depths(root.right, depth + 1)
    )


if __name__ == "__main__":
    root = BinaryTree(10)
    root.left = BinaryTree(9)
    root.right = BinaryTree(11)
    root.left.left = BinaryTree(8)
    root.right.right = BinaryTree(12)
    root.right.right.right = BinaryTree(14)

    depth = node_depths(root, 0)
    assert depth == 9
