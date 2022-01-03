from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Runtime: 32 ms, faster than 60.28% of Python3 online submissions for Same Tree.
# Memory Usage: 14.4 MB, less than 31.75% of Python3 online submissions for Same Tree.
class Solution:
    def is_same_recurse(self, first: Optional[TreeNode], second: Optional[TreeNode]):
        if first is None and second is None:
            return True
        if first is None or second is None:
            return False
        is_same = first.val == second.val
        return (
            self.is_same_recurse(first.left, second.left)
            and self.is_same_recurse(first.right, second.right)
            and is_same
        )

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.is_same_recurse(p, q)
