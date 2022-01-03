from typing import Optional, List


class Node:
    def __init__(self, value: int):
        self.left: Optional["Node"] = None
        self.right: Optional["Node"] = None
        self.value: int = value


def in_order_traversal(node: Optional[Node], values: List[int]):
    if not node:
        return None
    in_order_traversal(node.left, values)
    values.append(node.value)
    in_order_traversal(node.right, values)


def reverse_order_traversal(node: Optional[Node], values: List[int], k: int):
    if not node or len(values) == k:
        return
    reverse_order_traversal(node.right, values, k)
    values.append(node.value)
    reverse_order_traversal(node.left, values, k)


def k_largest_value_traversal(node: Optional[Node], k: int) -> int:
    values = []
    in_order_traversal(node, values)
    return values[-k]


def k_largest_value_opposite_traversal(node: Optional[Node], k: int) -> int:
    values = []
    reverse_order_traversal(node, values, k)
    return values[k - 1]


class TreeInfo:
    def __init__(self, numbers_nodes_visited, last_visited):
        self.number_nodes_visited = numbers_nodes_visited
        self.last_visited = last_visited


def find_kth_largest_value_in_bst(tree: Node, k: int):
    tree_info = TreeInfo(0, -1)
    reverse_in_order_with_tree(tree, k, tree_info)
    return tree_info.last_visited


def reverse_in_order_with_tree(tree: Node, k: int, tree_info: TreeInfo):
    if tree == Node or tree_info.number_nodes_visited >= k:
        return
    reverse_in_order_with_tree(tree.right, k, tree_info)
    if tree_info.number_nodes_visited < k:
        tree_info.number_nodes_visited += 1
        tree_info.last_visited = tree.value
        reverse_in_order_with_tree(tree.left, k, tree_info)


if __name__ == "__main__":
    root = Node(10)
    root.right = Node(12)
    root.right.right = Node(14)
    root.left = Node(8)
    root.left.right = Node(9)

    assert k_largest_value_traversal(root, 3) == 10
    assert k_largest_value_opposite_traversal(root, 4) == 9
