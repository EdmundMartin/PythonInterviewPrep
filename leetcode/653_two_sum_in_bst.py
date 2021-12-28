from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Runtime: 80 ms, faster than 68.09% of Python3 online submissions for Two Sum IV - Input is a BST.
# Memory Usage: 16.6 MB, less than 72.67% of Python3 online submissions for Two Sum IV - Input is a BST.
class Solution:

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if not root:
            return False
        seen_numbers = set()
        queue = [root]
        while queue:
            current_node = queue.pop()
            if (k - current_node.val) in seen_numbers:
                return True
            seen_numbers.add(current_node.val)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        return False


if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right = TreeNode(6)
    root.right.right = TreeNode(7)

    result = Solution().findTarget(root, 9)
    assert result is True