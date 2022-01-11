from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def in_order_traversal(self, node: Optional[TreeNode], values, k):
        if node is None or len(values) - 1 == k:
            return
        self.in_order_traversal(node.left, values, k)
        values.append(node.val)
        self.in_order_traversal(node.right, values, k)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        values = []
        self.in_order_traversal(root, values, k)
        return values[k - 1]