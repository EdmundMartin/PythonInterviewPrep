from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeInfo:
    def __init__(self, height, diameter):
        self.height = height
        self.diameter = diameter


class Solution:
    def recurse_tree(self, root: Optional[TreeNode]) -> TreeInfo:
        if root is None:
            return TreeInfo(0, 0)
        left_tree = self.recurse_tree(root.left)
        right_tree = self.recurse_tree(root.right)
        longest_path = left_tree.height + right_tree.height
        max_diameter = max(left_tree.diameter, right_tree.diameter)
        current_diameter = max(longest_path, max_diameter)
        current_height = 1 + max(left_tree.height, right_tree.height)
        return TreeInfo(current_height, current_diameter)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.recurse_tree(root).diameter
