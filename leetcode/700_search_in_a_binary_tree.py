from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return
        current_node = root
        found_node = None
        while current_node:
            if val < current_node.val:
                current_node = current_node.left
            elif val > current_node.val:
                current_node = current_node.right
            else:
                found_node = current_node
                break
        return found_node