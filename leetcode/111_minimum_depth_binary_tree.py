# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        min_depth = float('inf')
        queue = [(root, 1)]
        while queue:
            current_node, depth = queue.pop(0)
            if current_node.left:
                queue.append((current_node.left, depth + 1))
            if current_node.right:
                queue.append((current_node.right, depth + 1))
            if not current_node.left and not current_node.right:
                min_depth = min(depth, min_depth)
        return min_depth