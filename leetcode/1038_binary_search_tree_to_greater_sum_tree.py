

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def in_order_traverse(self, root, values):
        if not root:
            return
        self.in_order_traverse(root.left, values)
        values.append(root)
        self.in_order_traverse(root.right, values)

    def bstToGst(self, root: TreeNode) -> TreeNode:
        stack = []
        accumulator = 0
        self.in_order_traverse(root, stack)
        while stack:
            node = stack.pop()
            node.val += accumulator
            accumulator = node.val
        return root
