from typing import Union

from algoexpert.utils.binary_tree import BinaryTree


def validation_helper(
    tree: BinaryTree, min_value: Union[float, int], max_value: Union[float, int]
) -> bool:
    if tree is None:
        return True
    if tree.value < min_value or tree.value >= max_value:
        return False
    left_valid = validation_helper(tree.left, min_value, tree.value)
    right_valid = validation_helper(tree.right, tree.value, max_value)
    return left_valid and right_valid


def validate_bst(tree: BinaryTree) -> bool:
    return validation_helper(tree, float("-inf"), float("inf"))


if __name__ == "__main__":
    valid_tree = BinaryTree(10)
    valid_tree.left = BinaryTree(7)
    valid_tree.left.left = BinaryTree(6)
    valid_tree.left.right = BinaryTree(7)
    assert validate_bst(valid_tree) is True

    invalid_tree = BinaryTree(10)
    invalid_tree.right = BinaryTree(12)
    invalid_tree.right.left = BinaryTree(11)
    invalid_tree.right.right = BinaryTree(8)
    assert validate_bst(invalid_tree) is False
