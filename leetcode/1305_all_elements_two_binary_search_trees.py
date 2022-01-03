from typing import List


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

    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        first_values = []
        self.in_order_traverse(root1, first_values)
        second_values = []
        self.in_order_traverse(root2, second_values)

        result = []
        while first_values and second_values:
            if first_values[0] < second_values[0]:
                result.append(first_values.pop(0))
            else:
                result.append(second_values.pop(0))
        if not first_values:
            result = result + second_values
        if not second_values:
            result = result + first_values
        return result
