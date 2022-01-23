

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def maxDepth(self, root: 'Node') -> int:
        max_depth = 1
        if root is None:
            return 0
        queue = [(root, 1)]
        while queue:
            current_node, depth = queue.pop(0)
            max_depth = max(depth, max_depth)
            for child in current_node.children:
                queue.append((child, depth + 1))
        return max_depth
