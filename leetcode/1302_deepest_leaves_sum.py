from typing import Optional
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        levels = defaultdict(list)

        queue = [(root, 0)]
        while queue:
            current_node, level = queue.pop()
            if current_node.left is None and current_node.right is None:
                levels[level].append(current_node.val)
            if current_node.left:
                queue.append((current_node.left, level + 1))
            if current_node.right:
                queue.append((current_node.right, level + 1))
        max_level = max(list(levels.keys()))
        return sum(levels[max_level])
