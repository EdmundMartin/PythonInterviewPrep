

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def in_order_traversal(node: TreeNode, values):
    if not node:
        return
    in_order_traversal(node.left, values)
    values.append(node.val)
    in_order_traversal(node.right, values)


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        values = []
        in_order_traversal(root, values)
        head_value = values.pop(0)
        head = TreeNode(head_value)
        current = head
        for value in values:
            current.next = TreeNode(value)
            current = current.next
        return head
