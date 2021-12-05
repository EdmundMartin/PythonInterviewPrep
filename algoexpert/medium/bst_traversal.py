from typing import List

from algoexpert.utils.binary_tree import BinaryTree


def in_order(tree: BinaryTree, array: List[int]) -> List[int]:
    if tree is not None:
        in_order(tree.left, array)
        array.append(tree.value)
        in_order(tree.right, array)
    return array


def pre_order(tree: BinaryTree, array: List[int]) -> List[int]:
    if tree is not None:
        array.append(tree.value)
        pre_order(tree.left, array)
        pre_order(tree.right, array)
    return array


def post_order(tree: BinaryTree, array: List[int]) -> List[int]:
    if tree is not None:
        post_order(tree.left, array)
        post_order(tree.right, array)
        array.append(tree.value)
    return array
