from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int):
        if not root:
            return 0
        total_sum = 0
        queue = [root]
        while queue:
            current_node = queue.pop(0)
            if current_node.val >= low and current_node.val <= high:
                total_sum += current_node.val
            if current_node.right and current_node.val <= high:
                queue.append(current_node.right)
            if current_node.left and current_node.val >= low:
                queue.append(current_node.left)
        return total_sum
