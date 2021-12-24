from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        queue = [(root, 0)]
        found = False
        while queue:
            node, current_sum = queue.pop(0)
            current_sum = current_sum + node.val
            if node.left:
                queue.append((node.left, current_sum))
            if node.right:
                queue.append((node.right, current_sum))
            if not node.left and not node.right:
                if current_sum == targetSum:
                    return True
        return found
