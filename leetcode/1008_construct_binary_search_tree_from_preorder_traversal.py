from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None

        current_value = preorder[0]
        right_tree_idx = len(preorder)

        for idx in range(1, len(preorder)):
            value = preorder[idx]
            if value >= current_value:
                right_tree_idx = idx
                break

        left_tree = self.bstFromPreorder(preorder[1:right_tree_idx])
        right_tree = self.bstFromPreorder(preorder[right_tree_idx:])

        return TreeNode(current_value, left_tree, right_tree)