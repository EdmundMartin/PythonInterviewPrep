from algoexpert.utils.binary_tree import BinaryTree
from typing import List


def branch_sum_helper(root: BinaryTree, running_sum: int, sums: List[int]) -> None:
    if root is None:
        return
    new_running_sum = running_sum + root.value
    if root.left is None and root.right is None:
        sums.append(new_running_sum)
        return
    branch_sum_helper(root.left, new_running_sum, sums)
    branch_sum_helper(root.right, new_running_sum, sums)


def branch_sums(root: BinaryTree) -> List[int]:
    sums = []
    branch_sum_helper(root, 0, sums)
    return sums


if __name__ == '__main__':
    root = BinaryTree(10)
    root.left = BinaryTree(8)
    root.left.left = BinaryTree(6)
    root.left.left.left = BinaryTree(4)
    root.right = BinaryTree(12)
    root.right.right = BinaryTree(20)

    result = branch_sums(root)
    assert result == [28, 42]