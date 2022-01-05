from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        prev = None
        current_node = root

        while current_node:
            if val > current_node.val:
                prev = current_node
                current_node = current_node.right
            else:
                prev = current_node
                current_node = current_node.left

        if not prev:
            return TreeNode(val)

        if val > prev.val:
            prev.right = TreeNode(val)
        else:
            prev.left = TreeNode(val)
        return root
