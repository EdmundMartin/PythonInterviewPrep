from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Runtime: 44 ms, faster than 71.53% of Python3 online submissions for Validate Binary Search Tree.
# Memory Usage: 16.5 MB, less than 52.26% of Python3 online submissions for Validate Binary Search Tree.
class Solution:
    def validation_helper(
        self, tree: Optional[TreeNode], min_value: int, max_value: int
    ) -> bool:
        if tree is None:
            return True
        if tree.val <= min_value or tree.val >= max_value:
            return False
        left_valid = self.validation_helper(tree.left, min_value, tree.val)
        right_valid = self.validation_helper(tree.right, tree.val, max_value)
        return left_valid and right_valid

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validation_helper(root, float("-inf"), float("inf"))


if __name__ == "__main__":
    root = TreeNode(val=1)
    root.right = TreeNode(val=1)
    result = Solution().isValidBST(root)
    assert result is False
