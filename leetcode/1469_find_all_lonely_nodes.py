from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:

        queue = [root]
        lonely_nodes = []

        while queue:
            current_node = queue.pop()

            if current_node.left and not current_node.right:
                lonely_nodes.append(current_node.left.val)
            if current_node.right and not current_node.left:
                lonely_nodes.append(current_node.right.val)

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        return lonely_nodes