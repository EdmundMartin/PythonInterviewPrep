from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Runtime: 32 ms, faster than 59.51% of Python3 online submissions for Binary Tree Preorder Traversal.
# Memory Usage: 14.3 MB, less than 46.06% of Python3 online submissions for Binary Tree Preorder Traversal.
class Solution:

    def pre_order_helper(self, node: Optional[TreeNode], values: List[int]) -> None:
        if not node:
            return
        values.append(node.val)
        self.pre_order_helper(node.left, values)
        self.pre_order_helper(node.right, values)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        values = []
        self.pre_order_helper(root, values)
        return values
