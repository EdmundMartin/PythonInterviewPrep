

class BinaryTree:
    def __init__(self, value: int, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, diameter, height):
        self.diameter = diameter
        self.height = height


def binary_tree_diameter(root: BinaryTree) -> int:
    return get_tree_info(root).diameter


def get_tree_info(tree: BinaryTree) -> TreeInfo:
    if tree is None:
        return TreeInfo(0, 0)
    left_tree_info = get_tree_info(tree.left)
    right_tree_info = get_tree_info(tree.right)
    longest_path_through_root = left_tree_info.height + right_tree_info.height
    max_diameter_so_far = max(left_tree_info.diameter, right_tree_info.diameter)
    current_diameter = max(longest_path_through_root, max_diameter_so_far)
    current_height = 1 + max(left_tree_info.height, right_tree_info.height)
    return TreeInfo(current_diameter, current_height)


