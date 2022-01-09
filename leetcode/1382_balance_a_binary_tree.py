

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def in_order_traverse(self, node: TreeNode, values):
        if not node:
            return
        self.in_order_traverse(node.left, values)
        values.append(node.val)
        self.in_order_traverse(node.right, values)

    def construct_bst(self, values, left, right):
        if left > right:
            return
        middle = left + (right - left) // 2
        root = TreeNode(values[middle])
        root.left = self.construct_bst(values, left, middle - 1)
        root.right = self.construct_bst(values, middle + 1, right)
        return root

    def balanceBST(self, root: TreeNode) -> TreeNode:
        tree_values = []
        self.in_order_traverse(root, tree_values)
        return self.construct_bst(tree_values, 0, len(tree_values) - 1)
