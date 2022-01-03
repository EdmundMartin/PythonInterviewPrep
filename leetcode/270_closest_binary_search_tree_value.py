from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Runtime: 40 ms, faster than 69.84% of Python3 online submissions for Closest Binary Search Tree Value.
# Memory Usage: 16.1 MB, less than 59.29% of Python3 online submissions for Closest Binary Search Tree Value.
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        diff = float("inf")
        result = None
        queue = [root]
        while queue:
            current_node = queue.pop()
            if current_node is None:
                continue
            new_diff = abs(current_node.val - target)
            if new_diff < diff:
                result = current_node.val
                diff = new_diff
            if current_node.val > target:
                queue.append(current_node.left)
            if current_node.val < target:
                queue.append(current_node.right)
        return result


if __name__ == "__main__":
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)

    result = Solution().closestValue(root, 3.714286)
    assert result == 4

    root = TreeNode(1)
    result = Solution().closestValue(root, 4.428571)
    assert result == 1

    root = TreeNode(1)
    root.right = TreeNode(2)
    result = Solution().closestValue(root, 3.428571)
    assert result == 2
