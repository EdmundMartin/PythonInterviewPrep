from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Runtime: 32 ms, faster than 67.79% of Python3 online submissions for Sum Root to Leaf Numbers.
# Memory Usage: 14.4 MB, less than 18.63% of Python3 online submissions for Sum Root to Leaf Numbers.
class Solution:

    def sum_paths(self, paths: List[List[int]]):
        total = 0
        for path in paths:
            path_as_num = int(''.join([str(p) for p in path]))
            total += path_as_num
        return total

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        unique_paths = []
        queue = [(root, [])]
        while queue:
            current_node, path = queue.pop(0)
            path.append(current_node.val)

            if current_node.left:
                queue.append((current_node.left, path[:]))
            if current_node.right:
                queue.append((current_node.right, path[:]))
            if not current_node.left and not current_node.right:
                unique_paths.append(path)
        return self.sum_paths(unique_paths)