from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Runtime: 60 ms, faster than 97.22% of Python3 online submissions for Two Sum BSTs.
# Memory Usage: 20.1 MB, less than 53.75% of Python3 online submissions for Two Sum BSTs.
class Solution:

    def in_order_traversal(self, node: Optional[TreeNode], values):
        if not node:
            return
        self.in_order_traversal(node.left, values)
        values.add(node.val)
        self.in_order_traversal(node.right, values)

    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:

        first_results = set()
        self.in_order_traversal(root1, first_results)

        queue = [root2]
        while queue:
            current_node = queue.pop(0)
            if target - current_node.val in first_results:
                return True
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        return False