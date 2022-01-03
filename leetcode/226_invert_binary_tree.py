from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Runtime: 32 ms, faster than 67.92% of Python3 online submissions for Invert Binary Tree.
# Memory Usage: 14.1 MB, less than 76.31% of Python3 online submissions for Invert Binary Tree.
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        queue = [root]
        while queue:
            current_node = queue.pop(0)
            if not current_node:
                continue
            current_node.left, current_node.right = (
                current_node.right,
                current_node.left,
            )
            queue.append(current_node.left)
            queue.append(current_node.right)
        return root
