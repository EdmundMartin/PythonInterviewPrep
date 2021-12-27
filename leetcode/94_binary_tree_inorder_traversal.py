from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Runtime: 32 ms, faster than 60.87% of Python3 online submissions for Binary Tree Inorder Traversal.
# Memory Usage: 14.3 MB, less than 12.87% of Python3 online submissions for Binary Tree Inorder Traversal.
class Solution:

    def in_order_helper(self, node: Optional[TreeNode], values):
        if not node:
            return
        self.in_order_helper(node.left, values)
        values.append(node.val)
        self.in_order_helper(node.right, values)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        values = []
        self.in_order_helper(root, values)
        return values